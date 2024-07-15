from datetime import datetime

class NodoArbolNario:
    def __init__(self, datos):
        self.datos = datos
        self.hijos = []

    def eliminar_hijo(self, hijo):
        self.hijos = [h for h in self.hijos if h != hijo]

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

class ArbolNario:
    def __init__(self, datos_raiz):
        self.raiz = NodoArbolNario(datos_raiz)

    def agregar_hijo(self, padre, datos_hijo):
        hijo = NodoArbolNario(datos_hijo)
        padre.agregar_hijo(hijo)
        return hijo

    def preorden(self, nodo):
        if nodo:
            print(nodo.datos, end=" ")
            for hijo in nodo.hijos:
                self.preorden(hijo)

    def postorden(self, nodo):
        if nodo:
            for hijo in nodo.hijos:
                self.postorden(hijo)
            print(nodo.datos, end=" ")

    def profundidad(self, nodo):
        if not nodo:
            return 0
        if not nodo.hijos:
            return 1
        return 1 + max(self.profundidad(h) for h in nodo.hijos)

    def encontrar_padre(self, actual, objetivo):
        if not actual:
            return None
        for hijo in actual.hijos:
            if hijo == objetivo:
                return actual
            padre = self.encontrar_padre(hijo, objetivo)
            if padre:
                return padre
        return None

    def modificar_por_atributo(self, atributo, valor, nuevos_datos):
        nodo_modificar = self.encontrar_por_atributo(atributo, valor)
        if nodo_modificar:
            nodo_modificar.datos.id = nuevos_datos['id']
            nodo_modificar.datos.nombre = nuevos_datos['nombre']
            nodo_modificar.datos.descripcion = nuevos_datos['descripcion']
            nodo_modificar.datos.fecha_inicio = nuevos_datos['fecha_inicio']
            nodo_modificar.datos.fecha_vencimiento = nuevos_datos['fecha_vencimiento']
            nodo_modificar.datos.estado = nuevos_datos['estado']
            nodo_modificar.datos.empresa = nuevos_datos['empresa']
            nodo_modificar.datos.porcentaje = nuevos_datos['porcentaje']
            return True
        return False

    def eliminar_nodo(self, objetivo):
        if self.raiz == objetivo:
            self.raiz = None
        else:
            padre = self.encontrar_padre(self.raiz, objetivo)
            if padre:
                padre.eliminar_hijo(objetivo)

    def nodos_en_nivel(self, nivel):
        if not self.raiz:
            return []
        if nivel == 0:
            return [self.raiz.datos]

        actual = 0
        cola = [self.raiz]

        while cola:
            siguiente_cola = []
            actual += 1
            for nodo in cola:
                siguiente_cola.extend(nodo.hijos)
            if actual == nivel:
                return [h.datos for h in siguiente_cola]
            cola = siguiente_cola

        return []

    def mostrar_arbol(self, nodo, nivel=0):
        if nodo:
            print(' ' * nivel * 2 + str(nodo.datos))
            for hijo in nodo.hijos:
                self.mostrar_arbol(hijo, nivel + 1)

    def encontrar(self, datos):
        return self._encontrar_recursivo(self.raiz, datos)

    def _encontrar_recursivo(self, nodo, datos):
        if nodo is None:
            return None
        if nodo.datos == datos:
            return nodo
        for hijo in nodo.hijos:
            resultado = self._encontrar_recursivo(hijo, datos)
            if resultado:
                return resultado
        return None

    def encontrar_por_atributo(self, atributo, valor):
        return self._encontrar_por_atributo_recursivo(self.raiz, atributo, valor)

    def _encontrar_por_atributo_recursivo(self, nodo, atributo, valor):
        if nodo is None:
            return None
        if getattr(nodo.datos, atributo, None) == valor:
            return nodo
        for hijo in nodo.hijos:
            resultado = self._encontrar_por_atributo_recursivo(hijo, atributo, valor)
            if resultado:
                return resultado
        return None

    def eliminar_por_atributo(self, atributo, valor):
        objetivo = self.encontrar_por_atributo(atributo, valor)
        if objetivo:
            if self.raiz == objetivo:
                self.raiz = None
            else:
                padre = self.encontrar_padre(self.raiz, objetivo)
                if padre:
                    padre.eliminar_hijo(objetivo)
                    return True
        return False

    def inorden(self, nodo):
        resultado = []
        self._inorden_recursivo(nodo, resultado)
        return resultado

    def _inorden_recursivo(self, nodo, resultado):
        if nodo:
            for hijo in nodo.hijos:
                self._inorden_recursivo(hijo, resultado)
            resultado.append(nodo.datos)

