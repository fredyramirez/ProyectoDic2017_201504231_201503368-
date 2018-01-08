package proyecto_edd_dic;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.logging.Level;
/**
 *
 * @author jose_
 */
public class WService {
    public static OkHttpClient webClient = new OkHttpClient();

    
    
    public static String getString(String metodo, RequestBody formBody) {

        try {
            URL url = new URL("http://localhost:5000/" + metodo);
            //http://127.0.0.1:5000/
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();//Aqui obtiene la respuesta en dado caso si hayas pues un return en python
            String response_string = response.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
            java.util.logging.Logger.getLogger(WService.class.getName()).log(Level.SEVERE, null, ex);
        } catch (Exception ex) {
            java.util.logging.Logger.getLogger(WService.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }
    public static void insertarUsuario(String nombre , String pass){
        RequestBody request = new FormEncodingBuilder()
                .add("usuario",nombre)
                .add("contra", pass).build();
        String r = getString("registro", request);
        System.out.println(r);
        
    }
    public static void cargaMasiva(String path){
        
        RequestBody request = new FormEncodingBuilder().add("path", path).build();
        String r = getString("CargaMasiva", request);
        System.out.println(r);
    }
    public static void reporteUsuarios(){
        RequestBody request = new FormEncodingBuilder().add("asdf", "asdf").build();
        String respuesta = getString("reporteUsuarios",request);
        System.err.println(respuesta);
    }
    public static void reporteMatriz(){
        RequestBody request = new FormEncodingBuilder().add("asdf","asdf").build();
        String respuesta = getString("reporteMatriz",request);
        System.err.println(respuesta);
    }
    // metodos re los reportes 
    public static void reporteArtistas(String genero , String year){
        System.out.println(genero);
        System.out.println(year);
    RequestBody request = new FormEncodingBuilder()
                .add("genero",genero)
                .add("anio", year).build();
        String respuesta = getString("reporteArtista",request);
        System.err.println(respuesta);
    }
    public static void reporteAlbumes(String genero , String anio , String artista){
        RequestBody request = new FormEncodingBuilder()
                .add("genero",genero)
                .add("anio", anio)
                .add("artista", artista).build();
        String respuesta = getString("reporteAlbumesEspecifico",request);
        System.err.println(respuesta);
    }
     public static void reporteColaUsuario(){
        RequestBody request = new FormEncodingBuilder()
                .add("artista", "asdf").build();
        String respuesta = getString("reporteAlbumesEspecifico",request);
        System.err.println(respuesta);
    }
    public static void reportelistaCanciones(String genero , String year , String artista, String album){
        RequestBody request = new FormEncodingBuilder()
                .add("genero",genero)
                .add("anio", year)
                .add("artista", artista)
                .add("album",album)
                .build();
        String respuesta = getString("replistaCancion",request);
        System.err.println(respuesta);
    }
    public static String getRegistro(){
        String cadena="";
        RequestBody request = new FormEncodingBuilder().add("registro","registro").build();
         String respuesta = getString("CancionesSistema",request);
         System.out.println(respuesta);
         cadena = respuesta;
        return cadena;
    }
    public static String getArtistas(){
        RequestBody request = new FormEncodingBuilder().build();
        String respuesta = getString("obtenerArtistas", request);
        return respuesta;
    }
    public static String getAlbumes(){
        RequestBody request = new FormEncodingBuilder().build();
        String respuesta = getString("obtenerAlbumes", request);
        return respuesta;
    }
    public static String getAnios(){
        RequestBody request = new FormEncodingBuilder().build();
        String respuesta = getString("obtenerAnios", request);
        return respuesta;
    }
    public static String getGeneros(){
        RequestBody request = new FormEncodingBuilder().build();
        String respuesta = getString("obtenerGeneros", request);
        return respuesta;
    }
    public static void reporteListaCanciones(String genero , String year , String artista, String album){
         RequestBody request = new FormEncodingBuilder()
                .add("genero",genero)
                .add("anio", year)
                .add("artista", artista)
                .add("album", album)
                 .build();
        String respuesta = getString("",request);
        System.err.println(respuesta);
    }
    public static void reporteUsuariosSistema(){
     RequestBody request = new FormEncodingBuilder().build();
        String respuesta = getString("",request);
        System.err.println(respuesta);
    
    }
    
    
    public static String login(String nombre, String pass){
        RequestBody request = new FormEncodingBuilder()
                .add("usuario",nombre)
                .add("contra", pass).build();
        String respuesta = getString("login",request);
        System.out.println(respuesta);
        return respuesta;
    }
     public static String metodoPost(String parametroJava) {
        RequestBody formBody = new FormEncodingBuilder()
                .add("x", parametroJava)
                .build();
        String r = getString("metodos", formBody);
        System.out.println("respuesta:" + r);
        return r;
    }

    
    public static void main(String[] args) {
        metodoPost("secreto");
    }

}
