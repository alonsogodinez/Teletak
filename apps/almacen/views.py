from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect , redirect, render_to_response
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from Teletak.mixins import SuccessMessageMixin
from .forms import *
from .models import User,Ingreso,DetalleIngreso,Salida,DetalleSalida

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

class Ingresos(LoginRequiredMixin,View,SuccessMessageMixin):
    template_name='almacen/ingresos/index.html'
    def get(self,request):
        return render(request,self.template_name)
    def post(self,request):
        ingresos_form= IngresoForm(request.POST)
        detalleingreso_form = DetalleIngresoForm(request.POST)
        producto_form = ProductoForm(request.POST)
        guiaremision_form = GuiaRemisionForm(request.POST)
        if ingresos_form.is_valid() and detalleingreso_form.is_valid() and producto_form.is_valid() \
                and guiaremision_form.is_valid():

            nuevo_item = ingresos_form.save(commit=False)
            nuevo_item.guia_remision = guiaremision_form.save()
            nuevo_item1 = detalleingreso_form.save(commit=False)
            nuevo_item1.id_ingreso=nuevo_item.save()
            nuevo_item1.codigo_producto=producto_form.save()
            nuevo_item1.save()
            success_message = 'Los datos se actualizaron correctamente'

            return redirect("/ingresos/")
        else:
            template_name = 'almacen/ingresos'
            usuario_form = UsuarioForm
            ingresos_form = IngresoForm
            detalleingreso_form = DetalleIngreso
            producto_form = ProductoForm
            guiaremision_form = GuiaRemisionForm
            proveedores_form = ProveedoresForm

            return render(request,template_name,locals())

class IngresoMultiple(LoginRequiredMixin,SuccessMessageMixin,View):

    template_name = 'almacen/ingresos/ingreso_multiple.html'
    model = Ingreso

    def get(self,request):
        ctx = {}
        ctx['ingresos_form']= IngresoForm()
        ctx['formset'] = DetalleIngresoFormSet()
        ctx['guiaremision_form'] = GuiaRemisionForm()


        return render(request,self.template_name,ctx)

    def post(self,request):
        ingresos_form= IngresoForm(request.POST)
        guiaremision_form = GuiaRemisionForm(request.POST)
        print "holaaa"

        print request.POST

        if ingresos_form.is_valid()  and guiaremision_form.is_valid():
            print "aca estoy"
            nuevo_item = ingresos_form.save(commit=False)
            nuevo_item.guia_remision = guiaremision_form.save()
            nuevo_item.save()
            formset = DetalleIngresoFormSet(request.POST,instance=nuevo_item)
            if formset.is_valid():
                formset.save()
                success_message = 'Los datos se actualizaron correctamente'
                return HttpResponseRedirect("/operaciones")
            return render(request,self.template_name,locals())

        else:

            return render(request,self.template_name,locals())




class Reingresos(LoginRequiredMixin,View):
    template_name='almacen/reingresos/index.html'
    def get(self,request):
        return render(request,self.template_name)


#salidas
import datetime

class SalidaView(LoginRequiredMixin,View):
    def get(self, request):
        salidaform = SalidaForm
        formset = AddDetalleFormset
        form = DetalleSalidaForm
        return render_to_response('almacen/salidas/index.html',locals(),context_instance=RequestContext(request))
    def post(self,request):
        print request.POST
        salida_form = SalidaForm(request.POST)
        formset = AddDetalleFormset(request.POST)
        form = DetalleSalidaForm
        if salida_form.is_valid and formset.is_valid:
            salida = salida_form.save(commit=False)
            salida.fecha = datetime.date.today()
            salida.save()
            for form in formset.forms:
                object = form.save(commit=False)
                if form.has_changed():
                    object.id_salida = salida
                    object.save()
            return  HttpResponseRedirect("/operaciones")
        else:
            return render_to_response('almacen/salidas/index.html',locals(),context_instance=RequestContext(request))


def RegistrarSalida(request):
    print request.POST['mitoken']
    if request.POST['mitoken'] == "1" or request.POST['mitoken'] == 1:
        print "El token si es 1"
        form_salida = SalidaForm(request.POST)
        if form_salida.is_valid():
            SalidaInstancia = form_salida.save(commit=False)
            SalidaInstancia.fecha = datetime.date.today()
            SalidaInstancia.save()
            new_sal = AddDetalleFormset(prefix='sal',instance=SalidaInstancia)
            return render_to_response('almacen/salidas/index.html',{'sal':new_sal,'register':False,'id': SalidaInstancia.id},context_instance=RequestContext(request))
        else:
            form_salida = SalidaForm()
            return render_to_response('almacen/salidas/index.html',{'form_salida':form_salida,'register':True},context_instance=RequestContext(request))
    else:
         print "El token es 0"
         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



def AddDetalleSalida(request):
        id = request.POST['id']
        print "Id nr %s " %id
        SalidaInstancia = Salida.objects.get(pk=id)
        if request.method == 'POST':
            if 'add_detalle' in request.POST:
                cp = request.POST.copy()
                cp['sal-TOTAL_FORMS'] = int(cp['sal-TOTAL_FORMS'])+ 1
                new_sal = AddDetalleFormset(cp,prefix='sal')
            elif 'submit' in request.POST:
                formset = AddDetalleFormset(request.POST,instance=SalidaInstancia)
                if formset.is_valid:
                    formset.save()
                    return HttpResponseRedirect("/")
        else:
            new_sal = AddDetalleFormset (prefix='sal',instance=SalidaInstancia)
        return render_to_response('almacen/salidas/index.html',{'sal':new_sal,'register':False,'id':id},context_instance=RequestContext(request))
