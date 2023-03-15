# programa para identificar el indice de masa corporal 

print("-------------------------------------")
print("------INDICE DE MASA CORPORAL--------")
print("-------------------------------------")


#intput

p = int(input("ingrese el valor del peso en kg: "))
a = float(input("ingrese el valor de la altura en m: "))

# procesing 1

imc = p/(a**2)

# procesing 2

if imc<16:
    rta= "Criterio de ingreso al hospital"
else:
    if 16<=imc<17:
        rta = "infrapeso"
    else:
        if 17<=imc<18:
            rta= "Bajo peso"
        else:
            if 18<=imc<25:
                rta="peso normal (saludable)"
            else:
                if 25<=imc<30:
                    rta= "Sobrepeso (obesidad grado I)"
                else:
                    if 30<=imc<35:
                        rta= "Sobrepeso cronico (obesidad grado II)"
                    else:
                        if 35<=imc<40:
                            rta="Obesidad premorbida (obesidad grado III)"
                        else:
                            rta= "Obesidad morbida (obesidad de grado IV)"
print(rta)
 


