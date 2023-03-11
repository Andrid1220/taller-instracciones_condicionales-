# programa que lea las cordenadas cartesianas (x,y)

# input

x = int(input("Ingrese la coordenada x: "))
y = int(input("Ingrese la coordenada y: "))

# procesing

if x > 0 and y > 0:
    print("El punto está en el primer cuadrante.")
elif x < 0 and y > 0:
    print("El punto está en el segundo cuadrante.")
elif x < 0 and y < 0:
    print("El punto está en el tercer cuadrante.")
elif x > 0 and y < 0:
    print("El punto está en el cuarto cuadrante.")
elif x == 0 and y == 0:
    print("El punto está en el origen.")
elif x == 0:
    print("El punto está sobre el eje y.")
else:
    print("El punto está sobre el eje x.")