from django.contrib.auth.decorators import login_required
from django.shortcuts import render,render_to_response,get_object_or_404, redirect
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

class RegistrarProducto(LoginRequiredMixin,View,SuccessMessageMixin):
    def get(self, request):
        template_name = 'productos/nuevo_producto.html'
        producto_form = ProductoForm
        unidad_producto_form = UnidadProductoForm
        unidad_producto_formset = UnidadProductoFormSet
        return render(request,template_name,locals())
    def post(self,request):
        producto_form = ProductoForm(request.POST)
        unidad_producto_form = UnidadProductoForm(request.POST)
        unidad_producto_formset = UnidadProductoFormSet(request.POST)
        if producto_form.is_valid() :
            unidad_producto =unidad_producto_form.save(commit=False)
            producto = producto_form.save()
            unidad_producto.codigo_producto = producto
            unidad_producto.save()
            success_message = 'Los datos se actualizaron correctamente'
            return redirect('/productos')
        else:
            template_name = 'productos/nuevo_producto.html'
            producto_form = ProductoForm
            return render(request,template_name,locals())


# class Editar_Producto(SuccessMessageMixin,UpdateView):
#
#     model = Producto
#     form_class = ProductoForm
#     success_url = '/usuarios/lista'
#     template_name = 'productos/editar_producto.html'
#     success_message = 'Los datos se actualizaron correctamente'

def Editar_Producto(request,id):
    template_name = 'productos/editar_producto.html'
    producto = get_object_or_404(Producto,pk=id)
    unidad_producto = UnidadProductoForm
    if request.POST:
        producto_form = ProductoForm(request.POST,instance=producto)
        unidadproducto_form = UnidadProductoForm(request.POST)
        #form = ArticleForm(request.POST, instance=article)
        if producto_form.is_valid() and unidadproducto_form.is_valid():
            producto_form.save()
            unidadproducto_form.save()
            # If the save was successful, redirect to another page
            #redirect_url = reverse(article_save_success)
            return HttpResponseRedirect('/productos/')
    else:
        producto_form = ProductoForm(instance=producto)
        unidadproducto_form = UnidadProductoForm(instance=unidad_producto)
        #form = ArticleForm(instance=producto)
    return render_to_response(template_name,locals(), context_instance=RequestContext(request))


class Categorias(View,SuccessMessageMixin):
    template_name = 'productos/categorias.html'
    success_message = 'Los datos se actualizaron correctamente'
    def get(self,request, *args, **kwargs):
        categoria = Categoria.objects.all()
        form = CategoriaForm
        return render_to_response(self.template_name,locals(),context_instance=RequestContext(self.request))
    def post(self,request):
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/productos/categoria")
        else:
            return render(request, self.template_name, {'form': form, 'error': 'Verifique los datos ingresados'})


def Editar_Categoria(request,id):
    cat = Categoria.objects.get(pk=id)
    if request.POST:
        form = CategoriaForm(request.POST,instance=cat)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/productos/categoria")
        else:
            return render(request,'productos/categorias.html', {'form': form, 'error': 'Verifique los datos ingresados'})
    else:
        form = CategoriaForm(instance=cat)
        categoria = Categoria.objects.all()
        return render_to_response('productos/categorias.html',locals(),context_instance=RequestContext(request))


class EliminarCategoria(SuccessMessageMixin,DeleteView):

    model = Categoria
    success_url = '/productos/categoria'
    template_name = 'productos/confirm_delete_categoria.html'
    success_message = 'El producto fue eliminado correctamente'



