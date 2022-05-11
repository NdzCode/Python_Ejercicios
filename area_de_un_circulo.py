
r = float(input("ingresa el radio del circulo:" ))
pi = float(3.14)

#contrato: func main: float --> .float
#objetivo:Mediante r calcula el area del circula
#ej: Cuando el radio=3 el area =28.26
#ej: Cuando el radio=5 el area =78.50
#funcion:
# [assert] area circulo(1)==3.14
def main(r):
    return pi*r**2
ar = main(r)
print("El area del circulo es :"+ str("%1.2f" %ar))

if __name__=='__main__':
    main

# [Marcadores] - %1.2f" %ar s