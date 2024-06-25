from dia3.models import Tarea, SubTarea

def crear_nueva_tarea(*descripciones:str):
    for descripcion in descripciones:
        t = Tarea(descripcion=descripcion)
        t.save()
    imprimir_en_pantalla()
# Para crear varias tareas a la vez: 
# crear_nueva_tarea('Tarea uno', 'Tarea dos', 'Tarea Tres')

def crear_sub_tarea(*descripciones:str, idtarea):
    t = Tarea.objects.get(id=idtarea)
    for descripcion in descripciones:
        st = SubTarea(descripcion=descripcion, tarea=t)
        st.save()
# Para crear varias subtareas asignadas a una tarea a la vez:
# crear_sub_tarea("subtarea uno", "subtarea dos", idtarea=3)

def elimina_tarea(idtarea:int):
    t = Tarea.objects.get(id=idtarea) 
    t.eliminada = True
    t.save()

def elimina_sub_tarea(idsubtarea:int):
    st = SubTarea.objects.get(id=idsubtarea) 
    st.eliminada = True
    st.save()

# def recupera_tarea(idtarea):
#     t = Tarea.objects.get(id=idtarea) 
#     t.eliminada = False
#     t.save()

def imprimir_en_pantalla():
    tareas = recupera_tareas_y_sub_tareas()
    for t in tareas:
        print (f'[{t.id}] {t.descripcion}')
        for sub_tarea in t.subtareas.filter(eliminada=False):
            print (f'       [{sub_tarea.id}] {sub_tarea.descripcion}')


def recupera_tareas_y_sub_tareas():
    tareas = Tarea.objects.filter(eliminada=False)
    return tareas

'''
[1] descripción tarea 1
.... [1] sub tarea 1
.... [2] sub tarea 2
[2] descripción tarea 2
.... [3] sub tarea 1
.... [4] sub tarea 2
'''