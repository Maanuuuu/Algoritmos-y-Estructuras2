from Modulo1 import *
from datetime import datetime
from ArbolAVL import *
from Gestion_tarea_prioridad import *
from Modulo5 import *

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




def menu_principal():
    gestor_empresas = GestorEmpresas()
    while True:
        print("\nSistema Avanzado de Gestion de Proyectos y Tareas")
        print("Elija su opcion:")
        print("1. Gestion de Empresas")
        print("2. Gestion de Proyectos")
        print("3. Gestion de Tareas y Prioridades")
        print("4. Gestion de Sprints")
        print("5. Gestion de Reportes")

        print("5. Salir")
        opcion = input(">. ")

        if opcion == '1':
            menu_gestor_empresas(gestor_empresas)
        elif opcion == '2':
            gestion_proyectos(gestor_empresas)
        elif opcion == '3':
            menu3()
        elif opcion == '4':
            menu4()
        elif opcion =="5":
            menu5()

        else:
            print("Opcion Invalida.")

# Menú para gestión de empresas
def menu_gestor_empresas(gestor_empresas):
    while True:
        print("\nMenu de Gestión de Empresas")
        print("1. Listar Empresas")
        print("2. Agregar Empresa")
        print("3. Modificar Empresa")
        print("4. Eliminar Empresa")
        print("5. Listar Proyectos de una Empresa")
        print("6. Agregar Proyecto a una Empresa")
        print("7. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            gestor_empresas.listar_empresas()
        elif opcion == '2':
            agregar_empresa(gestor_empresas)
        elif opcion == '3':
            modificar_empresa(gestor_empresas)
        elif opcion == '4':
            eliminar_empresa(gestor_empresas)
        elif opcion == '5':
            listar_proyectos_empresa(gestor_empresas)
        elif opcion == '6':
            agregar_proyecto_empresa(gestor_empresas)
        elif opcion == '7':
            break
        else:
            print("Opción no válida. Intente de nuevo.")


from datetime import datetime

def es_fecha_valida(fecha):
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def es_correo_valido(correo):
    partes = correo.split('@')
    if len(partes) == 2 and '.' in partes[1]:
        return True
    return False

def es_telefono_valido(telefono):
    if telefono.isdigit() or (telefono.count('-') == 1 and all(part.isdigit() for part in telefono.split('-'))):
        return True
    return False

def agregar_empresa(gestor_empresas):
    try:
        while True:
            id_empresa = input("Ingresa el id de la empresa: ")
            if id_empresa.isdigit():
                id_empresa = int(id_empresa)
                break
            else:
                print("El ID debe ser un número. Inténtalo de nuevo.")
        
        nombre = input("Ingresar el nombre de la empresa: ")
        
        descripcion = input("Descripcion de la empresa: ")
        
        while True:
            fecha_creacion = input("Ingresa la fecha de creación (YYYY-MM-DD): ")
            if es_fecha_valida(fecha_creacion):
                break
            else:
                print("La fecha no es válida. Inténtalo de nuevo.")

        direccion = input("Ingrese la direccion de la empresa: ")
        
        while True:
            telefono = input("Ingrese el numero de telefono de la empresa: ")
            if es_telefono_valido(telefono):
                break
            else:
                print("El número de teléfono no es válido. Inténtalo de nuevo.")
        
        while True:
            correo = input("Ingrese el correo de la empresa: ")
            if es_correo_valido(correo):
                break
            else:
                print("El correo electrónico no es válido. Inténtalo de nuevo.")
        
        gerente = input("Ingrese el gerente de la empresa: ")
        
        equipo_contacto = input("Ingrese el equipo de contacto de la empresa: ")

        gestor_empresas.crear_empresa(id_empresa, nombre, descripcion, fecha_creacion, direccion, telefono, correo, gerente, equipo_contacto)
        print("Empresa agregada con éxito.")
    except Exception as e:
        print(f"Ocurrió un error al agregar una empresa: {e}")

def modificar_empresa(gestor_empresas):
    id_empresa = input("Ingrese el ID de la empresa a modificar: ")
    empresa = gestor_empresas.buscar_empresa(id_empresa)
    if empresa:
        print("Deje en blanco los campos que no desea modificar.")
        nombre = input(f"Nuevo nombre ({empresa.nombre}): ") or empresa.nombre
        descripcion = input(f"Nueva descripción ({empresa.descripcion}): ") or empresa.descripcion
        direccion = input(f"Nueva dirección ({empresa.direccion}): ") or empresa.direccion
        telefono = input(f"Nuevo teléfono ({empresa.telefono}): ") or empresa.telefono
        correo = input(f"Nuevo correo ({empresa.correo}): ") or empresa.correo
        gerente = input(f"Nuevo gerente ({empresa.gerente}): ") or empresa.gerente
        equipo_contacto = input(f"Nuevo equipo de contacto ({empresa.equipo_contacto}): ") or empresa.equipo_contacto

        if gestor_empresas.modificar_empresa(id_empresa, nombre=nombre, descripcion=descripcion, direccion=direccion, telefono=telefono, correo=correo, gerente=gerente, equipo_contacto=equipo_contacto):
            print("Empresa modificada con éxito.")
        else:
            print("No se pudo modificar la empresa.")
    else:
        print("Empresa no encontrada.")

def eliminar_empresa(gestor_empresas):
    id_empresa = input("Ingrese el ID de la empresa a eliminar: ")
    if gestor_empresas.eliminar_empresa(id_empresa):
        print("Empresa eliminada con éxito.")
    else:
        print("No se pudo eliminar la empresa. Verifique el ID.")

def listar_proyectos_empresa(gestor_empresas):
    id_empresa = input("Ingrese el ID de la empresa para listar sus proyectos: ")
    print()
    if gestor_empresas.listar_proyectos(id_empresa):
        print("Listado de proyectos completado.")
    else:
        print("No se encontró la empresa o no tiene proyectos.")

def agregar_proyecto_empresa(gestor_empresas):
    id_empresa = input("Ingrese el ID de la empresa a la que desea agregar un proyecto: ")
    id_proyecto = input("Ingrese el ID del proyecto: ")
    nombre_proyecto = input("Ingrese el nombre del proyecto: ")
    descripcion_proyecto = input("Ingrese la descripción del proyecto: ")
    fecha_inicio = Identificar_fi()
    fecha_vencimiento = Identificar_fv()
    estado_actual = input("Ingrese el estado actual del proyecto: ")
    empresa=input("Ingrese la empresa del proyecto: ")
    gerente = input("Ingrese el nombre del gerente del proyecto: ")
    equipo = input("Ingrese los miembros del equipo (separados por comas): ").split(',')

    if gestor_empresas.agregar_proyecto(id_empresa, id_proyecto, nombre_proyecto, descripcion_proyecto, fecha_inicio, fecha_vencimiento, estado_actual,empresa, gerente, equipo):
        print("Proyecto agregado con éxito.")
    else:
        print("No se pudo agregar el proyecto. Verifique el ID de la empresa.")

def gestion_proyectos(gestor_empresas):
    while True:
        print("\nMenu de Gestión de Proyectos")
        print("1. Listar Proyectos")
        print("2. Agregar Proyecto")
        print("3. Modificar Proyecto")
        print("4. Eliminar Proyecto")
        print("5. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id_empresa = input("Ingrese el ID de la empresa: ")

            gestor_empresas.listar_proyectos(id_empresa)
        elif opcion == '2':
            agregar_proyecto(gestor_empresas)
        elif opcion == '3':
            modificar_proyecto(gestor_empresas)
        elif opcion == '4':
            eliminar_proyecto(gestor_empresas)
        elif opcion == '6':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def agregar_proyecto(gestor_empresas):
    id_empresa = input("Ingrese el ID de la empresa: ")
    id = input("Ingrese el ID del proyecto: ")
    nombre = input("Ingrese el nombre del proyecto: ")
    descripcion = input("Ingrese la descripción del proyecto: ")
    fecha_inicio = Identificar_fi()
    fecha_vencimiento = Identificar_fv()
    estado_actual = input("Ingrese el estado actual del proyecto: ")
    empresa=input("Ingrese la empresa del proyecto: ")
    gerente = input("Ingrese el nombre del gerente del proyecto: ")
    equipo = input("Ingrese los miembros del equipo (separados por comas): ").split(',')

    if gestor_empresas.agregar_proyecto(id_empresa, id, nombre, descripcion, fecha_inicio, fecha_vencimiento, estado_actual,empresa, gerente, equipo):
        print("Proyecto agregado con éxito.")
    else:
        print("No se pudo agregar el proyecto. Verifique el ID de la empresa.")

def modificar_proyecto(gestor_empresas):
    id = input("Ingrese el ID del proyecto a modificar: ")
    # Implementar la lógica para modificar el proyecto

def eliminar_proyecto(gestor_empresas):
    id = input("Ingrese el ID del proyecto a eliminar: ")
    if gestor_empresas.gestion_proyectos.eliminar_proyecto(id):
        print("Proyecto eliminado con éxito.")
    else:
        print("No se pudo eliminar el proyecto. Verifique el ID.")

def buscar_proyectos(gestor_empresas):
    criterio = input("Ingrese el criterio de búsqueda (id, nombre, gerente, fecha_inicio, fecha_vencimiento, estado_actual): ")
    valor = input("Ingrese el valor a buscar: ")
    proyectos = gestor_empresas.gestion_proyectos.buscar_proyectos(criterio, valor)
    for proyecto in proyectos:
        print(proyecto)

# Ejemplo de uso del menú principal
if __name__ == "__main__":
    menu_principal()


