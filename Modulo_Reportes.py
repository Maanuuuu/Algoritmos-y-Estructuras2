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
                self.consult_tarea_est(self.proyectitos)
            elif opcion == 2:
                self.filtrado_fechas(self.proyectitos)
            elif opcion == 3:
                self.filtrado_proyectos(self.proyectitos)
            elif opcion == 4:
                self.listar_sub_tareas(self.proyectitos)
            elif opcion == 5:
                break
            else:
                print("Opcion invalida")

    def consult_tarea_est(self,proyectitos):
        est=input("Indica el estado de la tarea: ")
        for proyecto in self.proyectitos:
            for tarea in proyecto.tareas:
                pass
                
        

    def filtrado_fechas(self,proyectitos):
        pass

    def filtrado_proyectos(self,proyectitos):
        pass

    def listar_sub_tareas(self,proyectitos):
        pass
