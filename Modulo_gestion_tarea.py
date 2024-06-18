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

#Crear la class "Tarea" para crear el objeto de tarea
class Tarea:

    def __init__(self,ide,nombre,cliente,descripcion,inicio,vencimiento,estado,avance=""):
        self.ide=ide
        self.nombre=nombre
        self.cliente=cliente
        self.descripcion=descripcion
        self.inicio=inicio
        self.vencimieno=vencimiento
        self.estado=estado
        self.avance=avance
        self.subtareas=[]

    def agregar_subtarea(self,subtarea):
        self.subtareas.append(subtarea)

#Crear la class "Subtarea" para crear el objeto de subtarea
class Subtarea:
    def __init__(self, ide, nombre, descripcion, estado):
        self.ide = ide
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado

#Ingreso por Tarea
def Ingresar_tarea():
    ide = int(input("El id de tarea: "))
    nombre = input("El nombre de tarea: ")
    cliente = input("El nombre de cliente en la tarea: ")
    descripcion = input("La descripcion de tarea: ")
    fi = input("Fecha de inicio de tarea: ")
    fv = input("Fecha de vencimiento de tarea: ")
    estado = input("El estado de tarea: ")
    avance = int(input("El avance de tarea: "))
    return ide,nombre,cliente,descripcion,fi,fv,estado,avance

#Ingreso por Subtarea
def Ingresar_subtarea ():
    ide = int(input("Id de proyecto: "))
    nombre = input("El nombre de Subtarea: ")
    descripcion = input("La descripcion de subtarea: ")
    estado_actual = input("El estado actual de proyecto: ")
    return ide,nombre,descripcion,estado_actual

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
    
    def mostrar_ALL_proyectos (self): #Funcion de mostrar todos los proyectos para imprimir
        inicial = self.cabeza
        if inicial != None:
            while inicial:
                print()
                print("El id de proyecto: ",inicial.ide)
                print("El nombre de proyecto: ",inicial.nombre)
                print("El nombre de empresa en el proyecto: ",inicial.empresa_cliente)
                print("La descripcion de proyecto: ",inicial.descripcion)
                print("Fecha de inicio: ",inicial.fi)
                print("Fecha de vencimiento: ",inicial.fv)
                print("El porcentaje de proyecto: ",inicial.porcentaje)
                print("Tarea de proyecto: ",inicial.tarea)
                inicial = inicial.siguiente
        else:
            print("Vacio")
    
    def eliminar_archivo(self): #Funcion de para eliminar el archivo por cima de vector
        if not self.cabeza:
            return None
        else:
            self.cabeza = self.cabeza.siguiente
    
#Colocando para haciendo pruebas
Test = proyecto_pila()
Test.agreagar_proyecto()
Test.mostrar_ALL_proyectos()
Test.eliminar_archivo()
Test.mostrar_ALL_proyectos()