from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import View, CreateView
from forms import *
from django.http import HttpResponse,HttpResponseRedirect
from Teletak.mixins import SuccessMessageMixin
from apps.usuarios.models import User
class LoginRequiredMixin(object):
    u"""Ensures that user must be authenticated in order to access view."""

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class Index(LoginRequiredMixin, View):

    template_name = 'almacen/index.html'
    def get(self, request):
        return render(request, self.template_name)

class Operaciones(LoginRequiredMixin,View):
    template_name='almacen/operaciones/index.html'
    def get(self,request):
        return render(request,self.template_name)



class Ingreso(LoginRequiredMixin,SuccessMessageMixin,View):

    template_name = 'almacen/ingresos/index.html'
    model = Ingreso

    def get(self,request):
        ingresos_form= IngresoForm
        formset = DetalleIngresoFormSet(prefix='formset')
        guiaremision_form = GuiaRemisionForm

        return render(request,self.template_name,locals())

    def post(self,request):

        ingresos_form= IngresoForm(request.POST)
        guiaremision_form = GuiaRemisionForm(request.POST)

        if ingresos_form.is_valid()  and guiaremision_form.is_valid():
            nuevo_ingreso = ingresos_form.save(commit=False)
            nuevo_ingreso.dni_usuario = request.user
            nuevo_ingreso.tipo = 1
            nuevo_ingreso.guia_remision = guiaremision_form.save()
            nuevo_ingreso.save()

            detalle_ingreso = DetalleIngresoFormSet(request.POST,prefix='formset',instance=nuevo_ingreso,)
            if detalle_ingreso.is_valid():

                for detalle in detalle_ingreso.save(commit=False):
                    detalle.id_almacen = Almacen.objects.get(id=request.POST['almacen'])
                detalle_ingreso.save()
                success_message = 'Los datos se actualizaron correctamente'
                return redirect("/operaciones")
            return render(request,self.template_name,locals())
        else:

            return render(request,self.template_name,locals())




class Reingresos(LoginRequiredMixin,View):

    template_name = 'almacen/reingresos/index.html'
    model = Ingreso

    def get(self,request):
        ingresos_form= IngresoForm
        formset = DetalleIngresoFormSet(prefix='formset')

        return render(request,self.template_name,locals())

    def post(self,request):

        ingresos_form= IngresoForm(request.POST)


        if ingresos_form.is_valid() :
            nuevo_ingreso = ingresos_form.save(commit=False)
            nuevo_ingreso.dni_usuario = request.user
            nuevo_ingreso.tipo = 2
            nuevo_ingreso.save()

            detalle_ingreso = DetalleIngresoFormSet(request.POST,prefix='formset',instance=nuevo_ingreso)

            if detalle_ingreso.is_valid():

                for detalle in detalle_ingreso.save(commit=False):
                    detalle.id_almacen = Almacen.objects.get(id=request.POST['almacen'])

                detalle_ingreso.save()
                success_message = 'Los datos se actualizaron correctamente'
                return redirect("/operaciones")

        return render(request,self.template_name,locals())



class Salidas(LoginRequiredMixin,View):
    template_name='almacen/salidas/index.html'
    def get(self,request):
        return render(request,self.template_name)

