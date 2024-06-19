import Gestion_Proyectos as gp

class Nodo_Tarea:
    def __init__(self, nombre, fecha_creacion, fecha_modificacion, tamano, contenido):
        self.nombre = nombre
        self.fecha_creacion = fecha_creacion
        self.fecha_modificacion = fecha_modificacion
        self.tamano = tamano
        self.contenido = contenido
        self.siguiente = None

class PilaArchivos:
    def __init__(self):
        self.cabeza = None

    def agregar_archivo(self, nombre, fecha_creacion, fecha_modificacion, tamano, contenido):
        nuevo_nodo = NodoArchivo(nombre, fecha_creacion, fecha_modificacion, tamano, contenido)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo

    def mostrar_archivos(self):
        actual = self.cabeza
        while actual:
            print("Nombre:", actual.nombre)
            print("Fecha de creación:", actual.fecha_creacion)
            print("Fecha de modificación:", actual.fecha_modificacion)
            print("Tamaño:", actual.tamano)
            print("Contenido:", actual.contenido)
            print()
            actual = actual.siguiente

    def buscar_archivo(self, nombre):
        actual = self.cabeza
        while actual:
            if actual.nombre == nombre:
                return True
            actual = actual.siguiente
        return False

    def eliminar_archivo(self):
        if not self.cabeza:
            return None
        eliminado = self.cabeza
        self.cabeza = self.cabeza.siguiente
        return eliminado

    def modificar_archivo(self, nombre, nuevo_nombre, fecha_modificacion, tamano, contenido):
        actual = self.cabeza
        while actual:
            if actual.nombre == nombre:
                actual.nombre = nuevo_nombre
                actual.fecha_modificacion = fecha_modificacion
                actual.tamano = tamano
                actual.contenido = contenido
                return True
            actual = actual.siguiente
        return False

    def obtener_posicion(self, nombre):
        actual = self.cabeza
        pos = 0
        while actual:
            if actual.nombre == nombre:
                return pos
            actual = actual.siguiente
            pos += 1
        return -1
class App:
    def main(self):
        print("---------PILA DE ARCHIVOS---------")

        # Crear una pila de archivos
        pila_archivos = PilaArchivos()
        pila_archivos.agregar_archivo("documento1.txt", "2024-01-01", "2024-02-01", "1024 KB", "Contenido del archivo 1")
        pila_archivos.agregar_archivo("imagen.png", "2024-01-02", "2024-02-02", "2048 KB", "Contenido de la imagen")
        pila_archivos.agregar_archivo("archivo.zip", "2024-01-03", "2024-02-03", "4096 KB", "Contenido del archivo comprimido")

        # Mostrar la pila de archivos
        print("Archivos en la pila:")
        pila_archivos.mostrar_archivos()

        # Buscar un archivo
        print("\nBuscar archivo:")
        print("¿documento1.txt existe?", pila_archivos.buscar_archivo("documento1.txt"))

        # Eliminar un archivo
        eliminado = pila_archivos.eliminar_archivo()
        print("\nArchivo eliminado:")
        if eliminado:
            print("Nombre:", eliminado.nombre)
            print("Fecha de creación:", eliminado.fecha_creacion)
            print("Fecha de modificación:", eliminado.fecha_modificacion)
            print("Tamaño:", eliminado.tamano)
            print("Contenido:", eliminado.contenido)
        else:
            print("La pila está vacía.")

        # Mostrar la pila de archivos después de eliminar
        print("\nArchivos en la pila después de eliminar:")
        pila_archivos.mostrar_archivos()

        # Modificar un archivo
        print("\nModificar archivo:")
        print("¿imagen.png renombrado a imagen_modificada.png?",
            pila_archivos.modificar_archivo("imagen.png", "imagen_modificada.png", "2024-02-04", "2048 KB", "Nuevo contenido de la imagen"))
        print("Archivos en la pila después de modificar:")
        pila_archivos.mostrar_archivos()

        # Obtener la posición de un archivo en la pila
        print("\nObtener posición:")
        print("Posición de 'imagen.png':", pila_archivos.obtener_posicion("imagen.png"))
        print("Posición de 'archivo.zip':", pila_archivos.obtener_posicion("archivo.zip"))

app = App()
app.main()