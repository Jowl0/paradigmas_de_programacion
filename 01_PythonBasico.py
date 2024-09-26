#=================================
#  Joel Reyes Garcia
#=================================
#  Paradigmas de programacion
#  Matematica Algoritmica
#  ESFM-IPN  IPN
#=================================
''' Este es un super comentario
    De iniaio a nuestro resumen
'''
#=================================
#  Operaciones basicas
#=================================
print (2+3)
print (2*3)
print (2/3)
print (2**10)
print (2**0.5)  # raiz cuadrada
print (10%2)    
print (10%0.1)  # esxclusivo de python

#=================================================
#  Para saber el  tipo de objeto que se usa type
#=================================================
t=0
print(type(t)) # entero
t=3.6  
print(type(t)) # real (flotante)
t=True
print(type(t)) # booleano (bool) 

#====================== 
# Mensajes a pantalla
#====================== 
print ("Este es un comando de python. ", "Este es otro enunciado. ", t)
print('id: 1')
print('Nombres:', 'Steve')
print('Apellidos:', 'Jobs')
print('Vamos a sumar esto' + 'Con esto otro ')

#================================================
# Continuar una instruccion en varios renglones
#================================================
if 100 > 99 and \
	200 <= 300 and \
	True != False:
		print('¡Hola a todos!')

#==================================================
#  Usando parentesis redondos, cuadrados o llaves 
#  se puede escribir en varios renglones
#==================================================
lista = [1 ,2 ,3 ,4
       ,5 ,6 ,7 ,8
       ,9 ,10 ,11 ,12]

matriz = [ [1,2,3,4], [5,6,7,8], [9,10,11,12] ]

print(lista)
print(matriz)

#===================================================================
#  Identacion distinta para procesos dependientes de: (dos puntos)
#===================================================================
if 10>5:
	print("diez es mayor a cinco")
	print("otra identacion")
for i in lista:
	print (i)
	print("ok")
if 10>5:
	print("verdadero")
	if 10<20:
		print("verdadero")
elif 5>3: # Comienza segundo condicional
	print("esto no se imprimira")
else:
	print ("aqui nunca llega")

#=============
#  Funciones
#=============
def saludar(nombre):
	print("Hola", nombre)
	print("Bienvenido al tutorial de python")

saludar("Julian")
