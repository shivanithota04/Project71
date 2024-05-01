from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# Create your views here.

class Home(View):
    def get(self, request):
        return render(request, 'home.html')


class RegisterInput(View):
    def get(self, request):
        return render(request, 'register.html')


class LoginInput(View):
    def get(self, request):
        return render(request, 'login.html')




# Create your views here.
