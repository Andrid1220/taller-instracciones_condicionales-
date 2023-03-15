# programa para determinar si la suma de dos numeros es igual al tercero 

print("-------------------------")
print("---------IGUALDA---------")
print("-------------------------")

# input

a=int(input("No. 1: "))
b=int(input("No. 2: "))
c=int(input("No. 3: "))

# procesing

d=a+b

if d == c:
    rta= f"la suma de {a} y {b} es igual a {c}"
else:
    rta= f"la suma de {a} y {b} no son iguales a {c}"
# output 
print(rta)