from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect , redirect, render_to_response, HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import View, ListView, DeleteView
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from Teletak.mixins import SuccessMessageMixin
from .forms import *
from .models import Ingreso,DetalleIngreso,Salida,DetalleAlmacen,DetalleStock
from django.views.generic.detail import DetailView

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

class IngresoView(LoginRequiredMixin,SuccessMessageMixin,View):

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

        if ingresos_form.is_valid() and guiaremision_form.is_valid():
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
                InsertarDetalleAlmacen(nuevo_ingreso.id,request.POST['almacen'])
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
                InsertarDetalleAlmacen(nuevo_ingreso.id,request.POST['almacen'])
                success_message = 'Los datos se actualizaron correctamente'
                return redirect("/operaciones")

        return render(request,self.template_name,locals())



#SALIDAS
import datetime

class SalidaView(LoginRequiredMixin,View,SuccessMessageMixin):
    template_name = 'almacen/salidas/index.html'
    def get(self, request):
        salidaform = SalidaForm
        formset = DetalleSalidaFormset(prefix='formset')
        #Verificar stock minimo
        stock = DetalleStock.objects.all()
        prod_list = []
        for item in stock:
            if item.stock < item.producto.stock_minimo:
                prod_list.append({'nombre':item.producto.descripcion, 'cantidad':item.stock,'almacen': item.id_almacen.ubicacion})
        print prod_list
        if prod_list.__len__() >0:
            return render_to_response(self.template_name,{'salidaform':salidaform,'formset':formset,'prod_list':prod_list,'status':True},context_instance=RequestContext(request))
        else:
            return render_to_response(self.template_name,{'salidaform':salidaform,'formset':formset},context_instance=RequestContext(request))
    def post(self,request):
        salidaform = SalidaForm(request.POST)
        if salidaform.is_valid() :
            salida = salidaform.save(commit=False)
            salida.fecha = datetime.date.today()
            salida.save()
            formset = DetalleSalidaFormset(request.POST,prefix='formset',instance=salida)
            if formset.is_valid():
                for detalle in formset.save(commit=False):
                    ActualizarSalida(detalle.id_almacen,detalle.codigo_producto,detalle.cantidad)
                formset.save()
                return  HttpResponseRedirect("/operaciones/listar_salidas")
            else:
                return render(request,self.template_name,locals())

        else:
            formset = DetalleSalidaFormset(request.POST,prefix="formset")
            return render_to_response(self.template_name,{'salidaform': salidaform,'formset':formset},context_instance=RequestContext(request))

class DetalleSalidaView(LoginRequiredMixin,View):
    def get(self,request,id):
        object_list = Salida.objects.all()
        sal = Salida.objects.get(pk=id)
        det = DetalleSalida.objects.filter(id_salida=id)
        template_name = 'almacen/salidas/lista_salidas.html'
        status = True
        return render(request,template_name,locals())


class ListarSalidas(LoginRequiredMixin,ListView):
    model = Salida
    template_name = 'almacen/salidas/lista_salidas.html'

class EliminarSalida(SuccessMessageMixin,DeleteView):
    model = Salida
    success_url = '/operaciones/listar_salidas'
    template_name = 'almacen/salidas/confirm_delete_salida.html'
    success_message = 'El registro de salida fue eliminado correctamente'

class ListarIngresos(LoginRequiredMixin,ListView):
    model = Ingreso
    template_name = 'almacen/ingresos/lista_ingresos.html'

class DetalleIngresoView(LoginRequiredMixin,View):
    def get(self,request,id):
        object_list = Ingreso.objects.all()
        sal = Ingreso.objects.get(pk=id)
        det = DetalleIngreso.objects.filter(id_ingreso=id)
        template_name = 'almacen/ingresos/lista_ingresos.html'
        status = True
        return render(request,template_name,locals())



#Funcion que se usa despues de cada ingreso(o reingreso) para insertar un registro en detallealmacen, y actualizar el stock
def InsertarDetalleAlmacen(ingreso_id,almacen_id):
    for p in DetalleIngreso.objects.filter(id_ingreso = ingreso_id).distinct('codigo_producto'):
        objeto = DetalleIngreso.objects.filter(id_ingreso = ingreso_id, codigo_producto = p.codigo_producto.codigo)
        cantidad = 0
        for r in objeto:
            cantidad = cantidad +  r.cantidad
        nuevo = DetalleAlmacen()
        nuevo.codigo_producto = Producto.objects.get(pk=p.codigo_producto.codigo)
        nuevo.id_almacen = Almacen.objects.get(pk=almacen_id)
        nuevo.id_ingreso = Ingreso.objects.get(pk=ingreso_id)
        nuevo.cantidad = cantidad
        nuevo.save()
        update = DetalleStock.objects.filter(id_almacen=almacen_id).filter(producto=p.codigo_producto.codigo)
        for item in update:
                item.stock = item.stock + cantidad
                item.save()
        if len(update) == 0:
            objeto = DetalleStock()
            objeto.id_almacen = Almacen.objects.get(pk=almacen_id)
            objeto.producto = Producto.objects.get(pk=p.codigo_producto.codigo)
            objeto.stock = cantidad
            objeto.save()

#Funcion que se utiliza para actualizar el stock luego de una salida
def ActualizarSalida(almacen_id,producto_id,cantidad):
    lista = DetalleStock.objects.filter(id_almacen = almacen_id).filter(producto = producto_id)
    print lista
    for item in lista:
        item.stock = item.stock - cantidad
        item.save()

#SOLO PARA PRUEBAS
class ActualizarStock:
    almacen = 0
    def __init__(self,almacen):
        self.almacen = int(almacen)
    def ActualizarTodoStock(self):
        stock = []
        for p in Producto.objects.all():
            contador = 0
            lista = DetalleAlmacen.objects.filter(id_almacen=self.almacen).filter(codigo_producto=p.codigo)
            for c in lista:
                contador = contador + c.cantidad
            if contador>0:
                stock.append((p.codigo,contador))
                d = DetalleStock.objects.filter(id_almacen=self.almacen).filter(producto=p)
                for item in d:
                    item.stock = contador
                    item.save()
                if len(d) == 0:
                    objeto = DetalleStock()
                    objeto.id_almacen = Almacen.objects.get(pk =  self.almacen )
                    objeto.producto = p
                    objeto.stock = contador
                    objeto.save()
        #print [ (p.codigo,p.descripcion) for p in Producto.objects.all()]
        return stock



#FUNCIONES PARA LOS SELECTS DINAMICOS
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def getProductosfromAlmacen(request):
    req  = request.body
    data = json.loads(req)
    lista = []
    productos = DetalleStock.objects.filter(id_almacen=data['almacen']).exclude(producto__in=data['productos'])
    for p in productos:
        lista.append({"codigo" : p.producto.codigo, "nombre" : p.producto.descripcion},)
    return HttpResponse(json.dumps(lista),content_type='application/json')

def getCantidadfromProductos(request,almacen_id,producto_id):
    lista = []
    items = DetalleStock.objects.filter(id_almacen=almacen_id,producto=producto_id)
    for p in items:
        lista.append({"max_value":p.stock},)
    return HttpResponse(json.dumps(lista),content_type='application/json')

class Reporte(View):
    template_name = 'almacen/reporte.html'

    def get(self, request):
        productos = Producto.objects.all()
        ingresos = Ingreso.objects.all()
        detalles = DetalleIngreso.objects.all()
        guia_remision = GuiaRemision.objects.all()
        return render(request, self.template_name, locals())
