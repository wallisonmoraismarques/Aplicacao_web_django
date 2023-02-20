from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required #para ele nao deixa o cara entrar na minha pagina sem estar logado

# depois das url.py eu venho aqui ai depois eu crio a pagina em html
@login_required(login_url='/login/')
def index(request):
    return render(request,'index.html')
# este aqui e escrito para eu voltar a pagina inicial do meu sait
def logout_user(request):
    print(request.user)
    logout(request)
    return redirect('/login/')


def login_user(request):
    return render(request, 'login.html')
# este aqui e o do botao
@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.error(request,'usuario e senha invalido')
    return redirect('/login/')
  