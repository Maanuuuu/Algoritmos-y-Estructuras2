#Modulo de gestion de tareas y prioridades

#Crear la class "proyecto" para crear el objeto de proyecto
class Proyecto:

    def __init__(self,ide,nombre,empresa_cliente,descripcion,fi,fv,estado_actual,porcentaje,tarea=[]):
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
        self.siguiente = None

    def agregar_subtarea(self,subtarea):
        self.subtareas.append(subtarea)

#Crear la class "Subtarea" para crear el objeto de subtarea
class Subtarea:
    def __init__(self, ide, nombre, descripcion, estado):
        self.ide = ide
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado

#Generar clase Cola para almacenar
class Cola_Al:
    def __init__(self):
        self.cabeza = None
        self.cola = None
    
    def agregar_archivo(self, ide,nombre,cliente,descripcion,fi,fv,estado,avance):
        Entarea = Tarea(ide,nombre,cliente,descripcion,fi,fv,estado,avance)
        if not self.cabeza:
            self.cabeza = Entarea
            self.cola = Entarea
        else:
            self.cola.siguiente = Entarea
            self.cola = Entarea
    
    def mostrar_TODOS_archivos(self):
        temp = self.cabeza
        while temp:
            print("Id:", temp.ide)
            print("Nombre:", temp.nombre)
            print("Cliente:", temp.cliente)
            print("Descripcion:", temp.descripcion)
            print("Fecha de inicio de tarea:", temp.fi)
            print("Fecha de vencimiento de tarea::", temp.fv)
            print("El estado de tarea:", temp.estado)
            print("El avance de tarea:", temp.avance)
            print()
            temp = temp.siguiente
    
    def eliminar_archivo_cima(self):
        if not self.cabeza:
            return None
        eliminado = self.cabeza
        self.cabeza = self.cabeza.siguiente
        return eliminado

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
    return ide,nombre,empresa,descripcion,fi,fv,estado_actual,porcentaje

#Agregar Subtarea area para la tarea correspondiente
def Montar_subtarea(band,band_yn,aux_tarea):
    while band_yn == 1:
        if band.lower() == "s":
            cant = input("Cuanto cantidad de subtarea quiere agregar: ")
            bandera_numeral = 0
            while bandera_numeral==0:
                if cant.isdigit():
                    bandera_numeral = 1
                else:
                    print("")
                    cant = input("Cuanto cantidad de subtarea quiere agregar: ")
            numeral_exitosa = int(cant)
            for i in range (numeral_exitosa):
                print("SubTarea {0:02}".format(i+1))
                tareaid,tareanombre,tareadescripcion,tareaestado = Ingresar_subtarea()
                tareanuevo = Subtarea(tareaid,tareanombre,tareadescripcion,tareaestado)
                aux_tarea.append(tareanuevo)
            band_yn = 0
        elif band.lower() == "n":
            print("No ha agregado nada subtarea")
            band_yn = 0
        else:
            print("No esta ingresado la opcion indicado, por favor ingresar de de nuevo")
            band = input("¿Desear agregar Subtarea? Si-> s No -> n: ")

#Agregar Tarea para el proyecto correspondiente
def agregar_tarea(band,band_yn,aux_tarea):
    while band_yn == 1:
        if band.lower() == "s":
            cant = input("Cuanto cantidad de tarea quiere agregar: ")
            bandera_numeral = 0
            while bandera_numeral==0:
                if cant.isdigit():
                    bandera_numeral = 1
                else:
                    print("")
                    cant = input("Cuanto cantidad de tarea quiere agregar: ")
            numeral_exitosa = int(cant)
            for i in range (numeral_exitosa):
                print("Tarea {0:02}".format(i+1))
                tareaid,tareanombre,tareacliente,tareadescripcion,tareafi,tareafv,tareaestado,tareaavance = Ingresar_tarea()
                sub_band = input("¿Desear agregar Subtarea? Si-> s No -> n: ")
                sub_bandyn = 1
                aux_subtarea = []
                Montar_subtarea(sub_band,sub_bandyn,aux_subtarea)
                tareanuevo = Tarea(tareaid,tareanombre,tareacliente,tareadescripcion,tareafi,tareafv,tareaestado,tareaavance)
                tareanuevo.agregar_subtarea(aux_subtarea)
                aux_tarea.append(tareanuevo)
            band_yn = 0
        elif band.lower() == "n":
            print("No ha agregado nada tarea")
            band_yn = 0
        else:
            print("No esta ingresado la opcion indicado, por favor ingresar de de nuevo")
            band = input("¿Desear agregar Tarea? Si-> s No -> n: ")

#Almacenar por forma de pila
class proyecto_pila:

    def __init__(self):
        self.cabeza = None

    def agreagar_proyecto(self): #Funcion de agregar
        ide,nombre,empresa_cliente,descripcion,fi,fv,estado_actual,porcentaje = Ingresar()
        band = input("¿Desear agregar Tarea? Si-> s No -> n: ")
        band_yn = 1 #Para que el usuario ingresa bien la opcion
        aux_tarea = []
        agregar_tarea(band,band_yn,aux_tarea)
        lista_proyecto = Proyecto(ide,nombre,empresa_cliente,descripcion,fi,fv,estado_actual,porcentaje,aux_tarea)
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