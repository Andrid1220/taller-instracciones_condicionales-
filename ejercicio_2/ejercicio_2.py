# programa para prestamo bancario

print("-------------------------------")
print("------PRESTAMOS BANCARIO-------")
print("-------------------------------")

#input

plata = int(input("Digite el valor de sus ingresos: "))
deudas= int(input("Digite el numero de deudas: "))

#procesing

if plata>945200:
    if deudas>0:
        rta = "No cumples con los requisitos para prestamo, librate de deudas primero"
    else:
        if deudas == 0:
            rta= "cumples con los requisitos para un prestamo"
        else:
            rta = "No cumples con los requisitos"
else: 
    rta = "No cumples con los requisitos para prestamo"

#output
print(rta)