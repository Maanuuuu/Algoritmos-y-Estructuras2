#Modulo de gestion de tareas y prioridades

#Crear la class "proyecto" para crear el objeto de proyecto
class Proyecto:

    def __init__(self,ide,nombre,empresa_cliente,descripcion,fi,fv,estado_actual,porcentaje,tarea):
        self.ide = ide
        self.nombre = nombre
        self.empresa_cliente = empresa_cliente
        self.descripcion = descripcion
        self.fi = fi
        self.fv = fv
        self.estado_actual = estado_actual
        self.porcentaje = porcentaje
        self.tarea = tarea
        self.siguiente = None

#Para el usuario que pueda ingresar
def Ingresar ():
    ide = int(input("El id de proyecto: "))
    nombre = input("El nombre de proyecto: ")
    empresa = input("El nombre de empresa en el proyecto: ")
    descripcion = input("La descripcion de proyecto: ")
    fi = input("Fecha de inicio de proyecto: ")
    fv = input("Fecha de vencimiento de proyecto: ")
    estado_actual = input("El estado actual de proyecto: ")
    porcentaje = int(input("El porcentaje de proyecto: "))
    cant = int(input("Cuanto cantidad de tarea quiere agregar: "))
    #for i in range (cant):
    return ide,nombre,empresa,descripcion,fi,fv,estado_actual,porcentaje,cant

#Almacenar por forma de pila
class proyecto_pila:

    def __init__(self):
        self.cabeza = None

    def agreagar_proyecto(self): #Funcion de agregar
        ide,nombre,empresa_cliente,descripcion,fi,fv,estado_actual,porcentaje,tarea = Ingresar()
        lista_proyecto = Proyecto(ide,nombre,empresa_cliente,descripcion,fi,fv,estado_actual,porcentaje,tarea)
        if self.cabeza == None:
            self.cabeza = lista_proyecto
        else:
            lista_proyecto.siguiente = self.cabeza
            self.cabeza = lista_proyecto