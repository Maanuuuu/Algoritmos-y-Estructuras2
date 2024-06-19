from datetime import datetime
import json
import Modulo_Reportes as mr
#Funcion para la lectura de datos del JSON


#Se declara la clase de Proyecto
class Proyecto:

    def __init__(self,id,nombre,descripcion,inicio,vencimiento,estado,empresa,gerente,equipo):
        self.id=id
        self.nombre=nombre
        self.descripcion=descripcion
        self.inicio=inicio
        self.vencimiento=vencimiento
        self.estado=estado
        self.empresa=empresa
        self.gerente=gerente
        self.equipo=equipo
        self.tareas=[]
        self.siguiente=None

    #Se crea una funcion para agregar tareas al proyecto
    def agregar_tarea(self,tarea):
        self.tareas.append(tarea)

    #Funcion para mostrar todos los datos del proyecto
    def mostrar(self):
        print('------')
        print('ID: {:<10}'.format(self.id))
        print('Nombre: {:<15}'.format(self.nombre))
        print('Descripcion: {:<15}'.format(self.descripcion))
        print('Inicio: {:<15}'.format(self.inicio.strftime("%d-%m-%Y")))
        print('Vencimiento: {:<15}'.format(self.vencimiento.strftime("%d-%m-%Y")))
        print('Estado: {:<15}'.format(self.estado))
        print('Empresa: {:<15}'.format(self.empresa))
        print('Gerente: {:<10}'.format(self.gerente))
        print('Equipo: {:<10}'.format(", ".join(self.equipo)))
        print('------')

class Tarea:

    def __init__(self,id,nombre,empresa,descripcion,inicio,vencimiento,estado,porcentaje=""):
        self.id=id
        self.nombre=nombre
        self.empresa=empresa
        self.descripcion=descripcion
        self.inicio=inicio
        self.vencimiento=vencimiento
        self.estado=estado
        self.porcentaje=porcentaje
        self.subtareas=[]
        self.siguiente=None


    def agregar_subtarea(self,subtarea):
        self.subtareas.append(subtarea)

    def mostar_tarea(self):
        print('------')
        print('ID: {:<10}'.format(self.id))
        print('Nombre: {:<15}'.format(self.nombre))
        print('Cliente: {:<15}'.format(self.empresa))
        print('Descripcion: {:<15}'.format(self.descripcion))
        print('Inicio: {:<15}'.format(self.inicio.strftime("%d-%m-%Y")))
        print('Vencimiento: {:<15}'.format(self.vencimiento.strftime("%d-%m-%Y")))
        print('Estado: {:<15}'.format(self.estado))
        print('Porcentaje: {:<10}'.format(self.porcentaje))
        print('------')

class Subtarea:
    def __init__(self, id, nombre, descripcion, estado):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado

class Cargar:
    
    def __init__(self):
        pass
    def cargar_datos_desde_json(nombre_archivo_txt):
        proyectos=[]
        
        def convertir_fecha(fecha_str):
            return datetime.strptime(fecha_str, "%d-%m-%Y")

        with open(nombre_archivo_txt, "r") as archivo_txt:
            nombre_archivo_json = archivo_txt.readline().strip()

        with open(nombre_archivo_json, "r") as archivo_json:
            datos = json.load(archivo_json)
            for proyecto_data in datos["proyectos"]:
                proyecto = Proyecto(
                    proyecto_data["id"],
                    proyecto_data["nombre"],
                    proyecto_data["descripcion"],
                    convertir_fecha(proyecto_data["inicio"]),
                    convertir_fecha(proyecto_data["vencimiento"]),
                    proyecto_data["estado"],
                    proyecto_data["empresa"],
                    proyecto_data["gerente"],
                    proyecto_data["equipo"]
                )
                
                for tarea_data in proyecto_data["tareas"]:
                    tarea = Tarea(
                        tarea_data["id"],
                        tarea_data["nombre"],
                        tarea_data["cliente"],
                        tarea_data["descripcion"],
                        convertir_fecha(tarea_data["inicio"]),
                        convertir_fecha(tarea_data["vencimiento"]),
                        tarea_data["estado"],
                        tarea_data["avance"]
                    )
                    for subtarea_data in tarea_data.get("subtareas", []):
                        subtarea = Subtarea(
                            subtarea_data["id"],
                            subtarea_data["nombre"],
                            subtarea_data["descripcion"],
                            subtarea_data["estado"]
                        )
                        tarea.agregar_subtarea(subtarea)
                    proyecto.agregar_tarea(tarea)
                
                proyectos.append(proyecto)
                
        return proyectos






