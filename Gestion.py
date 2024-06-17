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
    print("1.- ID: ")
    print("2.- Nombre: ")
    print("3.- Empresa: ")
    print("4.- Gerente: ")
    print("5.- Equipo: ")
    criterio=str(input("Ingrese opcion: "))

    if criterio=="1":
        id = str(input("Introduzca id del proyecto: "))
        filtrado=[proyecto for proyecto in proyectos if id.lower() in proyecto.id.lower()]
        if filtrado==[]:
            print("No existen proyectos con ese id")
        else:
            for proyecto in filtrado:
                print(f'{proyecto.id} {proyecto.nombre}')
        
    elif criterio=="2":
        nombre = str(input("Introduzca el nombre del proyecto: "))
        filtrado=[proyecto for proyecto in proyectos if nombre.lower() in proyecto.nombre.lower()]
        if filtrado==[]:
            print("No existen proyectos con ese nombre")
        else:
            for proyecto in filtrado:
                print(f'{proyecto.id} {proyecto.nombre}')
        
    elif criterio=="3":
        empresa = str(input("Introduzca la empresa del proyecto: "))
        filtrado=[proyecto for proyecto in proyectos if empresa.lower() in proyecto.empresa.lower()]
        if filtrado==[]:
            print("No existen proyectos de esa empresa")
        else:
            for proyecto in filtrado:
                print(f'{proyecto.id} {proyecto.nombre} {proyecto.empresa}')

    elif criterio=="4":
        gerente = str(input("Introduzca nombre del gerente del proyecto: "))
        filtrado=[proyecto for proyecto in proyectos if gerente.lower() in proyecto.gerente.lower()]
        if filtrado==[]:
            print("No existen proyectos administrados por ese gerente")
        else:
            for proyecto in filtrado:
                print(f'{proyecto.id} {proyecto.nombre} {proyecto.gerente}')

    elif criterio=="5":
        equipo = str(input("Introduzca nombre del equipo del proyecto: "))
        filtrado=[proyecto for proyecto in proyectos if equipo.lower() in proyecto.equipo.lower()]
        if filtrado==[]:
            print("No existen proyectos designados a ese equipo")
        else:
            for proyecto in filtrado:
                print(f'{proyecto.id} {proyecto.nombre} {proyecto.equipo}')


    else:
        print("Opcion Invalida")

xd = Proyecto("01","Pro1 asas","compras",3,1,"nose","InteliX","Manue","Ventas")
xd2 = Proyecto("02","Pro2 asasa","compras",3,1,"nose","CanTV","Santiago","Inventario")
xd3 = Proyecto("03","Pro2 asas","compras",3,1,"nose","CanTV","Jesu","Compras")
xd4 = Proyecto("04","Pro2 aaa" ,"compras",3,1,"nose","Lol","Manue","Compras")
proyectitos=[]
print(xd2.empresa)
proyectitos.append(xd)
proyectitos.append(xd2)
proyectitos.append(xd3)
proyectitos.append(xd4)
buscar_proyectos(proyectitos)