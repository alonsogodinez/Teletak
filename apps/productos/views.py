from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import View

class Index(View):

    template_name = 'productos/index.html'

    def get(self, request):
        return render(request, self.template_name)

