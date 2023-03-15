# programa para determinar el costo del agua de una vivienda

print("----------------------")
print("-----GASTO DE AGUA----")
print("----------------------")

# input 
m= int(input("Ingrese el valor de los m3: "))

# procesing

if m<50:
    rta= f"Su costo es de: {10000}"
else:
    if 50<=m<200:
        rta = f"su costo es de: {2000+10000}"
    else:
        rta=f"su costo es de: {3000+10000}"
     

print(rta)