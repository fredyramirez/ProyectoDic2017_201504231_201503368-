package proyecto_edd_dic;

import java.io.File;
import javazoom.jlgui.basicplayer.BasicPlayer;


public class reproductor {
    public BasicPlayer player;

    public reproductor() {
        player = new BasicPlayer();
    }
public void coge(String y){

}
    public void Play() throws Exception {
        player.play();
    }

    public void AbrirFichero(String ruta) throws Exception {
        player.open(new File(ruta));
    }

    public void Pausa() throws Exception {
        player.pause();
    }

    public void Continuar() throws Exception {
        player.resume();
    }

    public void Stop() throws Exception {
        player.stop();
    }
    public void reproducemp3 () throws Exception{
       try {
        reproductor   mi_reproductor = new reproductor();
            mi_reproductor.AbrirFichero("C:/Users/jose_/Music/Mi Segunda Vida.mp3");
            mi_reproductor.Play();
        } catch (Exception ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
    public static void main(String args[]) throws Exception{
     reproductor y = new reproductor();
     y.AbrirFichero("C:/Users/jose_/Music/Mi Segunda Vida.mp3");
    
     
     y.Play();
    }
}