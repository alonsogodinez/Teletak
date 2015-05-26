from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .forms import LoginForm

class Login(View):
    form_class = LoginForm
    template_name = 'login/index.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form':form })

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form, 'error': 'Verifique los datos ingresados'})


