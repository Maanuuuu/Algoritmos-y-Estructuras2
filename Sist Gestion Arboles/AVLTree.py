
class NodoProyecto:
    def __init__(self, proyecto):
        self.proyecto = proyecto
        self.izquierda = None
        self.derecha = None
        self.altura = 1

class ArbolProyectos:
    def __init__(self):
        self.raiz = None

    def altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def balance_factor(self, nodo):
        if not nodo:
            return 0
        return self.altura(nodo.izquierda) - self.altura(nodo.derecha)

    def rotacion_derecha(self, y):
        x = y.izquierda
        T2 = x.derecha
        x.derecha = y
        y.izquierda = T2
        y.altura = max(self.altura(y.izquierda), self.altura(y.derecha)) + 1
        x.altura = max(self.altura(x.izquierda), self.altura(x.derecha)) + 1
        return x

    def rotacion_izquierda(self, x):
        y = x.derecha
        T2 = y.izquierda
        y.izquierda = x
        x.derecha = T2
        x.altura = max(self.altura(x.izquierda), self.altura(x.derecha)) + 1
        y.altura = max(self.altura(y.izquierda), self.altura(y.derecha)) + 1
        return y

    def insertar(self, raiz, proyecto):
        if not raiz:
            return NodoProyecto(proyecto)
        
        if proyecto.tiempo_restante > raiz.proyecto.tiempo_restante:
            raiz.izquierda = self.insertar(raiz.izquierda, proyecto)
        else:
            raiz.derecha = self.insertar(raiz.derecha, proyecto)

        raiz.altura = 1 + max(self.altura(raiz.izquierda), self.altura(raiz.derecha))
        balance = self.balance_factor(raiz)

        if balance > 1:
            if proyecto.tiempo_restante > raiz.izquierda.proyecto.tiempo_restante:
                return self.rotacion_derecha(raiz)
            else:
                raiz.izquierda = self.rotacion_izquierda(raiz.izquierda)
                return self.rotacion_derecha(raiz)

        if balance < -1:
            if proyecto.tiempo_restante <= raiz.derecha.proyecto.tiempo_restante:
                return self.rotacion_izquierda(raiz)
            else:
                raiz.derecha = self.rotacion_derecha(raiz.derecha)
                return self.rotacion_izquierda(raiz)

        return raiz

    def insertar_proyecto(self, proyecto):
        self.raiz = self.insertar(self.raiz, proyecto)

    def buscar(self, raiz, criterio, valor):
        if not raiz:
            return []
        
        resultados = []
        if getattr(raiz.proyecto, criterio) == valor:
            resultados.append(raiz.proyecto)
        
        resultados.extend(self.buscar(raiz.izquierda, criterio, valor))
        resultados.extend(self.buscar(raiz.derecha, criterio, valor))
        return resultados

    def buscar_proyecto(self, criterio, valor):
        return self.buscar(self.raiz, criterio, valor)

    def actualizar_tiempo_restante(self):
        self._actualizar_tiempo_restante_recursivo(self.raiz)

    def _actualizar_tiempo_restante_recursivo(self, nodo):
        if nodo:
            nodo.proyecto.actualizar_tiempo_restante()
            self._actualizar_tiempo_restante_recursivo(nodo.izquierda)
            self._actualizar_tiempo_restante_recursivo(nodo.derecha)
