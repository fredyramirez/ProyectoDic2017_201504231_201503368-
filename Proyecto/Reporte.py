from MatrizBidimensional import MatrizBidimensional
import os


def generarImagen(nombre):
    
    dotPath = "\"C:\\Graphviz\\bin\\dot.exe\""
    fileInputPath = nombre+".txt"
    fileOutputPath = nombre+".png"
    tParam = " -Tpng "
    tOParam = " -o "    
    tuple = (dotPath + tParam + fileInputPath + tOParam + fileOutputPath)
    print tuple
    os.system(tuple)
    os.system(fileOutputPath)
    
def generarTxt(nombre,dot):
    archivo = open(nombre+".txt", 'w')
    archivo.write(dot)
    archivo.close()
    generarImagen(nombre)

def reporteMatriz(matriz):
    dot = matriz.graficar()
    generarTxt("reporteMatriz",dot)


def reporteArtistas(matriz, anio, genero):
    dot = matriz.getArtistas(anio, genero).getDot()
    generarTxt("reporteArtistas",dot)


def reporteAlbumes(matriz, anio, genero, nombreArtista):
    dot = matriz.getArtistas(anio, genero).busqueda(
        nombreArtista).getAlbumes().graficar()
    generarImagen(dot)


def reporteListaCanciones(matriz, anio, genero, nombreArtista, nombreAlbum):
    matriz.getArtistas(anio, genero).busqueda(nombreArtista).getAlbumes(
    ).getAlbum(nombreAlbum).getCanciones().graficar()


def reporteUsuarios(listaUsuarios):
    listaUsuarios.graficar()


def reporteGeneral(matriz):
    print "ya valimos xD"


def reporteCola(listaUsuarios, nombre):
    listaUsuarios.getCola(nombre).graficar()
