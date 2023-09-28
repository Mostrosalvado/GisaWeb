from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from Home.forms import RegisterForm,ContactForm
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.core.paginator import Paginator
from Obras.models import  Obra
from Loteos.models import Lote

# Create your views here.

def home (request):
    #Sacar obras
    obras=Obra.objects.all()
    #Paginar obras
    paginacion=Paginator(obras,3)
    #Obtener numero de pagina
    page = request.GET.get('page')
    page_obras= paginacion.get_page(page)

    #Sacar obras
    lotes=Lote.objects.all()
    #Paginar obras
    paginacion=Paginator(lotes,3)
    #Obtener numero de pagina
    page = request.GET.get('page')
    page_lotes= paginacion.get_page(page)

    return render(request, "home.html",{
        'title':'Innovación que Construye Futuros',
        'obras':page_obras,
        'lotes': page_lotes
    })

def trabaja (request):

    return render(request, "trabaja.html",{
        'title':'Trabaja con nosotros',

    })

def sobreNosotros (request):

    return render(request, "SobreNosotros.html",{
        'title':'Sobre Nosotros',
    })



def contacto(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            # Guarda los datos en variables
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            message = contact_form.cleaned_data['message']

            # Contenido del correo
            subject = f'Nuevo mensaje de contacto de {name}'
            body = f'Nombre: {name}\nCorreo electrónico: {email}\nMensaje: {message}'

            # Enviar el correo
            to_email = 'diealesal@gmail.com'  # Dirección de correo deseada
            from_email = contact_form.cleaned_data['email']  # Usar el correo electrónico del usuario que envía el mensaje
            email = EmailMessage(subject, body, to=[to_email], from_email=from_email)

            
            try:
                email.send()
                messages.success(request, '¡Tu mensaje ha sido enviado!')
            except Exception as e:
                messages.error(request, 'Hubo un error al enviar el mensaje.')

            return redirect('home')
        else:
            messages.error(request, 'Por favor, corrija los errores en el formulario.')
    else:
        contact_form = ContactForm()

    return render(request, "contacto.html", {
        'form': contact_form,
    })



def login_page (request):
    if request.method == 'POST':
            username = request.POST.get ('username')
            password = request.POST.get ('password')

            user = authenticate(request , username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('obras')
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
            else:
                messages.warning(request,'Hubo un problema, intenta nuevamente')
        return render(request , 'users/register.html',{
            'title':"Registro",
            'register_form': register_form
        })

def en_construccion (request):

    return render(request, "en_construccion.html")

@login_required(login_url="login")
def logout_user (request):
    logout(request)
    return redirect ('home')