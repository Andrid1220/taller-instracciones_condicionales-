# programa para determinar el cuadrante de una coordenada 

print("-----------------------------------")
print("-------UBICACION EN EL PLANO-------")
print("-----------------------------------")

# input

x = int(input("Digite el valor de x: "))
y = int(input("Digite el valor de y: "))

# procesing 

if x==0:
    if y==0:
        rta = (f"Los valores insertados se ubican en el origen, en los puntos: {(x,y)}")

    else:
        rta = (f"Los valores insertados se ubican en el eje y, en los puntos: {(x, y)}")
else:
    if y==0:
        rta = (f"Los valores insertados se ubican en el eje x, en los puntos: {(x, y)}")
    else:
        if x>0:
            if y>0:
                rta = (f"Los valores insertados se ubican en el cuadrante I, en los puntos: {(x, y)}")   
            else:
                rta = (f"Los valores insertados se ubican en el cuadrante IV, en los puntos: {(x, y)}")
        else:
            if y>0:
                rta = (f"Los valores insertados se ubican en el cuadrante II, en los puntos: {(x, y)}")
            else:
                rta = (f"Los valores insertados se ubican en el cuadrante III, en los puntos: {(x, y)}")


print(rta)