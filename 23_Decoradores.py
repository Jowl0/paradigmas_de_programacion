#=================================
#  Joel Reyes Garcia
#=================================
#  Paradigmas de programacion
#  Matematica Algoritmica
#  ESFM-IPN  IPN
#=================================

#======================================
#   Funcion que regresa otra funcion
#======================================
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase 
    return wrapper 

#====================
#   Funcion saludo
#====================
def say_hi():
    return "Hello there"

#==============================
#   Generar y correr funcion
#==============================
decorate = uppercase_decorator(say_hi)
print(decorate())

#=============================
#   Utilizar como decorador 
#=============================
@uppercase_decorator
def say_hi():
    return "hello there"

#==================================
#   Correr funcion por decorador 
#==================================
print(say_hi())
