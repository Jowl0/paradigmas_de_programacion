#==================================
#    Joel Reyes Garcia
#==================================
#    Matematica Algoritmica
#    ESFM IPN
#    Septiembre 2024
#==================================

#==================
#   Condicionales
#==================
precio = 50
#-------------
#   Si esto
#-------------
if precio < 50:
    print ("El precio es menor que 50")
#------------------------------
#   Si no... si esto otro...
#------------------------------
elif precio > 50:
    print ("El precio es mayor a 50")
#-------------------------------
#   Si nada de lo anterior...
#-------------------------------
else:
    print("EL precio es 50")

precio = 50
cantidad = 5
total = precio*cantidad
#============================
#   Condicionales anidados
#============================
if total > 100:
    if total > 500:
        print("Total es mayor que 500")
    else:
        if total < 500 and total > 400:
            print("Total es menor que 500 pero mayor que 400")
        elif total < 500 and total > 300:
            print("Total entre 300 y 500")
        else:
            print("Total entre 100 y 300")
#------------------------------------
#   Condicional de igualdad son ==
#------------------------------------
elif total == 100:
    print("Total es 100")
else:
    print("Total es menor que 100")

#==================================================
#   Contador mientras la condicion sea verdadera
#==================================================
num = 0
while num < 5:
    num = num + 1
    print("num = ",num)

num = 0
while num < 5:
    num += 1                       # num += 1 es lo mismo de num = num + 1
    print("num = ", num)           # condicion antes de salir del bucle
    if num == 3:
        break

num = 0
while num < 5:
    num += 1
    if num > 1:
        continue                   # evitar lo que sigue, continuar con las iteraciones
    print("num = ", num)

#=======================
#   Bucle sobre lista
#=======================
nums = [ 10, 20, 30, 40, 50]
for i in nums:
    print(i)

#===========================
#   Bucle sobre un string
#===========================
for char in "Hola":
    print (char)

#================================
#   Bucle sobre un diccionario
#   items = elementos
#================================
numeros = {1:"uno" , 2:"dos", 3:"tres"}
for par in numeros.items():
    print(par)

#=============================
#   Bucle sobre diccionario
#   key = llave
#   value = valor
#============================
for k,v in numeros.items():
    print ("key  =", k , ", value = ", v) 

