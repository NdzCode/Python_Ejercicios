
r_1 = float(input("ingresa el radio exterior de anillo:"))
r_2=float(input("ingresa el radio interir del anillo:"))
pi = 3.14
"""Area de un anillo"""
# func-area:float -->  float
#calcula el area del anillo mediate, el area exterior - interior 
#Ej: r_1=4 , r_2= 2 --> 37.68
def area(r_1,r_2):
    amay= pi*r_1**2
    amen=pi*r_2**2
    return amay - amen

print("El area del anillo es : "+ str(round(area(r_1,r_2),2)))


if __name__=='__main__':
    area
    

