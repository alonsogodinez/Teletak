from django.contrib.auth.decorators import login_required
from django.shortcuts import render,render_to_response
from django.utils.decorators import method_decorator
from django.views.generic import View, CreateView,TemplateView, ListView, UpdateView, DeleteView
from apps.almacen.models import Producto
from Teletak.mixins import SuccessMessageMixin
from django.http import HttpResponse,HttpResponseRedirect
from .forms import ProductoForm
from django.template.context import RequestContext

class LoginRequiredMixin(object):
    u"""Ensures that user must be authenticated in order to access view."""

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class Index(LoginRequiredMixin, View):
    template_name = 'productos/index.html'
    def get(self, request):
        return render(request, self.template_name)

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form, 'error': 'Verifique los datos ingresados'})

class ListarProductos(LoginRequiredMixin,ListView):
    queryset = Producto.objects.all()
    template_name = 'productos/listar_productos.html'

class EliminarProducto(SuccessMessageMixin,DeleteView):

    model = Producto
    success_url = '/productos/listar'
    template_name = 'productos/confirm_delete_producto.html'
    success_message = 'El producto fue eliminado correctamente'

class RegistrarProducto(LoginRequiredMixin,SuccessMessageMixin,CreateView):

    model = Producto
    template_name = 'productos/nuevo_producto.html'
    form_class =  ProductoForm()
    success_url = '/productos/listar'
    success_message = 'El registro se realizo correctamente'
    def get(self, request, *args, **kwargs):
        template = "productos/nuevo_producto.html"
        form=ProductoForm()
        return render_to_response(template,context_instance=RequestContext(request,locals()))
    def post(self, request, *args, **kwargs):
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            enlace = form.save(commit = False)
            enlace.usuario = request.user
            enlace.save()
            return HttpResponseRedirect("/")



class EditarProducto(SuccessMessageMixin,UpdateView):

    model = Producto
    form_class = ProductoForm
    success_url = '/productos/listar'
    template_name = 'configuracion/editar_trabajador.html'
    success_message = 'Los datos se actualizaron correctamente'
