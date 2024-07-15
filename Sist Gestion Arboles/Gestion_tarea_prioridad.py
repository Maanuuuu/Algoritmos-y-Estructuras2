#Libreria
from datetime import datetime

#Creacion de class para los objetos

#Crear Tarea
class tarea:
    def __init__(self,ide,nombre,descripcion,inicio,vencimiento,estado,avance,objetivo_especifico):
        self.ide=ide
        self.nombre=nombre
        self.descripcion=descripcion
        self.inicio=inicio
        self.vencimiento=vencimiento
        self.estado=estado
        self.avance=avance
        self.objetivo_especifico = objetivo_especifico
        self.subtareas=[]

    def agregar_subtarea(self,subtarea):
        self.subtareas.append(subtarea)

    def __lt__(self, other):
        return self.ide < other.ide

    def __eq__(self, other):
        return self.ide == other.ide

    def __str__(self):
        return f"ID: {self.ide}, Nombre: {self.nombre}, Descripcion: {self.descripcion}, Fecha_inicio: {self.inicio}, Fecha_Vencimiento: {self.vencimiento}, Estado: {self.estado}, Avance: {self.avance}, Objetivo Especifico: {self.objetivo_especifico}\n"

    def __repr__(self):
        return str(self)

#Crear Subtarea
class Subtarea:
    def __init__(self, ide, nombre, empresa_cliente, fi, fv, descripcion, estado, porcentaje):
        self.ide = ide
        self.nombre = nombre
        self.empresa_cliente = empresa_cliente
        self.fi = fi
        self.fv = fv
        self.descripcion = descripcion
        self.estado = estado
        self.porcentaje = porcentaje

#-------------------------------------------------------------Separacion-------------------------------------------------------------

#Metodo de N-Arios
class NTreeNode:
    def __init__(self, tarea=None):
        self.tarea = tarea
        self.children = []

    def insert(self, tarea):
        self.children.append(NTreeNode(tarea))

    def __str__(self):
        return str(self.tarea)


class NTree:
    def __init__(self):
        self.root = None

    def insert(self, tarea):
        if not self.root:
            self.root = NTreeNode(tarea)
        else:
            self._insert_recursive(self.root, tarea)

    def _insert_recursive(self, node, tarea):
        if not node.children:
            node.insert(tarea)
        else:
            for child in node.children:
                self._insert_recursive(child, tarea)

    def traverse(self):
        if self.root:
            self._traverse_recursive(self.root)

    def _traverse_recursive(self, node):
        print(node)
        for child in node.children:
            self._traverse_recursive(child)

    def inorden(self):
        if self.root:
            self._inorden_recursive(self.root)

    def _inorden_recursive(self, node):
        if node:
            for child in node.children:
                self._inorden_recursive(child)
            print(node)

    def preorden(self):
        if self.root:
            self._preorden_recursive(self.root)

    def _preorden_recursive(self, node):
        if node:
            print(node)
            for child in node.children:
                self._preorden_recursive(child)

    def postorden(self):
        if self.root:
            self._postorden_recursive(self.root)

    def _postorden_recursive(self, node):
        if node:
            for child in node.children:
                self._postorden_recursive(child)
            print(node)

#-------------------------------------------------------------Separacion-------------------------------------------------------------


#-------------------------------------------------------------Separacion-------------------------------------------------------------

#Funciones

#Validacion para num
def validacion_num (num):
    bandera_numeral = 0
    while bandera_numeral==0:
        if num.isdigit():
            bandera_numeral = 1
            num = int(num)
        else:
            print("")
            print("Ha ingresado los caracteres incorrectas, por favor ingresar de nuevo")
            num = input("Ingresar de nuevo: ")

#Validacion para fecha
def validacion_fecha_inicial(fechaa):
    while True:
        try:
            fechaa = datetime.strptime(input("Ingrese la fecha de inicio del proyecto (Dia-Mes-Año): "), "%d-%m-%Y")
            return fechaa.date()
            break  # Se sale del bucle si la fecha es válida
        except ValueError:
            print()
            print("Formato de fecha inválido. Intente nuevamente.")

