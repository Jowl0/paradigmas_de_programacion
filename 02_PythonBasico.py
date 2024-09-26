#==================================
#    Joel Reyes Garcia
#==================================
#    Matematica Algoritmica
#    ESFM IPN
#    Septiembre 2024
#==================================

#=========================================================
#    Imput permite obtener datos del usario en prompter
#=========================================================
nombre = input("Dame nu nombre: ")
print("Hola como estas" ,nombre)

#============================================
#   Los enteros son de precision ilimitada
#============================================
y = 500000000000000000000000000000000000
print(y)

#=================================================================
#   Se pueden delimitar numeros con guion bajo pero no con coma
#=================================================================
y = 5_000_0000
print(y)

#========================================================
#   La funcion int() cambia strings y floats a enteros
#========================================================
numero = int(input("Dame tu edad: "))
type(numero)

#=======================================================
#   La notacion cientifica de flotantes utiliza e o E
#=======================================================
#   1.2 x 10^{-9}
#===================
y = 1.2E-09
print (y)

#=============================================================
#   La funcion float() convierte strings y enteros a floats
#=============================================================
y = float ("14.3")
print (y)

#=========================================================
#   Los complejos se escriben como la raiz de menos uno
#   j siempre con un numero como prefijo
#   no acepta la j suelta 
#=========================================================
z=1+1j

#   suma +
#   resta -
#   multiplicacion *
#   division / 
#   modulo %
#   exponente **
#   // funcion piso 
#   Funciones para transformar numeros int() float() complex()
#   Operaciones abs() round () pow()

print(round(3.14159,4))

#==============================
#   Strings de varias lineas
#==============================
parrafo = """ Eb el bosque de la china
la chinita se perdio """
print (parrafo)

#===================================================
#   La funcion len() obtiene el tamaño del string
#===================================================
n = len(parrafo)
print(n)

#================================================================
#   Las letras en un string ocupan lugares como en un arreglo)
#   (tambien de atras para adelante comenzando en -1 el ultimo)
#================================================================
palabra = "hola"
print(palabra[0])
print(palabra[-4])

