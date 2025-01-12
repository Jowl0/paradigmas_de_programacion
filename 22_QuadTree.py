#=================================
#  Joel Reyes Garcia
#=================================
#  Paradigmas de programacion
#  Matematica Algoritmica
#  ESFM-IPN  IPN
#=================================

#=======================
#   Paquetes externos 
#=======================
import random 
import matplotlib.pyplot as plt 
import matplotlib.patches as patches 

#=====================
#   Particula (x,y)
#=====================
class Particula():
    def __init__ (self, x:float, y:float):
        self.x = x
        self.y = y

#===========================================================================
#   Cajas para las particulas definidas por la esquina inferior izquierda
#   (x0,y0): esquina   (w,h): ancho y alto de la caja
#===========================================================================
class Nodo():
    def __init__(self, x0:float, y0:float, w:float, h:float,  particulas):
        self.x0 = x0
        self.y0 = y0
        self.ancho = w
        self.alto = h
        self.particulas = particulas 
        self.hijos = []

    def get_ancho(self):
        return self.ancho

    def get_alto(self):
        return self.alto

    def get_particulas(self):
        return self.particulas 

#====================================================
#   Funcion subdivision de cajas (en cuatro hijas)
#   se llama a si misma para seguir dividiendo
#   a las siguientes generaciones
#====================================================
def subdivison_recursiva(nodo:Nodo,k:int):
    if len(nodo.particulas)<=k:
        return 

    w_ = float(0.5* nodo.ancho)
    h_ = float(0.5* nodo.alto)

    p = cuantas_contiene(nodo.x0, nodo.y0, w_, h_, nodo.particulas)
    nodo.x1 = Nodo(nodo.x0, nodo.y0, w_, h_, p)
    subdivison_recursiva(nodo.x1, k)

    p = cuantas_contiene(nodo.x0, nodo.y0 + h_, w_, h_, nodo.particulas)
    nodo.x2 = Nodo(nodo.x0, nodo.y0 + h_, w_, h_, p)
    subdivison_recursiva(nodo.x2, k)

    p = cuantas_contiene(nodo.x0 + w_, nodo.y0, w_, h_, nodo.particulas)
    nodo.x3 = Nodo(nodo.x0 + w_, nodo.y0, w_, h_, p)
    subdivison_recursiva(nodo.x3, k)

    p = cuantas_contiene(nodo.x0 + w_, nodo.y0 + h_, w_, h_, nodo.particulas)
    nodo.x4 = Nodo(nodo.x0 + w_, nodo.y0 + h_, w_, h_, p)
    subdivison_recursiva(nodo.x4, k)


    nodo.hijos = [nodo.x1, nodo.x2, nodo.x3, nodo.x4]

#=================================================
#   Funcion para incluir particulas en una caja
#=================================================
def cuantas_contiene(x:float, y:float, w:float, h:float, particulas):
    pts=[]
    for particula in particulas:
        if particula.x >= x and particula.x <= x+w and particula.y >= y and particula.y <= y+h:
            pts.append(particula) 
    return pts 

#========================================
#   Funcion para encontrar cajas hijas
#========================================
def encontrar_hijos(nodo):
    if not nodo.hijos:
        return[nodo]
    else:
        hijos = []
        for hijo in nodo.hijos:
            hijos += (encontrar_hijos(hijo))
    return hijos 

#==============================================================
#   Objeto Quad tree es un arbol de cuatro ramas por nodo
#   para agrupar particulas en cajas y acelerar los calculos
#   con n particulas
#   Las cajas contienen maximo k particulas
#==============================================================
class QTree():
    def __init__(self, k:int, n:int):
        self.umbral = k
        self.particulas = [Particula(random.uniform(0,10), random.uniform(0,10)) for x in range(n)]
        self.root = Nodo(0, 0, 10, 10, self.particulas)

    def add_particula(self, x:float, y:float):
        self.particulas.append(Particula(x,y))

    def get_particulas(self):
        return self.particulas
    
    def subdividir(self):
        subdivison_recursiva(self.root, self.umbral)

    def visualizacion(self):
        fig = plt.figure(figsize= (12,8))
        plt.title("Quadtree")
        c = encontrar_hijos(self.root)
        print("Numero de segmentos. %d" %len(c))
        areas = set()
        for el in c:
            areas.add(el.ancho*el.ancho)
        print("Minima por segento: %.3f units" %min(areas))
        for n in c:
            plt.gcf().gca().add_patch(patches.Rectangle((n.x0, n.y0), n.ancho, n.alto, fill = False))
        x = [particula.x for particula in self.particulas]
        y = [particula.y for particula in self.particulas]
        plt.plot(x,y,"ro") # muestra las particulas como puntos rojos
        plt.show()
        return 

#========================
#   Programa principal
#========================
qtree = QTree(5,1000)
qtree.subdividir()
qtree.visualizacion()
