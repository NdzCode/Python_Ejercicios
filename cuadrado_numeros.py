
"""Readmid_ Calcular el cuadrado de los numeros del  rango dado por el usuario """


def main():
    
    print("Bienvenido calculemos los cuadrados de los numeros") # Mensaje de bienvenida

    n1 = int(input("Ingresa un numero entero:"))                #Pedir desde donde comenzaremos 

    n2 = int(input("Ingresa un numero entero:"))                # donde terminaremos
    
    for x in range(n1,n2):                                      # for nos permite hacer una iteracion () --> 
                                                                #sirve para recorer una secuencia , ()podemos ingresar parametros
        print(x*x)                                              # Mientras recore multiplicara los numeros por si mismos hallando su cuadrado
        
    print("Eso es todo")                                        # Mensaje de termino
  


main()