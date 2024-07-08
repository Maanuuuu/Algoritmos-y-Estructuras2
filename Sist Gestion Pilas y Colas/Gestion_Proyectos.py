from datetime import datetime
import json
import datos_abstracto as da

""" 
    Parcial IV Listas Enlazadas, Pilas y Colas.
    Seccion: 305C1
    
    Manuel Nava  30.822.007  @Maanuuuu
    Juan Wu      30.391.117  @juanww20    
    Jose Farrautto  30.696.288 @farreto06

"""


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

    def __init__(self,id,nombre,empresa,descripcion,inicio,vencimiento,estado,porcentaje="",subtareaaaa=[]):
        self.id=id
        self.nombre=nombre
        self.empresa=empresa
        self.descripcion=descripcion
        self.inicio=inicio
        self.vencimiento=vencimiento
        self.estado=estado
  
        self.porcentaje=porcentaje
        self.subtareas=subtareaaaa
        self.siguiente=None


    def agregar_subtarea(self,subtarea):
        self.subtareas.append(subtarea)

    def mostrar_tarea(self):
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

    
    def escribir_datos_txt(self,nombre_archivo,proyectos):
        with open(nombre_archivo,"w") as archivito:
            for proyecto in proyectos:
                archivito.write(f"ID Proyecto: {proyecto.id}, Nombre: {proyecto.nombre}, Descripcion: {proyecto.descripcion}, Empresa: {proyecto.empresa}, Gerente: {proyecto.gerente}\n")
                for tarea in proyecto.tareas:
                    archivito.write(f"      ID Tarea: {tarea.id}, Nombre: {tarea.nombre}, Empresa: {proyecto.empresa}, Estado: {proyecto.estado}\n")
                


    
    


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

#Validacion de id:
def Identificar_id ():
        id=str(input("ID: "))
        band = 0
        while band == 0:
            if id.isdigit():
                band = 1
            else:
                print("Error por mal escrito el ID, ¡debe escribir numero!")
                id=str(input("ID: "))
        return id

def Identificar_fi ():
    try:
        fi= datetime.strptime(input("Ingrese la fecha de inicio del proyecto (Dia-Mes-Año): "), "%d-%m-%Y")
    except :
        print("Ingrese bien las fechas en formato Dia-Mes-Año")
        fi= datetime.strptime(input("Ingrese la fecha de inicio del proyecto (Dia-Mes-Año): "), "%d-%m-%Y")
    return fi

def Identificar_fv ():
    try:
        fv = datetime.strptime(input("Ingrese la fecha de vencimiento del proyecto (Dia-Mes-Año): "), "%d-%m-%Y")
    except :
        print("Ingrese bien las fechas en formato Dia-Mes-Año")
        fv = datetime.strptime(input("Ingrese la fecha de vencimiento del proyecto (Dia-Mes-Año): "), "%d-%m-%Y")
    return fv

