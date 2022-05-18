
import math
c=[1,2,3]

# Recibe una lista ----> float
# calcular el promedio de la lista 
#Ej: def promedio([1,2,3]) ------> 2.0
def promedio(x):
    p= sum(x)/len(x)
    return p

print("este es el promedio: "+str(promedio(c)))

# funcion recibe una lista  ----> float 
# calcula la desviacion estandar de un lista de elemntos 
#Ej: def desviacion ([1,2,3]) -----> 0,81.....
def desviacion_e(x):
    d = 0
    for i in x:
        d += (i-promedio(x))**2
    return (d/len(x))**0.5

output_1= print("este es la desviacion Estandar : "+ str(desviacion_e(c)))

