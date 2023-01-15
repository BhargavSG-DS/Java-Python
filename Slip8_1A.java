import java.io.*;

import java.util.*;

interface shape

{

float pi=3.14f;

void area();

}

class circle implements shape

{

int r;

circle(int r)

{

this.r=r;

}

public void area()

{

System.out.println("Area of circle is :"+(pi*r*r));

}

}

class sphere implements shape

{

int r;

sphere(int r)

{

this.r=r;

}

public void area()

{

System.out.println("Area of sphere is :"+(4*pi*r*r));

}

}

class Slip8_1A

{

public static void main(String arg[])

{

Scanner sc=new Scanner(System.in);

System.out.println("enter the redius for circle :");

int n=sc.nextInt();

shape s;

s=new circle(n);

s.area();

System.out.println("enter the redius for sphere :");

n=sc.nextInt();

s=new sphere(n);

s.area(); 

}

}

