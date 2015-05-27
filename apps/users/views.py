from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import LoginForm



class Login(View):
    form_class = LoginForm
    template_name = 'login/index.html'
    user_check_failure_path = '/login'

    def get(self, request):
        print request.user.is_authenticated
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
                return redirect(request.GET['next'])
            return render(request, self.template_name, {'form': form, 'error': 'La cuenta esta deshabilitada'})

        else:
            return render(request, self.template_name, {'form': form, 'error': 'Verifique los datos ingresados'})




class Logout(View):

    def get(self,request):
            logout(request)
            return redirect('/login')







