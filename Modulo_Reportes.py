import Gestion_Proyectos as gp
import datos_abstracto as da

class Reporte:
    def __init__(self):
        self.proyectitos=[]
        self.proyectitos=gp.Cargar.cargar_datos_desde_json("config.txt")
        self.menu(self.proyectitos)

    def menu(self,proyectitos):
        while True:
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
                break
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
                    list_pilas.append(da.Pila_Tareas())
                    list_pilas[cont].agregar_tarea(tarea)
                    dicc_estados[tarea.estado]=cont
                    cont+=1
                
        for i in range(len(list_pilas)):
            print("-------------------------------------------------")
            print("Tareas con estado: ",list_estados[i])
            print(list_pilas[i].mostrar_pila_tareas())

    def filtrado_fechas(self,proyectitos):
        pass

    def filtrado_proyectos(self,proyectitos):
        pass

    def listar_sub_tareas(self,proyectitos):
        pass
