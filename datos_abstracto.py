import Gestion_Proyectos as gp

class Nodo_Tarea:
    def __init__(self,tarea):
        self.tarea=tarea
        self.siguiente = None

class Pila_Tareas:
    def __init__(self):
        self.cabeza = None

    def agregar_tarea(self,tarea):
        nuevo_nodo = Nodo_Tarea(tarea)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo

    def mostrar_pila_tareas(self):
        actual = self.cabeza
        while actual:
            if actual.tarea.mostrar_tarea()==None:
                pass
            else:
                actual.tarea.mostrar_tarea()
            actual = actual.siguiente
