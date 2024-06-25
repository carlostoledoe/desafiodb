from django.shortcuts import render, redirect

# Create your views here.
def counter(request):
    # Preguntamos si ya existe la variable 
    veces = request.session.get('veces', None) # Es un diccionario
    # Si es la primera vez que accede, inicamos en 0
    if veces is None:
        veces = 0
    # le sumamos 1 a la cantidad de visitas de ESE usuario
    veces += 1
    # Guardamos la sesión
    request.session['veces'] = veces
    return render(request, 'counter.html')

def resetcounter(request):
    request.session['veces'] = 0
    return redirect('/counter')