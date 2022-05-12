m =float(input("Ingresa la distancia recorrida del objeto :"))
s = float(input("Ingresa el tiempo trascurido:"))

"""Calculando La velocidad de un objeto"""
#
#metros float--> float 
#[metros] convertir de metros a Kilometros
#Ej: m=100 --> 0.1 
def metros(m):
    kl= m/1000
    return kl
#segundos float --> float
#m[segundos] s --> convertir a horas
#s=3600 --> 1
def segundos(s):
    hr= s/3600
    return hr
kl = metros(m)
hr = segundos(s)
#velocidad
#velocida:float ---> float 
#calcualar la velociddad en K/M
#Ej: velocidad(100,9.58) -->37.57
def velocida(kl,hr):
     velo = kl/hr
     return velo
print("La velocidad del objeto es :"+str(round(velocida(kl,hr),4))+" K/h")
#print("Version Precisa"+velocida(kl,hr))