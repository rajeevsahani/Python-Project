import java.awt.*;
import java.awt.image.BufferedImage;
import java.util.*;
import java.io.*;

import javax.imageio.ImageIO;
import javax.swing.JFrame;

class ImageEncryption 
{
        
   static public void main(String args[]) throws Exception 
   {  
      //System.out.print("Enter Plain Text:");
      //Scanner scanner = new Scanner(System.in);
      //String plain = scanner.nextLine();
      String plain="HELLO";
      System.out.println("Your Plain Text is  " + plain);
      char[] w = plain.toCharArray();
      int a[]=new int[plain.length()];
      ArrayList<Integer> ascii=new ArrayList<Integer>();//Creating arraylist
      for (int k = 0; k < plain.length(); k++) 
      {
         a[k]=(int)w[k];
         ascii.add(a[k]);
      //System.out.println(" "+w[k]+" "+(int)w[k]);
      }
      System.out.print("Ascii Value corresponding to plain Text: "); 
      for(Integer i:ascii)
         System.out.print(i+" ");
      System.out.println();
      BufferedImage image;
      int width;
      int height;
      File input = new File("Output.jpg");
      image = ImageIO.read(input);
      width = image.getWidth();
      height = image.getHeight();
      int original[][]=new int[width][height];
      int gray[][]=new int[height][width];
      ArrayList<Integer> pos=new ArrayList<Integer>();
      int count = 0;
      for(int i=0; i<height; i++) 
      {
         for(int j=0; j<4; j++) 
         {
            //count++;
            Color c = new Color(image.getRGB(i, j));
            System.out.println("Index is "+ i+" "+j + " Code " + c.getRed() +" ");
            //original[i][j]=c.getRed();
            //pos[i][j]=count;
            //pos.add(count);
            //System.out.print(count+" "+c.getRed()+" ");
            //System.out.print(gray[i][j]+" ");
         }
         //System.out.println();
      }
      /*
      for(int i=0; i<height; i++) 
      {
         for(int j=0; j<width; j++) 
         {
            gray[i][j]=original[j][i];
         }
      }
      
      ArrayList<Integer> loc=new ArrayList<Integer>();//Creating arraylist
      for(Integer s:ascii) 
      {
         for(int i=0; i<height; i++) 
         {
         
            for(int j=0; j<width; j++) 
            {
               //System.out.print(pos[i][j]+" "+gray[i][j]+" ");
               if(s==gray[i][j])
               {
                  loc.add(height*j+i);
                  
               }
            }
            
         }
         System.out.println(s+" Processing Completed and Matched at following location");
         System.out.print(loc.size()+" value is "+loc);
         int p = loc.get(new Random().nextInt(loc.size()));
         System.out.println(p);
         for(int i=0; i<height; i++) 
         {
            for(int j=0; j<width; j++) 
            {
               //System.out.print(pos[i][j]+" "+gray[i][j]+" ");
               if(p==(height*j+i))
               {
                  System.out.println(gray[i][j]+" ");
                  
               }
            }
            
         }
     }
      */
 
   }
}