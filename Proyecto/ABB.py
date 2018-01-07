from Album import Album


class ABB:
    """docstring for ABB"""

    def __init__(self):
        self.raiz = None

    def insertar(self, nombre, listaCanciones):
        if self.raiz == None:
            self.raiz = Album(nombre, listaCanciones)
        else:
            self.raiz.insertar(nombre, listaCanciones)

    def graficar(self):
        return self.raiz.getCodigoGraphviz()

    def inorden(self):
        print u"Recorrido inorden del arbol binario de busqueda"
        self.inordenAux(self.raiz)
        print "\n"

    def getAlbum(self, nombre):
        return self.inordenAux(self.raiz)

    def getAlbumAux(self, actual, nombre):
        if actual == None:
            return
        self.inordenAux(actual.izquierdo)
        if actual.nombre == nombre:
            return actual
        self.inordenAux(actual.derecho)

    def inordenAux(self, a):
        if a == None:
            return
        self.inordenAux(a.izquierdo)
        print a.nombre + ","
        self.inordenAux(a.derecho)
