import Gestion_Proyectos as gp

class Reporte:
    def __init__(self):
        self.proyectitos=[]
        self.proyectitos=gp.Cargar.cargar_datos_desde_json("config.txt")
        self.menu(self.proyectitos)

    def menu(self,proyectitos):
        while True:
            print("1. Consultar tarea por estado: ")
            print("2. Filtrado por fechas: ")
            print("3. Filtrado de proyectos:")
            print("4. Listar subtareas: ")
            print("5. Salir")
            opcion = int(input("Ingrese la opcion: "))
            if opcion == 1:
                self.reporte_proyectos(proyectitos)
            elif opcion == 2:
                self.reporte_tareas(proyectitos)
            elif opcion == 3:
                self.reporte_subtareas(proyectitos)
            elif opcion == 4:
                self.reporte_subtareas(proyectitos)
            elif opcion == 5:
                break
            else:
                print("Opcion invalida")