#Definimos nuestra funcion principal para gestionar los proyectos
class Gestion_de_proyecto:
    def __init__(self):
        self.proyectitos=Cargar.cargar_datos_desde_json("config.txt")
        
        
    def buscar_proyectos(self):  # Añadir self como primer parámetro
        print("Buscar Proyecto por: ")
        print("1.- Nombre: ")
        print("2.- Empresa: ")
        print("3.- Gerente: ")
        print("4.- Equipo: ")
        criterio = str(input("Ingrese opcion: "))

        if criterio == "1":
            nombre = str(input("Introduzca el nombre del proyecto: "))
            filtrado = [proyecto for proyecto in self.proyectitos if nombre.lower() in proyecto.nombre.lower()]
            if filtrado == []:
                print("No existen proyectos con ese nombre")
                return None

        elif criterio == "2":
            empresa = str(input("Introduzca la empresa del proyecto: "))
            filtrado = [proyecto for proyecto in self.proyectitos if empresa.lower() in proyecto.empresa.lower()]
            if filtrado == []:
                print("No existen proyectos de esa empresa")
                return None

        elif criterio == "3":
            gerente = str(input("Introduzca nombre del gerente del proyecto: "))
            filtrado = [proyecto for proyecto in self.proyectitos if gerente.lower() in proyecto.gerente.lower()]
            if filtrado == []:
                print("No existen proyectos administrados por ese gerente")
                return None

        elif criterio == "4":
            integrante = str(input("Introduzca al integrante del equipo del proyecto: "))
            filtrado = [proyecto for proyecto in self.proyectitos if any(integrante.lower() in miembro.lower() for miembro in proyecto.equipo)]
            if filtrado == []:
                print("No existen proyectos administrados por ese equipo")
                return None

        else:
            print("Opcion Invalida")

        if filtrado:
            print("Proyectos encontrados: ")
            for proyecto in filtrado:
                print('ID: {:^10} / Nombre: {:^15}  /  Empresa: {:^15}  /  Equipo: {:^10}  /  Gerente: {:^10}'.format(proyecto.id, proyecto.nombre, proyecto.empresa, ", ".join(proyecto.equipo), proyecto.gerente))

            seleccion = str(input("\nSeleccione el ID del proyecto que desea operar: "))
            for proyecto in filtrado:
                if seleccion == str(proyecto.id):
                    return proyecto

            print("ID invalido")
            return None
                
    def menu(self):
        # Construimos un menú para que el usuario elija la acción a realizar
        print("--------------------")
        print("Gestion del Proyecto ")
        print("Elija la operacion a realizar:")
        print("1.- Crear. ")
        print("2.- Modificar. ")
        print("3.- Consultar. ")
        print("4.- Listar. ")
        print("5.- Eliminar. ")

        self.opcion = str(input("Ingrese opcion: "))
        print()
        if self.opcion == "1":
            self.crear(self.proyectitos)
        elif self.opcion == "2":
            self.modificar(self.proyectitos)
        elif self.opcion == "3":
            self.consultar(self.proyectitos)
        elif self.opcion == "4":
            self.listar(self.proyectitos)
        elif self.opcion == "5":
            self.eliminar(self.proyectitos)
        print()

        print("----------")
        print("Desea seguir con la gestion de Proyectos?: ")
        print("1.- Si\n2.-No")
        seguir = (input(">. "))

        if seguir == "1":
            print("")
            self.menu()
        else:
            print("\nPrograma Finalizado.")
            
                
    def crear(self,proyectitos):
        print("Ingrese las especificaciones del proyecto: ")
        new_proyecto=Proyecto(
                id=str(input("ID: ")),
                nombre=str(input("Nombre: ")),
                descripcion=str(input("Descripcion: ")),
                inicio = datetime.strptime(input("Ingrese la fecha de inicio del proyecto (Dia-Mes-Año): "), "%d-%m-%Y"),
                vencimiento = datetime.strptime(input("Ingrese la fecha de vencimiento del proyecto (Dia-Mes-Año): "), "%d-%m-%Y"),
                estado=str(input("Estado actual: ")),
                empresa=str(input("Empresa: ")),
                gerente=str(input("Gerente: ")),
                equipo=str(input("Equipo: ")).split(",")
            )
        proyectitos.append(new_proyecto)         
    
                
            
    def modificar(self,proyectitos):
        #Se busca el proyecto con el que se va a realizar la accion elegida
        proyecto=self.buscar_proyectos()
        if proyecto != None:
            print("Ingrese las modificaciones del proyecto: ")
            proyecto.id=str(input("ID: "))
            proyecto.nombre=str(input("Nombre: "))
            proyecto.descripcion=str(input("Descripcion: "))
            proyecto.inicio = datetime.strptime(input("Ingrese la fecha de inicio del proyecto (Dia-Mes-Año): "), "%d-%m-%Y")
            proyecto.vencimiento = datetime.strptime(input("Ingrese la fecha de vencimiento del proyecto (Dia-Mes-Año): "), "%d-%m-%Y")
            proyecto.estado=str(input("Estado actual: "))
            proyecto.empresa=str(input("Empresa: "))
            proyecto.gerente=str(input("Gerente: "))
            proyecto.equipo=str(input("Equipo: ")).split(",")
        else: pass
    
    def consultar(self,proyectitos):
        proyecto=self.buscar_proyectos()
        if proyecto!=None:
            print("Informacion del Proyecto:")
            proyecto.mostrar()
        else: pass

    def listar(self,proyectitos):
            for proyecto in proyectitos:
                proyecto.mostrar()
        

    def eliminar(self,proyectitos):
        
        proyecto=self.buscar_proyectos()
        if proyecto!=None:
            option=str(input("Desea borrar el proyecto "+proyecto.nombre+"?: "))
            if option.lower()=="si":
                proyectitos.remove(proyecto)
                print("Proyecto Eliminado")
            else:
                print("Eliminacion cancelada")
        else: pass


