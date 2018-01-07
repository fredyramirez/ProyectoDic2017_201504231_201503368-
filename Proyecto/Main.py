from flask import Flask, session
from flask import request
from flask import make_response
import Reporte

from CargaMasiva import CargaMasiva

app = Flask(__name__)
Carga = CargaMasiva()


def main():
    print "exito!!"


@app.route('/login', methods=['POST'])
def login():
    usuario = str(request.form['usuario'])
    pas = str(request.form['contra'])
    print usuario
    print Carga.usuarios.login(usuario, pas)
    return Carga.usuarios.login(usuario, pas)


@app.route('/CargaMasiva', methods=['POST'])
def CargaMasiva():

    path = str(request.form['path'])
    print path
    Carga.analizarXML(path)
    return "Si se pudo"


@app.route('/reporteUsuarios', methods=['POST'])
def reporteUsuarios():

    Reporte.reporteUsuarios(Carga.getUsuarios())
    return "Si se pudo"

@app.route('/reporteMatriz', methods=['POST'])
def reporteMatriz():

    Reporte.reporteMatriz(Carga.getMatriz())
    return "Si se pudo"
@app.route('/reporteArtista', methods=['POST'])
def reporteArtista():
	year = str(request.form['anio'])
	gen = str(request.form['genero'])
	Reporte.reporteArtistas(Carga.getMatriz(),year,gen)
	return "Si se pudo"

@app.route('/replistaCancion', methods=['POST'])
def replistaCancion():
	year = str(request.form['anio'])
	gen = str(request.form['genero'])
	nombreArtista = str(request.form['artista'])
	nombreAlbum = str(request.form['nombreAlbum'])
	Reporte.reporteListaCanciones(Carga.getMatriz(), year, gen, nombreArtista, nombreAlbum)
	return "Si se pudo"

@app.route('/getAlbumes', methods=['POST'])
def getAlbumes():

    return "Si se pudo"


@app.route('/CancionesSistema', methods=['POST'])
def CancionesSistema():
    aux = Carga.listaReporte.obtener()
    titulo = aux.Cancion
    artista = aux.Artistas
    album = aux.Album
    genero = aux.Genero
    Anio = aux.Anio

    return str(titulo) + "~" + str(artista) + "~" + str(album) + "~" + str(genero) + "~" + str(Anio)

if __name__ == '__main__':
    app.run(debug=True)
