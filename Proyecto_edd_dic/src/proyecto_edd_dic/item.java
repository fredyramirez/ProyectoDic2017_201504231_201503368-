/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package proyecto_edd_dic;

/**
 *
 * @author jose_
 */
public class item {
    String nombreCancion , Artista, album,genero,anio;

    public item(String nombreCancion, String Artista, String album,String genero ,String anio) {
        this.nombreCancion = nombreCancion;
        this.Artista = Artista;
        this.album = album;
        this.genero= genero;
        this.anio=anio;
    }
    
     public String getGenero() {
        return genero;
    }

    public void setGenero(String genero) {
        this.genero = genero;
    }
     public String getAnio() {
        return anio;
    }

    public void setAnio(String anio) {
        this.anio = anio;
    }
    public String getNombreCancion() {
        return nombreCancion;
    }

    public void setNombreCancion(String nombreCancion) {
        this.nombreCancion = nombreCancion;
    }

    public String getArtista() {
        return Artista;
    }
    
    public void setArtista(String Artista) {
        this.Artista = Artista;
    }

    public String getAlbum() {
        return album;
    }

    public void setAlbum(String album) {
        this.album = album;
    }
    
}
