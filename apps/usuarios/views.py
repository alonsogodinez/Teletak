# -*- encoding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.contrib import messages
from django.shortcuts import render,redirect
from django.utils.decorators import method_decorator
from django.views.generic import View, CreateView,TemplateView, ListView, UpdateView, DeleteView

from .forms import LoginForm, RegistrarTrabajadorForm, EditarTrabajadorForm
from .models import User

from apps.productos.models import *
from apps.almacen.models import *

from Teletak.mixins import SuccessMessageMixin

class LoginRequiredMixin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class AdminPermissionRequiredMixin(object):

    def get(self,request):
        if request.user.is_staff:
            return render(request, self.template_name)
        messages.info(request, 'No tienes acceso a este módulo')
        return redirect('/')

class Login(View):

    form_class = LoginForm
    template_name = 'login/index.html'
    user_check_failure_path = '/login'

    def get(self, request):
        if request.user.is_authenticated():
            return redirect('/')
        form = self.form_class()
        return render(request, self.template_name, {'form':form })

    def post(self,request):
        form = self.form_class(request.POST)

        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            if user.is_active:
                login(request, user)
                if request.GET:
                    return redirect(request.GET['next'])
                return redirect('/')
            return render(request, self.template_name, {'form': form, 'error': 'La cuenta esta deshabilitada'})

        else:
            return render(request, self.template_name, {'form': form, 'error': 'Verifique los datos ingresados'})


class Logout(View):

    def get(self,request):
            logout(request)
            return redirect('/login')


class Configuracion(AdminPermissionRequiredMixin,TemplateView):
    template_name = 'configuracion/index.html'


class RegistrarTrabajador(LoginRequiredMixin,SuccessMessageMixin,CreateView):

    model = User
    template_name = 'configuracion/nuevo_trabajador.html'
    form_class = RegistrarTrabajadorForm
    success_url = '/usuarios'
    success_message = 'El registro se realizó correctamente'

    def form_valid(self, form):
        hasher = PBKDF2PasswordHasher()
        password = hasher.encode(password=self.request.POST['password'], salt='salt', iterations=50000)
        form.instance.password = password
        form.instance.save()
        return super(RegistrarTrabajador, self).form_valid(form)


class ListarTrabajadores(LoginRequiredMixin,ListView):
    queryset = User.objects.all()
    template_name = 'configuracion/listar_trabajadores.html'


class EditarTrabajador(SuccessMessageMixin,UpdateView):

    model = User
    form_class = EditarTrabajadorForm
    success_url = '/usuarios/lista'
    template_name = 'configuracion/editar_trabajador.html'
    success_message = 'Los datos se actualizaron correctamente'


class EliminarTrabajador(SuccessMessageMixin,DeleteView):

    model = User
    success_url = '/usuarios/lista'
    template_name = 'configuracion/confirm_delete_trabajador.html'
    success_message = 'El trabajador fue eliminado correctamente'


class Prueba(View):
    template_name = 'almacen/reporte.html'

    def get(self, request):
        productos = Producto.objects.all()
        ingresos = Ingreso.objects.all()
        detalles = DetalleIngreso.objects.all()
        guia_remision = GuiaRemision.objects.all()
        return render(request, self.template_name, locals())