def validacion_fecha_final(fechaa):
    while True:
        try:
            fechaa = datetime.strptime(input("Ingrese la fecha de final del proyecto (Dia-Mes-Año): "), "%d-%m-%Y")
            return fechaa.date()
            break  # Se sale del bucle si la fecha es válida
        except ValueError:
            print()
            print("Formato de fecha inválido. Intente nuevamente.")


def prohibido_espacio_blanco (texto):
    while True:
        texto = texto.strip()  # Elimina espacios en blanco al inicio y final
        
        if texto and not texto.isspace():  # Valida si no está vacío o solo espacios
            return texto
            break
        else:
            print()
            print("Esta dejando vacio el ingreso o haciendo un invalido ingreso, por favor, ingresa de nuevo")
            texto = input("Ingresar el dato anterior: ")

#Funcionalidad de otra
def consultar_id (lista_tareas,id_buscado):
    for i in lista_tareas:
        if i.ide == id_buscado:
            print(f"Tarea seleccionada: {i}")
            return
    print(f"No se encontró la tarea seleccionada con el ID {id_buscado}, puede que ser la tarea que no existe o ingreso mal id")

def eliminar_id(lista_tareas, id_buscado):
    for i, iii in enumerate(lista_tareas):
        if iii.ide == id_buscado:
            del lista_tareas[i]
            print(f"Tarea con ID {id_buscado} eliminada.")
            return
    print(f"No se encontró la tarea seleccionada con el ID {id_buscado}, puede que ser la tarea que no existe o ingreso mal id.")

def modificar_id(lista_tareas, id_buscado):
    for hm in lista_tareas:
        if hm.ide == id_buscado:
            print(f"Detalles de la tarea con ID {id_buscado}:")
            print(hm)

            print("\nIngresa los nuevos datos de la tarea:")
            
            n_nombree = input("Ingresar el nuevo nombre: ")
            prohibido_espacio_blanco(n_nombree)
            hm.nombre = n_nombree

            n_descripcionn = input("Ingresar la nueva descripcion: ")
            prohibido_espacio_blanco(n_descripcionn)
            hm.descripcion = n_descripcionn

            n_aux_fecha = ""
            n_fecha_inicio = validacion_fecha_inicial(n_aux_fecha)
            hm.inicio = n_fecha_inicio

            n_aux_fecha = ""
            n_fecha_final = validacion_fecha_final(n_aux_fecha)
            hm.vencimiento = n_fecha_final

            n_estadoo = input("Ingresar el nuevo estado: ")
            prohibido_espacio_blanco(n_estadoo)
            hm.estado = n_estadoo

            n_avancee = input("Ingresar la nueva avance: ")
            validacion_num(n_avancee)
            hm.avance = n_avancee
            
            n_objetivo_especificoo = input("Ingresar el nuevo objetivo especifico: ")
            prohibido_espacio_blanco(n_objetivo_especificoo)
            hm.objetivo_especifico = n_objetivo_especificoo

            print("\nTarea modificada:")
            print(hm)
            return
    print(f"No se encontró una tarea con el ID {id_buscado}.")

#-------------------------------------------------------------Separacion-------------------------------------------------------------

