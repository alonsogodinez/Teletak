from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View

class LoginRequiredMixin(object):
    u"""Ensures that user must be authenticated in order to access view."""

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class Index(LoginRequiredMixin, View):

    template_name = 'almacen/index.html'
    def get(self, request):
        return render(request, self.template_name)

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form, 'error': 'Verifique los datos ingresados'})
