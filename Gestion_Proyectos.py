from datetime import datetime

class Proyecto:

    def __init__(self,id,nombre,descripcion,inicio,vencimiento,estado,empresa,gerente,equipo):
        self.id=id
        self.nombre=nombre
        self.descripcion=descripcion
        self.inicio=inicio
        self.vencimieno=vencimiento
        self.estado=estado
        self.empresa=empresa
        self.gerente=gerente
        self.equipo=equipo
        self.tareas=[]

    def agregar_tarea(self,tarea):
        self.tareas.append(tarea)


    def mostrar(self):
        print('------\nID: {:<10}\nNombre: {:<15}\nDescripcion: {:<15}\nEstado: {:<15}\nEmpresa: {:<15}\nEquipo: {:<10}\nGerente: {:<10}\n'.format(self.id, self.nombre, self.descripcion,self.estado,self.empresa, self.equipo, self.gerente))


class Tarea:

    def __init__(self,id,nombre,empresa,cliente,descripcion,inicio,vencimiento,estado,porcentaje):
        self.id=id
        self.nombre=nombre
        self.descripcion=descripcion
        self.inicio=inicio
        self.vencimieno=vencimiento
        self.estado=estado
        self.empresa=empresa
        self.cliente=cliente
        self.porcentaje=porcentaje
        self.subtareas=[]

    def agregar_subtarea(self,subtarea):
        self.subtareas.append(subtarea)
        


def buscar_proyectos(proyectos):
    print("Buscar Proyecto por: ")
    
    print("1.- Nombre: ")
    print("2.- Empresa: ")
    print("3.- Gerente: ")
    print("4.- Equipo: ")
    criterio=str(input("Ingrese opcion: "))


    if criterio=="1":
        nombre = str(input("Introduzca el nombre del proyecto: "))
        filtrado=[proyecto for proyecto in proyectos if nombre.lower() in proyecto.nombre.lower()]
        if filtrado==[]:
            print("No existen proyectos con ese nombre")
        
    elif criterio=="2":
        empresa = str(input("Introduzca la empresa del proyecto: "))
        filtrado=[proyecto for proyecto in proyectos if empresa.lower() in proyecto.empresa.lower()]
        if filtrado==[]:
            print("No existen proyectos de esa empresa")


    elif criterio=="3":
        gerente = str(input("Introduzca nombre del gerente del proyecto: "))
        filtrado=[proyecto for proyecto in proyectos if gerente.lower() in proyecto.gerente.lower()]
        if filtrado==[]:
            print("No existen proyectos administrados por ese gerente")
        

    elif criterio=="4":
        equipo = str(input("Introduzca nombre del equipo del proyecto: "))
        filtrado=[proyecto for proyecto in proyectos if equipo.lower() in proyecto.equipo.lower()]
        if filtrado==[]:
            print("No existen proyectos administrados por ese equipo")
    

    
    else:
        print("Opcion Invalida")

    if filtrado!=[]:
        print("Proyectos encontrados: ")
        for proyecto in filtrado:
            print('ID: {:^10} / Nombre: {:^15}  /  Empresa: {:^15}  /  Equipo: {:^10}  /  Gerente: {:^10}'.format(proyecto.id, proyecto.nombre, proyecto.empresa, proyecto.equipo, proyecto.gerente))
        
        seleccion=str(input("\nSeleccione el ID del proyecto que desea operar: "))
        try:
            lista=[proyecto for proyecto in filtrado if seleccion.lower() in proyecto.id.lower()]
            proyecto_seleccionado=lista[0]
            

        except:
            print("ID invalido")
    return proyecto_seleccionado

def Gestion_proyecto():
    print("--------------------")
    print("Gestion del Proyecto ")
    print("Elija la operacion a realizar:")
    print("1.- Modificar. ")
    print("2.- Consultar. ")
    print("3.- Listar. ")
    print("4.- Eliminar. ")

    opcion=str(input("Ingrese opcion: "))
    print()
    

    if opcion=="1":
        proyecto=buscar_proyectos(proyectitos)
        print("Ingrese las modificaciones del proyecto: ")
        proyecto.id=str(input("ID: "))
        proyecto.nombre=str(input("Nombre: "))
        proyecto.descripcion=str(input("Descripcion: "))
        proyecto.inicio = datetime.strptime(input("Ingrese la fecha de inicio del proyecto (Dia-Mes-Año): "), "%d-%m-%Y")
        proyecto.vencimiento = datetime.strptime(input("Ingrese la fecha de vencimiento del proyecto (Dia-Mes-Año): "), "%d-%m-%Y")
        proyecto.estado=str(input("Estado actual: "))
        proyecto.empresa=str(input("Empresa: "))
        proyecto.gerente=str(input("Gerente: "))
        proyecto.equipo=str(input("Equipo: "))
    
    elif opcion=="2":
        proyecto=buscar_proyectos(proyectitos)
        print("Informacion del Proyecto:")
        proyecto.mostrar()

    elif opcion=="3":
        for proyecto in proyectitos:
            proyecto.mostrar()

    elif opcion=="4":
        proyecto=buscar_proyectos(proyectitos)
        option=str(input("Desea borrar el proyecto "+proyecto.nombre+"?: "))
        if option.lower()=="si":
            proyectitos.remove(proyecto)
            print("Proyecto Eliminado")
        else:
            print("Eliminacion cancelada")
        

    print("Desea seguir con la gestion de Proyectos?: ")
    print("1.- Si\n2.-No")
    seguir=(input(">. "))
    
    if seguir=="1":
        print("")
        Gestion_proyecto()
    else: pass
#id,nombre,descripcion,inicio,vencimiento,estado,empresa,gerente,equipo

xd = Proyecto("01","Pro1 asas","compras",3,1,"nose","InteliX","Manue","Ventas")
xd2 = Proyecto("02","Pro2 asasa","compras",3,1,"nose","CanTV","Santiago","Inventario")
xd3 = Proyecto("03","Pro2 asas","compras",3,1,"nose","CanTV","Jesu","Compras")
xd4 = Proyecto("04","Pro2 aaa" ,"compras",3,1,"nose","Lol","Manue","Compras")
proyectitos=[]

proyectitos.append(xd)
proyectitos.append(xd2)
proyectitos.append(xd3)
proyectitos.append(xd4)
Gestion_proyecto()