def reportes(arbol):
    print("\n1. Recorrer las tareas de un proyecto en PostOrden")
    print("2. Listar sprints de un proyecto")
    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        nombre_proyecto = input("Ingrese el nombre del proyecto: ")
        proyecto = arbol.encontrar_por_atributo('nombre', nombre_proyecto)
        if proyecto:
            arbol.postorden(proyecto)
            print()
        else:
            print("No se encontró el proyecto.")

    elif opcion == 2:
        nombre_proyecto = input("Ingrese el nombre del proyecto: ")
        proyecto = arbol.encontrar_por_atributo('nombre', nombre_proyecto)
        if proyecto:
            nivel = int(input("Ingrese la altura desde donde desea mostrar los sprints: "))
            nodos = arbol.nodos_en_nivel(nivel)
            for nodo in nodos:
                print(nodo)
        else:
            print("No se encontró el proyecto.")

    else:
        print("Opción no válida.")

def menu5():
    arbol = None

    while True:
        print("\n--- Menú de Gestión de Proyecto ---")
        print("0. Crear Arbol")
        print("1. Agregar un nodo al árbol")
        print("2. Modificar un nodo")
        print("3. Eliminar un nodo")
        print("4. Mostrar el árbol")
        print("5. Buscar un nodo por atributo")
        print("6. Reportes")
        print("7. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 0:
            try:
                nombre = input('Ingrese el nombre del Arbol: ')
                arbol = ArbolNario(f"Arbol {nombre}")
                print(f"Arbol {nombre} creado exitosamente")
            except:
                print('Error al crear el arbol')

        elif opcion == 1:
            if arbol:
                datos_padre = input("Ingrese los datos del nodo padre: ")
                padre = arbol.encontrar(datos_padre)
                if padre:
                    datos_hijo = input("Ingrese los datos del nuevo nodo: ")
                    arbol.agregar_hijo(padre, datos_hijo)
                    print("Nodo agregado exitosamente.")
                else:
                    print("Nodo padre no encontrado.")
            else:
                print("Primero debe crear un árbol.")

        elif opcion == 2:
            if arbol:
                atributo = input("Ingrese el atributo del nodo a modificar (por ejemplo, 'nombre'): ")
                valor = input("Ingrese el valor del atributo del nodo a modificar: ")
                nuevos_datos = input("Ingrese los nuevos datos del nodo (formato: id,nombre,descripcion,fecha_inicio,fecha_vencimiento,estado,empresa,porcentaje): ").split(',')
                nuevos_datos_nodo = {
                    'id': int(nuevos_datos[0]),
                    'nombre': nuevos_datos[1],
                    'descripcion': nuevos_datos[2],
                    'fecha_inicio': nuevos_datos[3],
                    'fecha_vencimiento': nuevos_datos[4],
                    'estado': nuevos_datos[5],
                    'empresa': nuevos_datos[6],
                    'porcentaje': float(nuevos_datos[7])
                }
                exito = arbol.modificar_por_atributo(atributo, valor, nuevos_datos_nodo)
                if exito:
                    print("Nodo modificado exitosamente.")
                else:
                    print("No se encontró el nodo o no se pudo modificar.")
            else:
                print("Primero debe crear un árbol.")

        elif opcion == 3:
            if arbol:
                atributo = input("Ingrese el atributo del nodo a eliminar (por ejemplo, 'nombre'): ")
                valor = input("Ingrese el valor del atributo del nodo a eliminar: ")
                exito = arbol.eliminar_por_atributo(atributo, valor)
                if exito:
                    print("Nodo eliminado exitosamente.")
                else:
                    print("No se encontró el nodo o no se pudo eliminar.")
            else:
                print("Primero debe crear un árbol.")

        elif opcion == 4:
            if arbol:
                arbol.mostrar_arbol(arbol.raiz)
            else:
                print("Primero debe crear un árbol.")

        elif opcion == 5:
            if arbol:
                atributo = input("Ingrese el atributo del nodo a buscar (por ejemplo, 'nombre'): ")
                valor = input("Ingrese el valor del atributo del nodo a buscar: ")
                nodo = arbol.encontrar_por_atributo(atributo, valor)
                if nodo:
                    print("Nodo encontrado:", nodo.datos)
                else:
                    print("No se encontró el nodo.")
            else:
                print("Primero debe crear un árbol.")

        elif opcion == 6:
            if arbol:
                reportes(arbol)
            else:
                print("Primero debe crear un árbol.")

        elif opcion == 7:
            print("Saliendo del menú.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

