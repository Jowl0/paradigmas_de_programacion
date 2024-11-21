#==============================================================
#   Del directorio aplicacion, el subdirectorio repositorio,
#   el archivo basededatos.py : trae el objeto Basededatos   
#==============================================================
from aplicacion.repositorio.basededatos import BaseDeDatos 

#==========================================================
#   Del archivo aplicacion, el subdirectorio repositorio 
#   el archivo s3.py : trea el objeto S3
#==========================================================
from aplicacion.repositorio.s3 import S3

#========================================================================
#   Del directorio aplicacion, el subdirectorio repositorio,
#   el archivo sistemadearchivos.py : trae el objeto SistemaDeArchivos
#========================================================================
from aplicacion.repositorio.sistemadearchivos import SistemaDeArchivos 

#==========================================================
#   Del directorio aplicacion, el subdirectorio modelos,
#   el archivo usuario.py : trae el objeto Usuario 
#==========================================================
from aplicacion.modelos.usuario import Usuario 

#================================================================================
#   Del directorio aplicacion, el subdirectorio negocios,
#   el archivo manejodeinscripciones.py : trae el objeto ManejoDeInscripciones
#================================================================================
from aplicacion.negocios.manejodeinscripciones import ManejoDeInscripciones

#=============================
#   Crear el objeto Usuario 
#============================= 
Usuario("Robeto","Jimenez",18)

#========================
#   Crear el objeto S3
#========================
repositorioS3 = S3("321221321","sdf324223","MiCubeta")

#=================================================================
#   Interface inscribirUsuario del objeto ManejoDeInscripciones
#=================================================================
ManejoDeInscripciones.inscribirUsuario(usuario,repositoriosS3)
print("\n")

#=========================================
#   Crear el objeto sistema de archivos 
#=========================================
repositorioSistemaDeArchivos = SistemaDeArchivos ("/home/users")

#=================================================================
#   Interface inscribirUsuario del objeto ManejoDeInscripciones
#=================================================================
ManejoDeInscripciones.inscribirUsuario(usuario,repositorioSistemaDeArchivos)
print("\n")

#=================================
#   Crear el objeto basededatos
#=================================
repositorioBaseDeDatos = BaseDeDatos("localhost","admin","admin123")

#==================================================================
#   Interface inscribirUsuario del obejeto ManejoDeInscripciones
#==================================================================
ManejoDeInscripciones.inscribirUsuario(usuario,repositorioBaseDeDatos)
print("\n")

