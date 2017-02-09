# -*- coding: utf-8 -*-
import random

def retornarMaso():
   return ['A_♥','A_♣','A_♦','A_♠','2_♥','2_♣','2_♦','2_♠','3_♥','3_♣','3_♦','3_♠',
          '4_♥','4_♣','4_♦','4_♠','5_♥','5_♣','5_♦','5_♠','6_♥','6_♣','6_♦','6_♠',
          '7_♥','7_♣','7_♦','7_♠','8_♥','8_♣','8_♦','8_♠','9_♥','9_♣','9_♦','9_♠',
          '10_♥','10_♣','10_♦','10_♠','J_♥','J_♣','J_♦','J_♠','Q_♥','Q_♣','Q_♦','Q_♠',
          'K_♥','K_♣','K_♦','K_♠']

def barajarMaso(a):
    random.shuffle(a)
    return a

def suma(seq):
    if (len(seq)== 0):
        return 0;
    else:
       return seq[0]+sum(seq[1:]);

def establecerSuma(a,b):
   b.clear();
   for x in a:
      if (x=="A_♥" or x=="A_♣" or x=="A_♦" or x=="A_♠"):
         if(suma(b[0:a.index(x)])>=10):
             b.append(1);
         elif(suma(b[0:a.index(x)])<10):
             b.append(11);
      else:
          b.append(definirValor(x));
   return suma(b);         
              
def definirValor(b):
    if any(s for s in b if "2_" in b):
        return 2;
    elif any(s for s in b if "3_" in b):
        return 3;
    elif any(s for s in b if "4_" in b):
        return 4;
    elif any(s for s in b if "5_" in b):
        return 5;
    elif any(s for s in b if "6_" in b):
        return 6;
    elif any(s for s in b if "7_" in b):
        return 7;
    elif any(s for s in b if "8_" in b):
        return 8;
    elif any(s for s in b if "9_" in b):
        return 9;
    elif any(s for s in b if "10_" in b):
        return 10;
    elif any(s for s in b if "J_" in b):
        return 11;
    elif any(s for s in b if "Q_" in b):
        return 12;
    elif any(s for s in b if "K_" in b):
        return 13;
    else:
        return 0;

def verificarMano(b,c):
   if (establecerSuma(b,[])>21):
      print("Te has pasado!! ... HAS PERDIDO   =(    ");
      print("Tu mano: ")
      print(b);
      print("mano de la casa: ")
      print(c)
      return "true";
   elif(establecerSuma(b,[])==21):
      print("Tienes 21!! ... HAS GANADO   =D    ");
      print("Tu mano: ")
      print(b);
      print("mano de la casa: ")
      print(c)
      return "true";   
   elif(establecerSuma(b,[])<21):
      print("Tu mano: ")
      print(b);
      return "false";   
     
def verificarManoCasa(c,b):
   if (establecerSuma(c,[])>21):
      print("La casa se ha pasado ... HAS GANADO   =D   ");
      print("Tu mano: ")
      print(b);
      print("mano de la casa: ")
      print(c)
      return "true";
   elif(establecerSuma(c,[])==21):
      print("La casa ha ganado ... HAS PERDIDO   =(   ");
      print("Tu mano: ")
      print(b);
      print("mano de la casa: ")
      print(c)
      return "true";   
   elif(establecerSuma(c,[])<21):
      return "false";  


def compararFinal(c,b):
   if(establecerSuma(c,[])>establecerSuma(b,[])):
      print("La casa ha ganado ... HAS PERDIDO   =(   ");
      print("Tu mano: ")
      print(b);
      print("mano de la casa: ")
      print(c)
   elif(establecerSuma(c,[])<establecerSuma(b,[])):
      print("La casa ha ganado ... HAS PERDIDO   =(   ");
      print("Tu mano: ")
      print(b);
      print("mano de la casa: ")
      print(c)
   elif(establecerSuma(c,[])==establecerSuma(b,[])):
      print(" ... HAN EMPATADO   =0   ");
      print("Tu mano: ")
      print(b);
      print("mano de la casa: ")
      print(c)

      

def jugar(a,b,c):
   if(len(b)==0 and len(c)==0):
      b.append(a[0]);
      c.append(a[1]);
      jugar(a[2:],b,c);
   else:
      print("Tu Mano : ");
      print(b);
      c.append(input("Desea otra carta? "));
      print("============================================");
      if('s' in c):
         c.remove("s");
         b.append(a[0]);
         if(verificarMano(b,c)=="false"):
             print("Se reparte otra carta a la casa.");
             c.append(a[1]);
             if(verificarManoCasa(c,b)=="false"):
                 jugar(a[2:],b,c);  
      elif('n' in c):
        c.remove("n");
        while(verificarManoCasa(c,b)=="false"):
            if(establecerSuma(c,[])<21 and establecerSuma(c,[])>17):
               compararFinal(c,b);
               break;
            else:   
               c.append(a[0]);
               a.remove(a[0]);
               print("Se reparte otra carta a la casa.");
     
                      

jugar(barajarMaso(retornarMaso()),[],[]);


      







