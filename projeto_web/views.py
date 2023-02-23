from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required #para ele nao deixa o cara entrar na minha pagina sem estar logado
from .models import Empresa

# depois das url.py eu venho aqui ai depois eu crio a pagina em html
@login_required(login_url='/login/')
def register_empresa(request):
    empresa_id = request.GET.get("id")
    if empresa_id:
        empresa = Empresa.objects.get(id=empresa_id)
        if empresa.user == request.user:
            return render(request,"register-empresa.html",{"empresa":empresa})
    return render(request,"register-empresa.html")

    return render(request,'register-empresa.html')

@login_required(login_url='/login/')
def set_empresa(request):
    cidade = request.POST.get('cidade')
    email = request.POST.get('email')
    telefone = request.POST.get('telefone')
    descrisao = request.POST.get('descrisao')
    foto = request.FILES.get('file')
    empresa_id = request.POST.get('empresa-id')
    user = request.user
    if empresa_id:
        empresa = Empresa.objects.get(id=empresa_id)
        if user == empresa.user:
            empresa.email = email
            empresa.cidade = cidade
            empresa.telefone = telefone
            empresa.descrisao = descrisao
            if foto:
                empresa.foto = foto
            empresa.save()   
    else:
        empresa= Empresa.objects.create(email=email, telefone=telefone, descrisao=descrisao, foto=foto, user=user , cidade=cidade)
        url= '/empresa/detail/{}/'.format(empresa.id)
    return redirect(url)

@login_required(login_url='/login/')
def delete_empresa(request, id):
    empresa=Empresa.objects.get(id=id)
    if empresa.user == request.user :
        empresa.delete()
    return redirect('/')

@login_required(login_url='/login/')
def list_all_empresa(request):
    empresa= Empresa.objects.filter(ativo=True)
    return render(request,'list.html',{'empresa':empresa})

def list_user_empresa(request):
    empresa= Empresa.objects.filter(ativo=True, user=request.user)
    return render(request,'list.html',{'empresa':empresa})

def empresa_detail(request, id):
    empresa=Empresa.objects.get(ativo=True, id=id)
    print(empresa.id)
    return render(request,'empresa.html',{'empresa':empresa})
    
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
  