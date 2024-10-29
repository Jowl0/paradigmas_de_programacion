#=================================
#  Joel Reyes Garcia
#=================================
#  Paradigmas de programacion
#  Matematica Algoritmica
#  ESFM-IPN  IPN
#=================================

#======================================
#   Programacion orientada a objetos
#======================================

#====================================
#   Una clase para un objeto vacio 
#   No esta tan vacio, necesita 
#   La palabra pass = pasar
#====================================
class ObjetoVacio:
    pass 

#======================================================
#   nada es la instanciacion de la clase ObjetoVacio 
#======================================================
nada = ObjetoVacio()
print(type(nada)) 

#=====================
#   la clase llanta 
#=====================
class Llanta:
    #=========================================
    #   Variable cuenta es de toda la clase
    #=========================================
    cuenta = 0
    #=========================================
    #   funcion constructora de identidad 
    #   __init__ es una funcion reservada 
    #   comienza con uno mismo: self
    #   pero puede ser otro nombre (mi) 
    #   parametros de entrada = default 
    #=========================================
    def __init__(mi,radio=50,ancho=30,presion=1.5):
        #   variable de la estructura completa Llanta 
        Llanta.cuenta += 1
        #   variables exclusivas de cada objeto 
        mi.radio = radio 
        mi.ancho = ancho 
        mi.presion = presion 

#============================
#   Objeros (instanciados)
#============================
llanta1 = Llanta(50,30,1.5)
llanta2 = Llanta(presion = 1.2)
llanta3 = Llanta()
llanta4 = Llanta(40,30,1.6)

#=======================================
#   Objeto que contiene otros objetos
#=======================================
class Coche:
    def __init__(mi,ll1,ll2,ll3,ll4):
        mi.llanta1 = ll1
        mi.llanta2 = ll2
        mi.llanta3 = ll3
        mi.llanta4 = ll4

micoche = Coche(llanta1,llanta2,llanta3,llanta4)

print("Total de llantas: ", Llanta.cuenta) # Variable global de la clase
print("Presion de la llanta 4 = ", llanta4.presion) # Presion de la llanta 4
print("Radio de la llanta 4 = ", llanta4.radio)
print("Radio de la llanta 4 = ", llanta3.radio)
print("Persion de la llanta 1 de mi coche = ", micoche.llanta1.presion)


