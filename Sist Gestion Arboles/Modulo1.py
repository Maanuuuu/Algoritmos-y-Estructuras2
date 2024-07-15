from Modulo2 import *
import csv

class Nodo:
    def __init__(self, empresa):
        self.empresa = empresa
        self.siguiente = None



class Empresa:
    def __init__(self, id, nombre, descripcion, fecha_creacion, direccion, telefono, correo, gerente, equipo_contacto):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_creacion = fecha_creacion
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.gerente = gerente
        self.equipo_contacto = equipo_contacto
        self.proyectos = []

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Descripción: {self.descripcion}, Fecha de Creación: {self.fecha_creacion}, Dirección: {self.direccion}, Teléfono: {self.telefono}, Correo: {self.correo}, Gerente: {self.gerente}, Equipo de Contacto: {self.equipo_contacto}"


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_nodo(self, empresa):
        nuevo_nodo = Nodo(empresa)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo

    def eliminar_nodo(self, id):
        if not self.cabeza:
            return False
        if self.cabeza.empresa.id == id:
            self.cabeza = self.cabeza.siguiente
            return True
        nodo_actual = self.cabeza
        while nodo_actual.siguiente:
            if nodo_actual.siguiente.empresa.id == id:
                nodo_actual.siguiente = nodo_actual.siguiente.siguiente
                return True
            nodo_actual = nodo_actual.siguiente
        return False

    def buscar_nodo(self, id):
        nodo_actual = self.cabeza
        while nodo_actual:
            if nodo_actual.empresa.id == id:
                return nodo_actual.empresa
            nodo_actual = nodo_actual.siguiente
        return None

    def listar_nodos(self):
        lista_empresas = []
        nodo_actual = self.cabeza
        while nodo_actual:
            lista_empresas.append(nodo_actual.empresa)
            nodo_actual = nodo_actual.siguiente
        return lista_empresas


class GestorEmpresas:
    def __init__(self):
        self.archivo_csv = "Sist Gestion Arboles\empresasitas.csv"
        self.lista_empresas = ListaEnlazada()
        self.gestor_proyectos = GestorProyectos()
        self.cargar_empresas()

    def cargar_empresas(self):
        try:
            with open(self.archivo_csv, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for fila in reader:
                    empresa = Empresa(
                        fila['id'],
                        fila['nombre'],
                        fila['descripcion'],
                        fila['fecha_creacion'],
                        fila['direccion'],
                        fila['telefono'],
                        fila['correo'],
                        fila['gerente'],
                        fila['equipo_contacto']
                    )
                    self.lista_empresas.agregar_nodo(empresa)
        except FileNotFoundError:
            print(f"El archivo {self.archivo_csv} no se encontró. Se creará uno nuevo.")
    
    def guardar_empresas(self):
        with open(self.archivo_csv, 'w', newline='') as csvfile:
            fieldnames = ['id', 'nombre', 'descripcion', 'fecha_creacion', 'direccion', 'telefono', 'correo', 'gerente', 'equipo_contacto']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for empresa in self.lista_empresas.listar_nodos():
                writer.writerow({
                    'id': empresa.id,
                    'nombre': empresa.nombre,
                    'descripcion': empresa.descripcion,
                    'fecha_creacion': empresa.fecha_creacion,
                    'direccion': empresa.direccion,
                    'telefono': empresa.telefono,
                    'correo': empresa.correo,
                    'gerente': empresa.gerente,
                    'equipo_contacto': empresa.equipo_contacto
                })

    def crear_empresa(self, id, nombre, descripcion, fecha_creacion, direccion, telefono, correo, gerente, equipo_contacto):
        nueva_empresa = Empresa(id, nombre, descripcion, fecha_creacion, direccion, telefono, correo, gerente, equipo_contacto)
        self.lista_empresas.agregar_nodo(nueva_empresa)
        self.guardar_empresas()

    def listar_empresas(self):
        for empresa in self.lista_empresas.listar_nodos():
            print(empresa)
            print()

    def buscar_empresa(self, id_empresa):
        return self.lista_empresas.buscar_nodo(id_empresa)

    def modificar_empresa(self, id, **kwargs):
        empresa = self.buscar_empresa(id)
        if empresa:
            for key, value in kwargs.items():
                setattr(empresa, key, value)
            self.guardar_empresas()
            return True
        return False


    def eliminar_empresa(self, id):
        if self.lista_empresas.eliminar_nodo(id):
            self.guardar_empresas()
            return True
        return False

    def agregar_proyecto(self, id_empresa, id, nombre, descripcion, fecha_inicio, fecha_vencimiento, estado_actual, empresa, gerente, equipo):
        empresa = self.buscar_empresa(id_empresa)
        if empresa:
            proyecto = Proyecto(id, nombre, descripcion, fecha_inicio, fecha_vencimiento, estado_actual, empresa, gerente, equipo)
            empresa.proyectos.append(proyecto)
            self.guardar_empresas()  # Guardar cambios en el archivo
            return True
        return False

    def listar_proyectos(self, id_empresa):
        empresa = self.buscar_empresa(id_empresa)
        if empresa:
            if empresa.proyectos:
                print("Proyectos de la empresa:", empresa.nombre)
                for proyecto in empresa.proyectos:
                    print(f"ID: {proyecto.id}, Nombre: {proyecto.nombre}, Descripción: {proyecto.descripcion}, Fecha de inicio: {proyecto.fecha_inicio}, Fecha de vencimiento: {proyecto.fecha_vencimiento}, Estado actual: {proyecto.estado_actual}, Gerente: {proyecto.gerente}, Equipo: {', '.join(proyecto.equipo)}")
                return True
            else:
                print("La empresa no tiene proyectos.")
                return False
        else:
            print("No se encontró la empresa con el ID proporcionado.")
            return False