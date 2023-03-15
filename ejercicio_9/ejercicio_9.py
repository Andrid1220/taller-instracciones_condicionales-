


lado_1= int(input("lado 1"))
lado_2= int(input("lado 2"))
lado_3= int(input("lado 3"))

# procesing
if(lado_1<lado_2):
    if lado_2<lado_3:
        c=lado_3
        a=lado_2
        b=lado_1
    else:
        c=lado_2
        a=lado_1
        b=lado_3
else:
    if lado_1<lado_3:
        c=lado_3
        a=lado_2
        b=lado_1
    else:
        c=lado_1
        a=lado_2
        b=lado_3

ce=c**2
otro=(a**2)+(b**2)

if ce==otro:
    rta="es un triangulo recto"
else:
    if ce<otro:
        rta= "agudo"
    else:
        rta="es un trinagulo obtuso"

print(rta)
    








