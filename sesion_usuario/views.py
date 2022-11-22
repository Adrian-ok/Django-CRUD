from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.models import User

#--------------------------------------------------------------------------------------------#
#INICIAR SESION
def log_in(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form' : AuthenticationForm 
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password']) #Guardo en user la autentificacion del usuario

        if user is None: #si user esta vacio, no se inicia sesion porque no encontro usuario con los datos que se ingresaron
            return render(request, 'login.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o Contraseña Incorrecto'
            })
        else:
            login(request, user) #Guardo el id de sesion
            return redirect('home')

#--------------------------------------------------------------------------------------------#
#CERRAR SESION
def log_out(request):
    logout(request)
    # return redirect('log_in')
    response = redirect('log_in')
    response.delete_cookie('user_location')
    return response

#--------------------------------------------------------------------------------------------#
#REGISTRARSE
def registrar(request): #Registrarse
    if request.method == 'GET': #si llega a traves de get esta tratando de ver la interfaz por ende se la muestro.
        return render(request, 'reg.html', {
            'form': UserCreationForm
        })
    else: #si llega por POST esta obteniendo datos.
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                password=request.POST['password1'])
                user.save()
                return redirect('log_in')
            except IntegrityError: #Se pueden manejar errores especificos ejemplo error de integridad producido por la duplicidad de datos
                return render(request, 'reg.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                }) 
        return render(request, 'reg.html', {
            'form': UserCreationForm,
            'error': 'Las contraseñas no coinciden'
        })

