import Gestion_Proyectos as gp
import datos_abstracto as da
from datetime import datetime

class Reporte:
    def __init__(self,proyectitos):
        self.proyectitos=proyectitos
        

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
                print("a")
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
            pila=da.Pila_Tareas()
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
            pila=da.Pila_Tareas()
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
            pila=da.Pila_Tareas()
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
