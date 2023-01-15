import java.io.*;

class Slip18_1B

{

 public static void main(String args[])throws IOException

 {

  int c;

  try

  {

   FileReader fr=new FileReader("src/test#18.txt");

   FileWriter fw=new FileWriter("src/results#18.txt");

   while((c=fr.read())!=-1)

   {

    if(c>=65&&c<=90)

    {

     c=c+32;

     fw.write(c);

    }

    else if(c>=97&&c<=122)

    {

     c=c-32;

     fw.write(c);

    }

    else if(c>=48&&c<=57)

    {

     fw.write('*');

    }

    else

    {

     fw.write(c);

    }

    

   }

   System.out.println("Copy Successfully");

   fr.close();

   fw.close();

  }catch(Exception e)

  {

   System.out.println(e);

  }

 }

}