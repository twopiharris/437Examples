import java.awt.*;
import javax.swing.*;
import java.awt.geom.*;

public class Graphics2 extends JFrame {
  public static void main(String[] args){
    new Graphics2();
  } // end main

  MyCanvas c = new MyCanvas();

  public Graphics2(){
    this.setLayout(new BorderLayout());
    add(c, BorderLayout.CENTER);

    this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    this.setSize(640, 480);
    this.setVisible(true);
  } // end Graphics2

  class MyCanvas extends JPanel{
    
    @Override
    public void paintComponent(Graphics g){
      Graphics2D g2 = (Graphics2D)g;
    
      g2.setColor(Color.RED);

      //change line width
      g2.setStroke(new BasicStroke(5));

      g2.drawRect(100, 100, 200, 200);

      //change to a new color
      g2.setColor(Color.BLUE);
      g2.fillRect(300, 300, 100, 100);


      g2.setColor(Color.GREEN);

      //store current transformations
      AffineTransform t = g2.getTransform();

      // apply transformations
      g2.translate(200, 200);
      g2.rotate(Math.PI / 4);

      // new object drawn inside new transformation
      g2.fillRoundRect(0, 0, 100, 100, 10, 10);


      //restore original transformation
      g2.setTransform(t);

      //new drawings do not incorporate rotation
      g2.setColor(Color.YELLOW);
      g2.fillRect(10, 10, 100, 100);

      repaint();
    } // end paintComponent
  } // end MyCanvas

} // end Graphics2

      
