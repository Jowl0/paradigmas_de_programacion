#==================================
#    Joel Reyes Garcia
#==================================
#    Matematica Algoritmica
#    ESFM IPN
#    Septiembre 2024
#==================================

#===================================
#   Importacion de modulos 
#   Contienen objetos y funciones
#===================================
import matplotlib.pyplot as grafica
import math

#=========================
#   Funcion exponencial 
#   Serie de Taylor
#   Polinomio en orden 
#=========================
def exponencial(n:int=1500, x:float=0.5):
    factoriala = 1.0
    exponencial_de_x = 1.0
    for i in range (1,n):
        x_a_la_n *= x 
        factorial *= float(i)
        s = 1.0/factorial 
        exponencial_de_x += s*x_a_la_n
    return exponencial_de_x

def exponencial_pro(n:int=1500,x:float=0.5):
    flag = False 
    if x < 0:
        flag = True
        x = -x
    s = 1.0
    for i in range(n,0,-1):
        s *= x/float(i)
        s += 1.0 
    if flag == True:
        s = 1/s
    return s 
m=400
serie = 250 
error1 = []
error2 = []
x0 = 0.0 
b = list(range(m))


