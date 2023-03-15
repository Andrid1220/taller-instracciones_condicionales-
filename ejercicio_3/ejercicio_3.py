# programa para determinar el precio de venta de un articulo 

print("-----------------------------")
print("------PRECIO DE VENTA--------")
print("-----------------------------")

# input

price = int(input("Ingrese el valor del costo del articulo: "))

#procesing

if price< 3000:
    g = (15*price)/100
    
else:
    if 3000 <= price <= 6000:
        g = 500
    else: 
      g = (25* price)/100

## procesing
p = price + g

#output
print(p)