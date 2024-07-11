from datetime import datetime
from ArbolProyectos import *

class Proyecto:
    def __init__(self, id, nombre, descripcion, fecha_inicio, fecha_vencimiento, estado_actual, empresa, gerente, equipo):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_vencimiento = fecha_vencimiento
        self.estado_actual = estado_actual
        self.empresa = empresa
        self.gerente = gerente
        self.equipo = equipo
        self.tiempo_restante = (self.fecha_vencimiento - datetime.now()).days

    def actualizar_tiempo_restante(self):
        self.tiempo_restante = (self.fecha_vencimiento - datetime.now()).days

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Descripción: {self.descripcion}, Fecha de inicio: {self.fecha_inicio.strftime('%Y-%m-%d')}, Fecha de vencimiento: {self.fecha_vencimiento.strftime('%Y-%m-%d')}, Estado actual: {self.estado_actual}, Empresa: {self.empresa}, Gerente: {self.gerente}, Equipo: {self.equipo}, Tiempo restante: {self.tiempo_restante} días"


class GestorProyectos:
    def __init__(self):
        self.arbol_proyectos = ArbolProyectos()

    def crear_proyecto(self, identificador, nombre, descripcion, fecha_inicio, fecha_vencimiento, estado, empresa, gerente, equipo):
        nuevo_proyecto = Proyecto(identificador, nombre, descripcion, fecha_inicio, fecha_vencimiento, estado, empresa, gerente, equipo)
        self.arbol_proyectos.insertar_proyecto(nuevo_proyecto)

    def buscar_proyectos(self, criterio, valor):
        return self.arbol_proyectos.buscar_proyecto(criterio, valor)

    def modificar_proyecto(self, identificador, **kwargs):
        proyectos_encontrados = self.buscar_proyectos('id', identificador)
        if proyectos_encontrados:
            proyecto = proyectos_encontrados[0]
            for key, value in kwargs.items():
                setattr(proyecto, key, value)
            proyecto.actualizar_tiempo_restante()
            return True
        return False

    def eliminar_proyecto(self, identificador):
        proyectos = self.listar_proyectos()
        self.arbol_proyectos = ArbolProyectos()
        for proyecto in proyectos:
            if proyecto.id != identificador:
                self.arbol_proyectos.insertar_proyecto(proyecto)
        return True

    def listar_proyectos(self):
        return self.arbol_proyectos.buscar_proyecto('id', '')  # Retorna todos los proyectos

    def actualizar_tiempos_restantes(self):
        self.arbol_proyectos.actualizar_tiempo_restante()

