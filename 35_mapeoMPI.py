#=================================
#  Joel Reyes Garcia
#=================================
#  Paradigmas de programacion
#  Matematica Algoritmica
#  ESFM-IPN  IPN
#=================================

from mpi4py import MPI 
import  math 

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

#===========
#   Datos
#===========
n = 4
x = range(n)
m = int(math.ceil(float(len(x)) / size ))

#===============================================
#   Cada proceso tiene un pedazo de los datos 
#===============================================
x_chunk = list(x[rank*m:(rank+1)*m])
r_chunk = list(map(math.sqrt, x_chunk))

#=======================================================
#   Una sola lista de todos los datos en cada proceso 
#=======================================================
r = comm.allreduce(r_chunk)

#====================================================
#   Una matriz con todos los datos en cada proceso
#====================================================
rr = comm.allgather(r_chunk)

#======================================================
#   Una matriz con todos los datos para el proceso 1 
#======================================================
rrr = comm.gather(r_chunk, root = 1)

#=====================
#   Ver lo que paso 
#=====================
if rank == 0:
    print("Soy el 0 y esta es la reduccion de todos")
    print(r)
    print("Soy el 0 y esta es la coleccion de todos")
    print(rr)
    print("Soy el 0 y esta es la coleccion desde el 1")
    print(rrr)
if rank == 1:
    print("Soy el 1 y esta es la reduccion de todos")
    print(r)
    print("Soy el 1 y esta es la coleccion de todos")
    print(rr)
    print("Soy el 1 y esta es la coleccion desde el 1")
    print(rrr)
