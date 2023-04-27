import random

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBST:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(valor, self.raiz)

    def _insertar(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._insertar(valor, nodo_actual.izquierda)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self._insertar(valor, nodo_actual.derecha)
        else:
            # El valor ya está en el árbol
            pass

    def barrido_preorden(self):
        if self.raiz is not None:
            self._barrido_preorden(self.raiz)

    def _barrido_preorden(self, nodo_actual):
        if nodo_actual is not None:
            print(nodo_actual.valor)
            self._barrido_preorden(nodo_actual.izquierda)
            self._barrido_preorden(nodo_actual.derecha)

    def barrido_inorden(self):
        if self.raiz is not None:
            self._barrido_inorden(self.raiz)

    def _barrido_inorden(self, nodo_actual):
        if nodo_actual is not None:
            self._barrido_inorden(nodo_actual.izquierda)
            print(nodo_actual.valor)
            self._barrido_inorden(nodo_actual.derecha)

    def barrido_postorden(self):
        if self.raiz is not None:
            self._barrido_postorden(self.raiz)

    def _barrido_postorden(self, nodo_actual):
        if nodo_actual is not None:
            self._barrido_postorden(nodo_actual.izquierda)
            self._barrido_postorden(nodo_actual.derecha)
            print(nodo_actual.valor)

    def barrido_por_nivel(self):
        if self.raiz is not None:
            cola = [self.raiz]
            while cola:
                nodo_actual = cola.pop(0)
                print(nodo_actual.valor)
                if nodo_actual.izquierda is not None:
                    cola.append(nodo_actual.izquierda)
                if nodo_actual.derecha is not None:
                    cola.append(nodo_actual.derecha)

    def buscar(self, valor):
        return self._buscar(valor, self.raiz)

    def _buscar(self, valor, nodo_actual):
        if nodo_actual is None:
            return False
        elif valor == nodo_actual.valor:
            return True
        elif valor < nodo_actual.valor:
            return self._buscar(valor, nodo_actual.izquierda)
        else:
            return self._buscar(valor, nodo_actual.derecha)

    def eliminar(self, valor):
        if self.raiz is not None:
            self.raiz = self._eliminar(valor, self.raiz)

    def _eliminar(self, valor, nodo_actual):
        if nodo_actual is None:
            return nodo_actual
        if valor < nodo_actual.valor:
            nodo_actual.izquierda = self._eliminar(valor, nodo_actual.izquierda)
        elif valor > nodo_actual.valor:
            nodo_actual.derecha = self._eliminar(valor, nodo_actual.derecha)
        else:
            if nodo_actual.izquierda is None:
                return nodo_actual.derecha
            elif nodo_actual.derecha is None:
                return nodo_actual.izquierda
            else:
                nodo_actual.valor = self._minimo(nodo_actual.derecha)
                nodo_actual.derecha = self._eliminar(nodo_actual.valor, nodo_actual.derecha)
        return nodo_actual
    
def main():
    print("Bienvenido al generador de números aleatorios.")
    numeros = int(input("¿Cuantos números quieres generar? [1-20]: "))
    modo = int(input("¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal: "))
    lista_numeros = []
    for i in range(numeros):
        numero = random.uniform(0, 100)
        if modo == 1:
            redondeo = math.ceil(numero)
        elif modo == 2:
            redondeo = math.floor(numero)
        else:
            redondeo = round(numero)
        print(f"Número: {numero}, redondeado: {redondeo}")
        lista_numeros.append(redondeo)
    print(lista_numeros)
    arbol = ArbolBST()
    for i in lista_numeros:
        arbol.insertar(i)
    print("Barrido preorden:")
    arbol.barrido_preorden()
    print("Barrido inorden:")
    arbol.barrido_inorden()
    print("Barrido postorden:")
    arbol.barrido_postorden()
    print("Barrido por nivel:")
    arbol.barrido_por_nivel()
    print("Buscar 5:")
    print(arbol.buscar(5))
    print("Buscar 100:")
    print(arbol.buscar(100))
    print("Eliminar 5:")
    arbol.eliminar(5)
    print("Barrido preorden:")
    arbol.barrido_preorden()
    print("Barrido inorden:")
    arbol.barrido_inorden()
    print("Barrido postorden:")
    arbol.barrido_postorden()
    print("Barrido por nivel:")
    arbol.barrido_por_nivel()

if __name__ == "__main__":
    main()