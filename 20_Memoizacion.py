#=================================
#  Joel Reyes Garcia
#=================================
#  Paradigmas de programacion
#  Matematica Algoritmica
#  ESFM-IPN  IPN
#=================================

#=================================
#   Recursividad y memorizacion 
#=================================

#====================================
#   Herramientas para memorizacion
#====================================
from functools import lru_cache

def fibonacci_lento(n):
    if n==1:
        return 1
    if n==2:
        return 1
    if n>2:
        return fibinnaci_lento(n-1) + fibonnaci_lento(n-2)