def agregar_tarea(band,band_yn,aux_tarea,proyecto):
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
                tareaid,tareanombre,tareaempresa_cliente,tareadescripcion,tareafi,tareafv,tareaestado,tareaavance = Ingresar_tarea()
                band = input("¿Desear agregar Subtarea? Si-> s No -> n: ")

                tareanuevo = Tarea(tareaid,tareanombre,tareaempresa_cliente,tareadescripcion,tareafi,tareafv,tareaestado,tareaavance)
                print(tareanuevo.descripcion)
                aux_tarea.append(tareanuevo)
                proyecto.tareas.append(tareanuevo)
            band_yn = 0
        elif band.lower() == "n":
            print("No ha agregado nada tarea")
            band_yn = 0
        else:
            print("No esta ingresado la opcion indicado, por favor ingresar de de nuevo")
            band = input("¿Desear agregar Tarea? Si-> s No -> n: ")

def Ingresar_tarea():
    ide = int(input("El id de tarea: "))
    nombre = input("El nombre de tarea: ")
    empresa_cliente = input("Empresa Cliente de la tarea: ")
    descripcion = input("La descripcion de tarea: ")
    try:
       
        fi= datetime.strptime(input("Ingrese la fecha de inicio del proyecto (Dia-Mes-Año): "), "%d-%m-%Y")
        fv = datetime.strptime(input("Ingrese la fecha de vencimiento del proyecto (Dia-Mes-Año): "), "%d-%m-%Y")
    except :
        print("Ingrese las fechas en formato Dia-Mes-Año")
        fi= datetime.strptime(input("Ingrese la fecha de inicio del proyecto (Dia-Mes-Año): "), "%d-%m-%Y")
        fv = datetime.strptime(input("Ingrese la fecha de vencimiento del proyecto (Dia-Mes-Año): "), "%d-%m-%Y")
        
    estado = input("El estado de tarea: ")
    avance = int(input("El avance de tarea: "))
    return ide,nombre,empresa_cliente,descripcion,fi,fv,estado,avance

