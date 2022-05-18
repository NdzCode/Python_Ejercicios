a=int(input("ingresa la primera cantidad: "))
b=int(input("ingresa la segunda cantidad: "))
c=int(input("ingresa la tercera cantidad: "))

def  geo(a,b,c):
    y=float((a*b*c)**1/3)
    y =  round(y,3)
    return y

media = geo(a,b,c)

print("La media geometrica en : " +str(media) )


if __name__=='__main__':
    geo 