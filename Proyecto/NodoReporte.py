class NodoReporte:
	"""docstring for ClassName"""
	def __init__(self, Cancion, Artistas,Album,Genero, Anio):
		
		self.Cancion = Cancion
		self.Artistas = Artistas
		self.Album = Album
		self.Genero = Genero
		self.Anio = Anio
		self.Siguiente = None

	def getCancion(self):
		return self.Cancion
	

	def getArtistas(self):
		return self.Artistas

	def getAlbum(self):
		return self.Album

	def getGenero(self):
		return self.Genero

	def getAnio(self):
		return self.Anio

	def getSiguiente(self):
		return self.Siguiente

	def setSiguiente(self,Siguiente):
		self.Siguiente = Siguiente