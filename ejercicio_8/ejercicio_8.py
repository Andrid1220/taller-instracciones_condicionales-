# programa para determinar si dos numeros son multiplos del otro

print("----------------------------")
print("----------MULTIPLOS---------")
print("----------------------------")

# input

a=int(input("No.1: "))
b=int(input("No.2: "))

# procesing

c= a%b
if c == 0:
    d=b%a
    if d == 0:
        rta= f"{a} es igual a {b}"
    else:
        rta=f"{a} es multiplo de {b}"
else:
    d=b%a
    if d == 0:
        rta = f"{b} es multiplo de {a}"
    else:
        rta=f"{a} y {b} no son multiplos"
# output
print(rta)