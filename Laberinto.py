#matriz = [list(linea)[-1] for linea in open("archivo.txt").readlines()]
matriz = [["y", 1, 1, 0],
          [ 0, 1, 0, 0 ],
          [ 1, 0, 1, 0 ],
          [ 1, 1, 0, 0 ],
          [ 0, 0, 0, 1 ],
          [ 0, 1,"x", 0]
          ];

class Nodo():
    def __init__(self,valor,posicion,hijos=[]):
        self.valor=valor
        self.posicion = posicion
        self.hijos=hijos

    def agregarHijo(self,hijo):
        self.hijos.append(hijo)
        
    def setPosicion(self,posicion):
        self.posicion=posicion

    def setHijos(self,hijos):
        self.hijos=hijos


def buscar(arbol,posicion):
    if arbol==None:
        return False
    if arbol.posicion==posicion:
        return True
    return buscar_hijos(arbol.hijos,posicion) 



def buscar_hijos(hijos,posicion):
    if hijos==[]:
        return False
    return buscar(hijos[0],posicion) or buscar_hijos(hijos[1:],posicion)



def buscarValor(arbol,valor):
    if arbol==None:
        return False
    if arbol.valor==valor:
        return True
    return buscar_hijosValor(arbol.hijos,valor) 


def buscar_hijosValor(hijos,valor):
    if hijos==[]:
        return False
    return buscarValor(hijos[0],valor) or buscar_hijosValor(hijos[1:],valor)


def imprimir(arbol):
    if(arbol==None):
        print("None")
    else:
        print(arbol.posicion)
        if(len(arbol.hijos)>0):
            for i in arbol.hijos:
                imprimir(i)     

def buscarX(lista):
   for x in lista:
       for y in range(len(x)):
           if x[y] == "x":
               colocarArbol(lista.index(x),y) 

raiz=Nodo(0,0,[])
arbol=Nodo(0,0,[])
def colocarArbol(x,y):
        raiz.setPosicion((x,y))
        arbol.setPosicion((x,y))
        raiz.setHijos([verificarIzquierda(x,y,arbol),verificarAbajo(x,y,arbol),verificarArriba(x,y,arbol),verificarDerecha(x,y,arbol)])

   

def verificarDerecha(x,y,nodo):
    print((x,y),"→")
    if(y+1<=len(matriz[x])-1 and matriz[x][y+1]!=1):
        if(buscar(nodo,(x,y+1))!=True):
            nodo.agregarHijo(Nodo(matriz[x][y+1],(x,y+1),[]))
            return Nodo(matriz[x][y+1],(x,y+1),[verificarAbajo(x,y+1,nodo),verificarArriba(x,y+1,nodo),verificarIzquierda(x,y+1,nodo),verificarDerecha(x,y+1,nodo)])
        else:
            return None
    else:
        return None
 
def verificarIzquierda(x,y,nodo):
    print((x,y),"←")
    if(y-1>=0 and matriz[x][y-1]!=1):
        if(buscar(nodo,(x,y-1))!=True):
            nodo.agregarHijo(Nodo(matriz[x][y-1],(x,y-1),[]))
            return Nodo(matriz[x][y-1],(x,y-1),[verificarAbajo(x,y-1,nodo),verificarArriba(x,y-1,nodo),verificarIzquierda(x,y-1,nodo),verificarDerecha(x,y-1,nodo)])
        else:
            return None
    else:
        return None
 
def verificarAbajo(x,y,nodo):
    print((x,y),"↓")
    if(x+1<=len(matriz)-1 and matriz[x+1][y]!=1):
        if(buscar(nodo,(x+1,y))!=True):
            nodo.agregarHijo(Nodo(matriz[x+1][y],(x+1,y),[]))
            return Nodo(matriz[x+1][y],(x+1,y),[verificarAbajo(x+1,y,nodo),verificarArriba(x+1,y,nodo),verificarIzquierda(x+1,y,nodo),verificarDerecha(x+1,y,nodo)])
        else:
            return None
    else:
        return None
 
def verificarArriba(x,y,nodo):
    print((x,y),"↑")
    if(x-1>=0 and matriz[x-1][y]!=1):
        if(buscar(nodo,(x-1,y))!=True):
            nodo.agregarHijo(Nodo(matriz[x-1][y],(x-1,y),[]))
            return Nodo(matriz[x-1][y],(x-1,y),[verificarAbajo(x-1,y,nodo),verificarArriba(x-1,y,nodo),verificarIzquierda(x-1,y,nodo),verificarDerecha(x-1,y,nodo)])
        else:
            return None
    else:
        return None
        
print(matriz[0])
print(matriz[1])
print(matriz[2])
print(matriz[3])
print(matriz[4])
print(matriz[5])

buscarX(matriz)

if(buscarValor(raiz,"y")==True):
    print("Si tiene solución")
else:
    print("No tiene solución")





