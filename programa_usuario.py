
import modulo as nico

a=float(input("ingresa el valor del lado a del triangulo :"))
b=float(input("ingresa el valor del lado b del triangulo :"))
c=float(input("ingresa el valor del lado c del triangulo :"))

perimetro_u =nico.perimetro_angulo(a,b,c)

area_u = nico.area_angulo(a,b,c)

print(" ")

print("El perimetro del triangulo es: ", str(perimetro_u))

print(" ")

print("El area del triangulo es: ", str(area_u))