def Ingresar_subtarea ():
    ide = int(input("Id de proyecto: "))
    nombre = input("El nombre de Subtarea: ")
    descripcion = input("La descripcion de subtarea: ")
    estado_actual = input("El estado actual de proyecto: ")
    return ide,nombre,descripcion,estado_actual

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


class proyecto_pila:
    def __init__(self):
        self.cabeza = None

    def agreagar_proyecto(self):
        proyectitos = Cargar.cargar_datos_desde_json("config.txt")
        gestion_proyecto = Gestion_de_proyecto()  # Crear instancia de Gestion_de_proyecto
        proyecto = gestion_proyecto.buscar_proyectos() 
        band = input("¿Desear agregar Tarea? Si-> s No -> n: ")
        band_yn = 1 #Para que el usuario ingresa bien la opcion
        aux_tarea = []
        if band=="s":
            agregar_tarea(band,band_yn,aux_tarea,proyecto)
        else:
            pass
        
        lista_proyecto = proyecto
        if self.cabeza == None:
            self.cabeza = lista_proyecto
        else:
            lista_proyecto.siguiente = self.cabeza
            self.cabeza = lista_proyecto
    
    def mostrar_ALL_proyectos (self):
        inicial = self.cabeza
        if inicial != None:
            while inicial:
                
                print("Tareas del proyecto: ")
                for i in range(len(inicial.tareas)):
                    print('------')
                    print('ID: {:<10}'.format(inicial.tareas[i].id))
                    print('Nombre: {:<15}'.format(inicial.tareas[i].nombre))
                    print('Empresa: {:<15}'.format(inicial.tareas[i].empresa))

                    print('Descripcion: {:<15}'.format(inicial.tareas[i].descripcion))
                    print('Inicio: {:<15}'.format(inicial.tareas[i].inicio.strftime("%d-%m-%Y")))
                    print('Vencimiento: {:<15}'.format(inicial.tareas[i].vencimiento.strftime("%d-%m-%Y")))
                    print('Estado: {:<15}'.format(inicial.tareas[i].estado))
                    print('Porcentaje: {:<10}'.format(inicial.tareas[i].porcentaje))
                    print('------')
                inicial = inicial.siguiente

        else:
            print("Vacio")
    
    def eliminar_archivo(self):
        if not self.cabeza:
            return None
        else:
            borrado = self.cabeza
            self.cabeza = self.cabeza.siguiente
            return borrado
    
class Menu_Principal:
    
    def __init__(self):
        self.menu()
    
    def menu(self):
        #Construimos un menu para que el usuario elija la accion a realizar
        print("--------------------")
        print("Sistema avanzado de gestion ")
        print("Elija la operacion a realizar:")
        print("1.- Gestion de Proyectos. ")
        print("2.- Gestion de Tareas. ")
        print("3.- Reportes.")
        print()
        self.opcion=str(input("Elija su opcion: "))
        if self.opcion=="1":
            gestion=Gestion_de_proyecto()
            gestion.menu()
        elif self.opcion=="2":
                papa = proyecto_pila()
                papa.agreagar_proyecto()
                papa.mostrar_ALL_proyectos()
        elif self.opcion=="3":
            reporte=mr.Reporte()
                    
        print()
        print("----------")
        print("Desea seguir con el sistema de gestion?: ")
        print("1.- Si\n2.-No")
        seguir=(input(">. "))
              
        if seguir=="1":
            print("")
            self.menu()
        else: print("\nPrograma Finalizado.")
        
hola=Menu_Principal()
        