def menu3():
    n_tree = NTree()

    # Crear e insertar productos
    Lista_todas_tareas = [
        tarea(1, "Acheron", "Trabajando, y bien calidad", "01-06-2024", "03-06-2024", "Finalizando", 20, "Hacer bien las cosas"),
        tarea(2, "Manuel", "Trabajando, y bien calidad", "02-06-2024", "03-06-2024", "Finalizando", 30, "Hacer todas las cosas lo mas posible"),
        tarea(3, "Jose", "Trabajando, y bien bello", "08-06-2024", "12-06-2024", "En progreso", 30, "Averiguando todas las cosas lo mas posible"),
        tarea(4, "Venti", "Trabajando y disfrutando", "20-06-2024", "23-06-2024", "En progreso", 50, "Organizando las cosas lo mas posible"),
        tarea(5, "Kaeya", "Trabajando y organizando la cosa", "25-06-2024", "30-06-2024", "Culminando", 80, "Preparando las cosas"),
    ]

    for tareai in Lista_todas_tareas:
        n_tree.insert(tareai)

        #Menu Intentar
    bandera = 1
    while bandera == 1:
        print("")
        print("1. -> Agregar Tarea")
        print("2. -> Consultar tareas existentes")
        print("3. -> Modificar tarea")
        print("4. -> Listar tareas")
        print("5. -> Eliminar tarea")
        print()
        print("6. -> Salir la programa")
        pregunta = input("Elige la opcion: ")

        if pregunta == "1":
            idd = input("Ingresar el id: ")
            validacion_num(idd)
            idd = int(idd)

            nombree = input("Ingresar el nombre: ")
            prohibido_espacio_blanco(nombree)

            descripcionn = input("Ingresar la descripcion: ")
            prohibido_espacio_blanco(descripcionn)

            aux_fecha = ""
            fecha_inicio = validacion_fecha_inicial(aux_fecha)

            aux_fecha = ""
            fecha_final = validacion_fecha_final(aux_fecha)

            estadoo = input("Ingresar el estado: ")
            prohibido_espacio_blanco(estadoo)

            avancee = input("Ingresar la avance: ")
            validacion_num(avancee)

            objetivo_especificoo = input("Ingresar el objetivo especifico: ")
            prohibido_espacio_blanco(objetivo_especificoo)

            nueva_tarea = tarea(idd,nombree,descripcionn,fecha_inicio,fecha_final,estadoo,avancee,objetivo_especificoo)
            print("")
            print("Desea agregar subtarea para esta tarea?")
            print("1. si -> s")
            print("2. no -> n")
            pregunta_por_sub_tarea = input("Ingresar tu opcion: ")
            bandera_temporal_subtarea = 1
            while bandera_temporal_subtarea == 1:
                
                if pregunta_por_sub_tarea == "s":
                    sub_ide = input("Ingresar el id: ")
                    validacion_num(idd)
                    print(type(sub_ide))

                    sub_nombre = input("Ingresar el nombre: ")
                    prohibido_espacio_blanco(sub_nombre)

                    sub_empresa = input("Ingresar el nombre de empresa de cliente: ")
                    prohibido_espacio_blanco(sub_empresa)

                    sub_descripcion = input("Ingresar la descripcion: ")
                    prohibido_espacio_blanco(sub_descripcion)

                    aux_fecha = ""
                    sub_fecha_inicio = validacion_fecha_inicial(aux_fecha)

                    aux_fecha = ""
                    sub_fecha_final = validacion_fecha_final(aux_fecha)

                    sub_estado = input("Ingresar el estado: ")
                    prohibido_espacio_blanco(sub_estado)

                    sub_porcentaje = input("Ingresar el porcentaje: ")
                    validacion_num(sub_porcentaje)

                    nuevo_subtarea = Subtarea(sub_ide,sub_nombre,sub_empresa,sub_fecha_inicio,sub_fecha_final,sub_descripcion,sub_estado,sub_porcentaje)
                    nueva_tarea.agregar_subtarea(nuevo_subtarea)

                    bandera_temporal_subtarea = 0

                elif pregunta_por_sub_tarea == "n":
                    bandera_temporal_subtarea = 0
                    print("No ha agregado nada subtarea")
                else:
                    print()
                    print("No ha indica bien claro la opcion")
                    pregunta_por_sub_tarea = input("Ingresar tu opcion: ")
            
            Lista_todas_tareas.append(nueva_tarea)
            n_tree.insert(nueva_tarea)

        elif pregunta == "2": 
            
            print("1. -> Seleccionar por id especifico para consultar tarea")
            print("2. -> Consultar todas tareas existentes")
            pregunta_opcion_ver_tarea = input("Seleccionar su opcion: ")

            band_por_consultar = 1
            while band_por_consultar == 1:

                if pregunta_opcion_ver_tarea == "1":
                    id_selecion = input("El id: ")
                    validacion_num(id_selecion)
                    id_selecion = int(id_selecion)
                    consultar_id(Lista_todas_tareas,id_selecion)
                    band_por_consultar = 0
                
                elif pregunta_opcion_ver_tarea == "2":
                    band_temporal_visualizar_para_manera_ver = 1
                    print("1. -> Preorden")
                    print("2. -> Inorden")
                    print("3. -> Postorden")
                    manera_ver = input("Seleccionar de ver: ")
                    while band_temporal_visualizar_para_manera_ver == 1:
                        if manera_ver == "1":
                            print("")
                            print("Visualizacion por Forma de Preorden")
                            n_tree.preorden()
                            band_temporal_visualizar_para_manera_ver = 0
                        elif manera_ver == "2":
                            print("")
                            print("Visualizacion por Forma de Inorden")
                            n_tree.inorden()
                            band_temporal_visualizar_para_manera_ver = 0
                        elif manera_ver == "3":
                            print("")
                            print("Visualizacion por Forma de Postorden")
                            n_tree.postorden()
                            band_temporal_visualizar_para_manera_ver = 0
                        else:
                            print()
                            print("Ingreso mal opcion, por favor marcar de nuevo")
                            manera_ver = input("Seleccionar de ver: ")
                    
                    band_por_consultar = 0
                else:
                    print()
                    print("No se ha realizado bien la opcion")
                    pregunta_opcion_ver_tarea = input("Seleccionar su opcion: ")
        
        elif pregunta == "3":
            print("Aqui es la opcion de modificar el proyecto")
            print("Se borrar por el ID del tarea")
            print("¿Desea Eliminar alguno trabajo?")
            print("1. Si, por favor. -> s")
            print("2. No, por favor. -> n")
            bandera_para_modificar = 1
            opcion_modo_eliminar = input("Ingresar su opcion: ")
            while bandera_para_modificar == 1:
                if opcion_modo_eliminar == "s":
                    num_id = input("Ingresar su id de tarea: ")
                    num_id = int(num_id)
                    modificar_id(Lista_todas_tareas,num_id)
                    n_tree = NTree() 
                    for ii in Lista_todas_tareas:
                        n_tree.insert(ii)
                    print("¡Moficicado!")
                    bandera_para_modificar = 0
                elif opcion_modo_eliminar == "n":
                    print("No se ha modificado ningun tarea")
                    bandera_para_modificar = 0
                else:
                    print()
                    print("Usted ingreso un opcion invalida, por favor ingresar de nuevo")
                    opcion_modo_eliminar = input("Ingresar su opcion: ")

        elif pregunta == "4":
            print("Formas de listar tareas: ")
            band_temporal_visualizar_para_manera_ver = 1
            print("1. -> Preorden")
            print("2. -> Inorden")
            print("3. -> Postorden")
            manera_ver = input("Seleccionar de ver: ")
            while band_temporal_visualizar_para_manera_ver == 1:
                if manera_ver == "1":
                    print("")
                    print("Visualizacion por Forma de Preorden")
                    n_tree.preorden()
                    band_temporal_visualizar_para_manera_ver = 0
                elif manera_ver == "2":
                    print("")
                    print("Visualizacion por Forma de Inorden")
                    n_tree.inorden()
                    band_temporal_visualizar_para_manera_ver = 0
                elif manera_ver == "3":
                    print("")
                    print("Visualizacion por Forma de Postorden")
                    n_tree.postorden()
                    band_temporal_visualizar_para_manera_ver = 0
                else:
                    print()
                    print("Ingreso mal opcion, por favor marcar de nuevo")
                    manera_ver = input("Seleccionar de ver: ")
        elif pregunta == "5":
            print("Aqui se borra por id de la tarea")
            print("¿Esta seguro borrar algun tarea?")
            print("1. Si, por favor. -> s")
            print("2. No, por favor. -> n")
            bandera_para_eliminar = 1
            opcion_modo_eliminar = input("Ingresar su opcion: ")
            while bandera_para_eliminar == 1:
                if opcion_modo_eliminar == "s":
                    num_id = input("Ingresar su id de tarea: ")
                    num_id = int(num_id)
                    eliminar_id(Lista_todas_tareas,num_id)
                    n_tree = NTree() 
                    for ii in Lista_todas_tareas:
                        n_tree.insert(ii)
                    print("¡Eliminado!")
                    bandera_para_eliminar = 0
                elif opcion_modo_eliminar == "n":
                    print("No se ha eliminado ningun tarea")
                    bandera_para_eliminar = 0
                else:
                    print()
                    print("Usted ingreso un opcion invalida, por favor ingresar de nuevo")
                    opcion_modo_eliminar = input("Ingresar su opcion: ")

        elif pregunta == "6":
            bandera = 0
            print("Salir el modo de Gestión de Tareas y Prioridades")
        
        else:
            print()
            print("Ingresaste una opcion invalida, por favor marca bien la opcion")

menu3