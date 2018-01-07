class Coordenada:
    """docstring for Coordenada"""

    def __init__(self, anio, genero):
        self.anio = anio
        self.genero = genero
        self.siguiente = None

    def getAnio(self):
        return self.anio

    def getGenero(self):
        return self.genero

    def getSiguiente(self):
        return self.Siguiente

    def setSiguiente(self, Siguiente):
        self.Siguiente = Siguiente