#Definimos nuestra funcion principal para gestionar los proyectos
class Gestion_de_proyecto:
    def __init__(self,proyectos):
        self.proyectitos=proyectos
        
        
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
        bandera_opcion_sub = 0
        while bandera_opcion_sub == 0:
            if seguir == "1":
                bandera_opcion_sub = 1
                print("")
                self.menu()
            elif seguir == "2":
                bandera_opcion_sub = 1
                print("\nGestion de Proyectos Finalizado.")
            else:
                print("Por favor, escribir bien el numero de opcion")
                seguir = (input(">. "))
                #print("\nGestion de Proyectos Finalizado.")
    
        return self.proyectitos
            
    #inicio = datetime.strptime(input("Ingrese la fecha de inicio del proyecto (Dia-Mes-Año): "), "%d-%m-%Y")            
    def crear(self,proyectitos):
        print("Ingrese las especificaciones del proyecto: ")
        new_proyecto=Proyecto(

                id=Identificar_id(),
                nombre=str(input("Nombre: ")),
                descripcion=str(input("Descripcion: ")),
                inicio = Identificar_fi(),
                vencimiento = Identificar_fv(),
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
            nombre_id = Identificar_id()
            proyecto.id=nombre_id
            proyecto.nombre=str(input("Nombre: "))
            proyecto.descripcion=str(input("Descripcion: "))
            fi = Identificar_fi()
            proyecto.inicio = fi
            fv = Identificar_fv()
            proyecto.vencimiento = fv
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



#Generar clase Cola para almacenar
class Cola_Al:
    def __init__(self):
        self.cabeza = None
        self.cola = None
    
    def agregar_archivo(self, ide,nombre,cliente,descripcion,fi,fv,estado,avance,subtarea):
        Entarea = Tarea(ide,nombre,cliente,descripcion,fi,fv,estado,avance,subtarea)
        if not self.cabeza:
            self.cabeza = Entarea
            self.cola = Entarea
        else:
            self.cola.siguiente = Entarea
            self.cola = Entarea




def agregar_tarea(band,band_yn,aux_tarea,proyecto):
    Lista_cola = Cola_Al() #Esto es para crear la class "cola" para almacenar
    bandera_cola = 1
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
                bandera_subtarea = input("¿Desear agregar Subtarea? Si-> s No -> n: ")
                bandyn = 1
                aux_subtarea = []
                Montar_subtarea(bandera_subtarea,bandyn,aux_subtarea)
                #tareanuevo = Tarea(tareaid,tareanombre,tareaempresa_cliente,tareadescripcion,tareafi,tareafv,tareaestado,tareaavance)
                Lista_cola.agregar_archivo(tareaid,tareanombre,tareaempresa_cliente,tareadescripcion,tareafi,tareafv,tareaestado,tareaavance,aux_subtarea)
            inicial = Lista_cola.cabeza
            #print(tareanuevo.descripcion)
            if inicial != None:
                while inicial:
                    idd = inicial.id
                    nombree = inicial.nombre
                    empresaa = inicial.empresa
                    descripcionn = inicial.descripcion
                    inicioo = inicial.inicio
                    vencimientoo = inicial.vencimiento
                    estadoo = inicial.estado
                    porcentajee = inicial.porcentaje
                    aux_acomodando = Tarea(idd,nombree,empresaa,descripcionn,inicioo,vencimientoo,estadoo,porcentajee)
                    aux_tarea.append(aux_acomodando)
                    proyecto.tareas.append(aux_acomodando)
                    inicial = inicial.siguiente
            band_yn = 0
        elif band.lower() == "n":
            print("No ha agregado nada tarea")
            band_yn = 0
        else:
            print("No esta ingresado la opcion indicado, por favor ingresar de de nuevo")
            band = input("¿Desear agregar Tarea? Si-> s No -> n: ")
    

def Ingresar_tarea():
    ide = input("El id de tarea: ")
    baka = 0
    while baka == 0:
        if ide.isdigit():
            baka = 1
        else:
            print("Usted no ha ingresado de manera correcta, por favor ingresar de nuevo")
            ide = input("El id de tarea: ")
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
    def __init__(self,proyectos):
        self.cabeza = None
        self.proyectitos=proyectos

    def menu(self):
        #Construimos un menu para que el usuario elija la accion a realizar
        print("--------------------")
        print("Gestion de Tareas ")
        print("Elija la operacion a realizar:")
        print("1.- Agregar Tareas a Proyecto ")
        #print("2.- Mostrar Tareas del Proyecto ")
        print()
        self.opcion=str(input("Elija su opcion: "))
        bandera_opcion = 1
        while bandera_opcion == 1:
            if self.opcion=="1":
                self.agreagar_proyecto()
                self.mostrar_ALL_proyectos()
                bandera_opcion = 0
            else:
                print()
                print("¡Por favor escribir bien la opcion!")
                self.opcion=str(input("Elija su opcion: "))
                


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
   

    def agreagar_proyecto(self):
        proyecto=self.buscar_proyectos()
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



class Reporte:
    def __init__(self,proyectitos):
        self.proyectitos=proyectitos
        

    def menu_reporte(self):
        band=True
        while band==True:
            print("-------------------------------")
            print("Menu del modulo de reportes")
            print("Elija la operacion a realizar:")
            print("1.- Consultar tarea por estado.")
            print("2.- Filtrado por fechas.")
            print("3.- Filtrado de proyectos.")
            print("4.- Listar subtareas.")
            print("5.- Salir")
            opcion = int(input("Ingrese la opcion: "))
            if opcion == 1:
                self.consult_tarea_est(self.proyectitos)
            elif opcion == 2:
                self.filtrado_fechas(self.proyectitos)
            elif opcion == 3:
                self.filtrado_proyectos(self.proyectitos)
            elif opcion == 4:
                self.listar_sub_tareas(self.proyectitos)
            elif opcion == 5:
                band=False

            else:
                print("Opcion invalida")

    def consult_tarea_est(self,proyectitos):
        list_estados=[]
        list_pilas=[]
        cont=0
        dicc_estados={}
        for proyecto in self.proyectitos:
            for tarea in proyecto.tareas:
                if tarea.estado in list_estados:
                    pos=dicc_estados[tarea.estado]
                    list_pilas[pos].agregar_tarea(tarea)

                else:
                    list_estados.append(tarea.estado)
                    list_pilas.append(Pila_Tareas())
                    list_pilas[cont].agregar_tarea(tarea)
                    dicc_estados[tarea.estado]=cont
                    cont+=1
                
        for i in range(len(list_pilas)):
            print("-------------------------------------------------")
            print("Tareas con estado: ",list_estados[i])
            print(list_pilas[i].mostrar_pila_tareas())

    def filtrado_fechas(self,proyectitos):
        def menu_tip_fecha():
            print("-------------------------------")
            print("Filtrado por fechas")
            print("Ingrese con que fecha se va a filtar: ")
            print("1.- Fecha de inicio.")
            print("2.- Fecha de vencimiento.")
            return input("Ingrese la opcion: ")
        
        def menu_filtrado():
            print("-------------------------------")
            print("Filtrado por fechas")
            print("Ingrese el tipo de filtrado: ")
            print("1.- Rango de fechas.")
            print("2.- Antes de la fecha.")
            print("3.- Despues de la fecha.")
            return input("Ingrese la opcion: ")
        
        def pedir_fecha():
            return datetime.strptime(input("Ingrese la fecha en formato dd-mm-aaaa: "),"%d-%m-%Y")

        def rango():
            fecha1=pedir_fecha()
            fecha2=pedir_fecha()
            return fecha1,fecha2

        def filtrado_rango(fecha1,fecha2,criterio):
            pila=Pila_Tareas()
            for proyecto in self.proyectitos:
                for tarea in proyecto.tareas:
                    if criterio=="inicio":
                        if tarea.inicio>=fecha1 and tarea.inicio<=fecha2:
                            pila.agregar_tarea(tarea)

                    else:
                        if tarea.vencimiento>=fecha1 and tarea.vencimiento<=fecha2:
                            pila.agregar_tarea(tarea)
            print("---------------------------------")
            print("Tareas en rango de fechas: ")
            print(pila.mostrar_pila_tareas())

        def filtrado_antes(fecha,criterio):
            pila=Pila_Tareas()
            for proyecto in self.proyectitos:
                for tarea in proyecto.tareas:
                    if criterio=="inicio":
                        if tarea.inicio<fecha:
                            pila.agregar_tarea(tarea)
                    else:
                        if tarea.vencimiento<fecha:
                            pila.agregar_tarea(tarea)
            print("---------------------------------")
            print("Tareas con la fecha antes:")
            print(pila.mostrar_pila_tareas())

        def filtrado_despues(fecha,criterio):
            pila=Pila_Tareas()
            for proyecto in self.proyectitos:
                for tarea in proyecto.tareas:
                    if criterio=="inicio":
                        if tarea.inicio>fecha:
                            pila.agregar_tarea(tarea)
                    else:
                        if tarea.vencimiento>fecha:
                            pila.agregar_tarea(tarea)
            print("---------------------------------")
            print("Tareas con la fecha despues:")
            print(pila.mostrar_pila_tareas())
        
        def main():
            mtf=menu_tip_fecha()
            if mtf=="1":
                criterio="inicio"
            elif mtf=="2":
                criterio="vencimiento"
            else:
                print("Opcion invalida")
                main()
            
            mf=menu_filtrado()
            if mf=="1":
                fecha1,fecha2=rango()
                filtrado_rango(fecha1,fecha2,criterio)
            elif mf=="2":
                fecha=pedir_fecha()
                filtrado_antes(fecha,criterio)
            elif mf=="3":
                fecha=pedir_fecha()
                filtrado_despues(fecha,criterio)
            else:
                print("Opcion invalida")
        main()


    def filtrado_proyectos(self,proyectitos):
        pass

    def listar_sub_tareas(self,proyectitos):
        pass




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




class Menu_Principal:
    
    def __init__(self):
        self.proyectos=Cargar.cargar_datos_desde_json("config.txt")
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
 
        bandera_menu_opcion = 1
        while bandera_menu_opcion == 1:
            if self.opcion=="1":
                bandera_menu_opcion = 0
                gestion=Gestion_de_proyecto(self.proyectos)
                self.proyectos=gestion.menu()
                
            elif self.opcion=="2":
                bandera_menu_opcion = 0
                papa = proyecto_pila(self.proyectos)
                papa.menu()

            elif self.opcion=="3":
                bandera_menu_opcion = 0
                reporte=Reporte(self.proyectos)
                
                reporte.menu_reporte()
                    
            else:
                print("Usted no ha seleccionado bien la opcion, por favor ingresar de nuevo")
                self.opcion=str(input("Elija su opcion: "))
            
        
        Cargar_datos=Cargar()
        Cargar_datos.escribir_datos_txt("datos_actualizados.txt",self.proyectos)
        print()
        print("----------")
        print("Desea seguir con el sistema de gestion?: ")
        print("1.- Si\n2.- No")
        seguir=(input(">. "))
        bandera_confirmacion=1
        while bandera_confirmacion == 1:      
            if seguir=="1":
                bandera_confirmacion = 0
                print("")
                self.menu()
                Cargar_datos=Cargar()
                Cargar_datos.escribir_datos_txt("datos_actualizados.txt",self.proyectos)
            elif seguir == "2":
                bandera_confirmacion = 0
                Cargar_datos=Cargar()
                Cargar_datos.escribir_datos_txt("datos_actualizados.txt",self.proyectos)
                print("\nPrograma Finalizado.")
                bandera_menu_opcion=0
                break
            else:
                print("Por favor, escribir bien el numero de opcion")
                seguir=(input(">. "))
        
hola=Menu_Principal()
        
