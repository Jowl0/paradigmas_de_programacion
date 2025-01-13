#=================================
#  Joel Reyes Garcia
#=================================
#  Paradigmas de programacion
#  Matematica Algoritmica
#  ESFM-IPN  IPN
#=================================

from mpi4py import MPI 
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

#===============================================
#   Se indica el tipo de datos explicitamente 
#   Este ejemplo solo tiene 2 procesos
#===============================================

#==============================
#   Ejemplo 1 usando enteros 
#==============================
if rank == 0:
    #===================================
    #   Arreglo de enteros del 0 al 9
    #===================================
    data = numpy.arange(10, dtype="i")
    #========================================================
    #   Envio bloqueante especificando el tipo del mensaje
    #   tag es un identificador del mensaje 
    #========================================================
    comm.Send([data, MPI.INT], dest=1, tag = 77)

elif rank == 1:
    data = numpy.empty(10,dtype="i")
    comm.Recv([data,MPI.INT], source = 0, tag = 77)
    print(data)

#===============================================================
#   Tambien se pudede sin decir el tipo de dato pero deben
#   coinicidir el tipo de arreglos de los extremos del mesaje
#===============================================================

#================================
#   Ejemplo 2 usando flotantes
#================================
if rank == 0:
    data = numpy.arange(10, dtype=numpy.float64)
    comm.Send(data, dest=1, tag=13)
elif rank == 1:
    data = numpy.empty(10, dtype=numpy.float64)
    comm.Recv(data, source = 0, tag = 13)
    print(data)
