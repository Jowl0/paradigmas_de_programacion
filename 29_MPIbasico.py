#=================================
#  Joel Reyes Garcia
#=================================
#  Paradigmas de programacion
#  Matematica Algoritmica
#  ESFM-IPN  IPN
#=================================

#===========================================================
#   OJO para correr se escribe
#   mpiexec -n 4 python3 27_mpibasico.py
#   o esto otro 
#   mpirun -n python3 27_mpibasico.py
#===========================================================
#   Pero si quieres a,s procesos que procesadores
#   mpirun --oversubscribe -n 400 python3 27_mpibasico.py
#===========================================================
#   Para correr 4 procesoss 
#===========================================================
from mpi4py import MPI 

#=================================
#   Crear un objeto comunicador 
#=================================
comunicadores = MPI.COMM_WORLD

#==============================
#   Numero total de procesos 
#==============================
n_procesos = comunicadores.Get_size()

#===================================
#   Identificador de este proceso
#===================================
quien_soy = comunicadores.Get_rank()

print("Saludos desde el proceso",str(quien_soy), "de ", str(n_procesos))

#=================================
#   Si yo soy el cero hago esto 
#=================================
if quien_soy == 0:
    print("Yo soy el proceso 0")

#================================
#   Si yo soy el uno hago esto 
#================================
elif quien_soy == 1:
    print("Yo soy el proceso 1")

#==============================================
#   Si yo no soy ni el uno nu el 2 hago esto 
#==============================================
else:
    print("Yo no soy ninguno de los 2 primeros procesos")

