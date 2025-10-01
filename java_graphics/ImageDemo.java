import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import java.awt.image.*;
import java.io.*;
import javax.imageio.*;

public class ImageDemo extends JFrame {
  public static void main(String[] args){
    new ImageDemo();
  } // end main

  public ImageDemo(){

    MyCanvas c = new MyCanvas();
    this.add(c, BorderLayout.CENTER);

    this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    this.setSize(640, 480);
    this.setVisible(true);
  } // end constructor


  class MyCanvas extends JPanel{

    public void paintComponent(Graphics g){
      // create an empty buffered image object
      BufferedImage Emu = null; 
      

      //attempt to load the image from a file
      try {
        Emu = ImageIO.read(new File("emu_face.jpg"));
      } catch (Exception e){
        System.out.println("file error");
      } // end try

      // draw the image to fill rectangle 10, 10, 210, 210
      // encompasing the entire source image
      // using white to fill in any blank spaces,
      // and with no imageObserver

      g.drawImage(Emu, 10, 10, 200, 200, 
          0, 0, Emu.getWidth(), Emu.getHeight(),
          Color.WHITE, null); 

/*      
      g.drawImage(Emu, 10, 10, 200, 200, 
                0, 0, 400, 400, 
                          Color.WHITE, null); 
*/

      this.repaint();
    } // end paint

  } // end class def

} // end class def

