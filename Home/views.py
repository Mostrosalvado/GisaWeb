from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from Home.forms import RegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home (request):

    return render(request, "home.html",{
        'title':'Inicio',
    })

def trabaja (request):

    return render(request, "trabaja.html",{
        'title':'Trabaja con nosotros',
    })

def sobreNosotros (request):

    return render(request, "SobreNosotros.html",{
        'title':'Sobre Nosotros',
    })



def contacto (request):

    return render(request, "contacto.html",{
        'title':'Contacto',
    })

def login_page (request):
    if request.method == 'POST':
            username = request.POST.get ('username')
            password = request.POST.get ('password')

            user = authenticate(request , username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.warning(request,'No te has identificado correctamente :( ')

    return render(request, "users/login.html",{
        'title':'Iniciar Sesion',
    })

def register (request):
    if request.user.is_authenticated:
        return redirect('home')
    else:

        register_form = RegisterForm()
        if request.method == 'POST':
            register_form = RegisterForm(request.POST)
            if register_form.is_valid():
                register_form.save()
                messages.success(request,'Te has registrado correctamente!!')
                return redirect('home')
        return render(request , 'users/register.html',{
            'title':"Registro",
            'register_form': register_form
        })

def en_construccion (request):

    return render(request, "en_construccion.html")

@login_required(login_url="login")
def logout_user (request):
    logout(request)
    return redirect ('login')