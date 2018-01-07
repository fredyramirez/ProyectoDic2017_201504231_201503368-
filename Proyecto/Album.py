from ListaCanciones import ListaCanciones


class Album:
    """docstring for Album"""
    correlativo = 1

    def __init__(self, nombre, canciones):
        self.nombre = nombre
        self.canciones = canciones
        self.izquierdo = None
        self.derecho = None
        Album.correlativo = Album.correlativo + 1
        self.id = Album.correlativo

    def getCanciones(self):
        return self.canciones

    def insertar(self, nombre, canciones):
        if nombre < self.nombre:
            if self.izquierdo == None:
                self.izquierdo = Album(nombre, canciones)
            else:
                self.izquierdo.insertar(nombre, canciones)
        elif nombre > self.nombre:
            if self.derecho == None:
                self.derecho = Album(nombre, canciones)
            else:
                self.derecho.insertar(nombre, canciones)
        else:
            print "No se permiten los valores duplicados"

    def getCodigoGraphviz(self):
        return "digraph grafica{\nrankdir=TB;\nnode [shape = record, style=filled, fillcolor=seashell2];\n" + self.getCodigoInterno() + "}\n"

    def getCodigoInterno(self):
        etiqueta = ""
        if self.izquierdo == None and self.derecho == None:
            etiqueta = "Album" + str(self.id) + \
                " [ label =\"" + self.nombre + "\"];\n"
        else:
            etiqueta = "Album" + str(self.id) + \
                " [ label =\"<C0>|" + self.nombre + "|<C1>\"];\n"
        if self.izquierdo != None:
            etiqueta = etiqueta + self.izquierdo.getCodigoInterno() + "Album" + str(self.id) + \
                ":C0->Album" + str(self.izquierdo.id) + "\n"
        if self.derecho != None:
            etiqueta = etiqueta + self.derecho.getCodigoInterno() + "Album" + str(self.id) + \
                ":C1->Album" + str(self.derecho.id) + "\n"
        return etiqueta
