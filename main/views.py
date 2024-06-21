from django.shortcuts import render
from django.db import connection

# Create your views here.
def query1(request):
    cursor = connection.cursor()
    cursor.execute("insert into main_curso (cod, nombre, activo) values ('RP4', 'Repostería', true)")
    return HttpResponse('Listo')