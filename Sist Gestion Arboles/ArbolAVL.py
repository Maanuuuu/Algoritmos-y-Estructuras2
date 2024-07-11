from datetime import datetime

class Empresa_work:
    def __init__(self,id,nombre,nombre_descriptivo,fi,fv,estado,objetivo,equipo):
        self.id = id
        self.nombre = nombre
        self.nombre_descriptivo = nombre_descriptivo
        self.fi = fi
        self.fv = fv
        self.estado = estado
        self.objetivo = objetivo
        self.equipo = equipo
        self.list_tarea = []
        self.izquierda = None
        self.derecha = None
        self.altura = 1


class AVLFileSystem:
    def __init__(self):
        self.raiz = None

    def obtener_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def obtener_balance(self, nodo):
        if not nodo:
            return 0
        return self.obtener_altura(nodo.izquierda) - self.obtener_altura(nodo.derecha)

    def rotar_derecha(self, z):
        y = z.izquierda
        T3 = y.derecha

        y.derecha = z
        z.izquierda = T3

        z.altura = 1 + max(self.obtener_altura(z.izquierda), self.obtener_altura(z.derecha))
        y.altura = 1 + max(self.obtener_altura(y.izquierda), self.obtener_altura(y.derecha))

        return y

    def rotar_izquierda(self, z):
        y = z.derecha
        T2 = y.izquierda

        y.izquierda = z
        z.derecha = T2

        z.altura = 1 + max(self.obtener_altura(z.izquierda), self.obtener_altura(z.derecha))
        y.altura = 1 + max(self.obtener_altura(y.izquierda), self.obtener_altura(y.derecha))

        return y

    def insertar(self, nodo,id,nombre,nombre_descriptivo,fi,fv,estado,objetivo,equipo):
        if not nodo:
            return Empresa_work(id,nombre,nombre_descriptivo,fi,fv,estado,objetivo,equipo)

        if nombre < nodo.nombre:
            nodo.izquierda = self.insertar(nodo.izquierda, id,nombre,nombre_descriptivo,fi,fv,estado,objetivo,equipo)
        elif nombre > nodo.nombre:
            nodo.derecha = self.insertar(nodo.derecha, id,nombre,nombre_descriptivo,fi,fv,estado,objetivo,equipo)
        else:
            return nodo

        nodo.altura = 1 + max(self.obtener_altura(nodo.izquierda), self.obtener_altura(nodo.derecha))

        balance = self.obtener_balance(nodo)

        if balance > 1 and nombre < nodo.izquierda.nombre:
            return self.rotar_derecha(nodo)

        if balance < -1 and nombre > nodo.derecha.nombre:
            return self.rotar_izquierda(nodo)

        if balance > 1 and nombre > nodo.izquierda.nombre:
            nodo.izquierda = self.rotar_izquierda(nodo.izquierda)
            return self.rotar_derecha(nodo)

        if balance < -1 and nombre < nodo.derecha.nombre:
            nodo.derecha = self.rotar_derecha(nodo.derecha)
            return self.rotar_izquierda(nodo)

        return nodo

    def insertar_archivo(self,id,nombre,nombre_descriptivo,fi,fv,estado,objetivo,equipo):
        self.raiz = self.insertar(self.raiz, id,nombre,nombre_descriptivo,fi,fv,estado,objetivo,equipo)

    def in_order(self, nodo):
        if nodo:
            self.in_order(nodo.izquierda)
            print(nodo.nombre)
            self.in_order(nodo.derecha)
    
    def insertar_otro_externo_para_nuevo (self,clase_nuevo_desde_fuera):
        idd = clase_nuevo_desde_fuera.id
        namee = clase_nuevo_desde_fuera.nombre
        descripcion = clase_nuevo_desde_fuera.nombre_descriptivo
        fii = clase_nuevo_desde_fuera.fi
        fvv = clase_nuevo_desde_fuera.fv
        estadoo = clase_nuevo_desde_fuera.estado
        objetivoo = clase_nuevo_desde_fuera.objetivo
        equipoo = clase_nuevo_desde_fuera.equipo

        self.insertar_archivo(idd,namee,descripcion,fii,fvv,estadoo,objetivoo,equipoo)


# Ejemplo de uso
avl_fs = AVLFileSystem()
avl_fs.insertar_archivo(1,"Jose_empresa","Mucho trabajo","fecha inicial","ficha final","Sigue tra","ganar el juego","Team only")
avl_fs.insertar_archivo(2,"Manu_empresa","Mucho trabajo","fecha inicial","ficha final","Sigue trabajando","ganar el juego","Team only")
avl_fs.insertar_archivo(3,"Juna_empresa","Mucho trabajo","fecha inicial","ficha final","Sigue trabajando","ganar el juego","Team only")

avl_fs.in_order(avl_fs.raiz)

lista =[]
uva = Empresa_work(6,"Uva_empresa","Mucho trabajo","fecha inicial","ficha final","Sigue tra","ganar el juego","Team only")
uva2 = Empresa_work(8,"Uva2_empresa","Mucho trabajo","fecha inicial","ficha final","Sigue tra","ganar el juego","Team only")
lista.append(uva)
lista.append(uva2)

def menu4():
    bandera = 1
    while bandera:
        print("")
        print("1. -> Consultar todos los proyectos existentes")
        print("2. -> Insertar un nuevo proyecto")
        print("7. -> Salir la programa")
        pregunta = input("Elige la opcion: ")

        if pregunta == "1":
            avl_fs.in_order(avl_fs.raiz)

        elif pregunta == "2": 
            opcion = "0"
            print()
            print("1. -> Insertar directamente")
            print("2. -> Elegir un proyecto para pasar al gestion de sprint")
            opcion = input("Elige la opcion: ")
            if opcion == "1":
                print()
                ide = input("El id de proyecto: ")
                bandera_numeral = 0
                while bandera_numeral==0:
                    if ide.isdigit():
                        bandera_numeral = 1
                    else:
                        print("")
                        print("Ha ingresado los caracteres incorrectas, por favor ingresar de nuevo")
                        ide = input("Cuanto cantidad de tarea quiere agregar: ")
                
                #Ingreso datos por el usuario
                ide_verdadero = int(ide)
                nombre = input("El nombre: ")
                descripcion = input("El descripcion: ")
                fecha_inicio = datetime.strptime(input("Ingrese la fecha de inicio del proyecto (Dia-Mes-Año): "), "%d-%m-%Y")
                fecha_final = datetime.strptime(input("Ingrese la fecha de vencimiento del proyecto (Dia-Mes-Año): "), "%d-%m-%Y")
                estado = input("El estado de proyecto: ")
                objetivos = input("El objetivo de proyecto: ")
                equipo = input("El equipo de proyecto: ")
                avl_fs.insertar_archivo(ide_verdadero,nombre,descripcion,fecha_inicio,fecha_final,estado,objetivos,equipo)

            elif opcion == "2":
                opcion_seleccion = int(input("Dar la opcion de lista que no ha entrado en la gestion de sprint: "))
                avl_fs.insertar_otro_externo_para_nuevo(lista[opcion_seleccion-1])
            else:
                print()
                print("Ingresado mal caracteres, por lo tanto regresa el inicio")
            
        elif pregunta == "7":
            bandera = 0
            print("Salir el modo de gestión de sprint")
