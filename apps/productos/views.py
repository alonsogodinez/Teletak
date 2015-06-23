from django.contrib.auth.decorators import login_required
from django.shortcuts import render,render_to_response
from django.utils.decorators import method_decorator
from django.views.generic import View, CreateView, ListView, UpdateView, DeleteView
from Teletak.mixins import SuccessMessageMixin
from django.http import HttpResponse,HttpResponseRedirect
from .forms import *
from .models import *
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
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/productos/listar")
        else:
            return render(request, self.template_name, {'form': form, 'error': 'Verifique los datos ingresados'})

class EditarProducto(SuccessMessageMixin,UpdateView):

    model = Producto
    form_class = ProductoForm
    success_url = '/productos/listar'
    template_name= 'productos/editar_producto.html'
    success_message = 'Los datos se actualizaron correctamente'

class Categorias(View,LoginRequiredMixin):
    def get(self,request, *args, **kwargs):
        categoria = Categoria.objects.all()
        form = CategoriaForm
        return render_to_response('productos/categorias.html',locals(),context_instance=RequestContext(self.request))
    def post(self,request):
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/productos/categoria")
        else:
            return render(request, self.template_name, {'form': form, 'error': 'Verifique los datos ingresados'})
    def update(self,request):
        pass

class UnidadMedidaProducto(View,LoginRequiredMixin):
    def get(self):
        pass
    def post(self):
        pass
