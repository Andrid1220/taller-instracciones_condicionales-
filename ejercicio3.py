precio_costo = float(input("Ingrese el precio de costo del artículo: "))

if precio_costo < 3000:
    ganancia = precio_costo * 0.15
elif precio_costo < 6000:
    ganancia = 500
else:
    ganancia = precio_costo * 0.25

precio_venta = precio_costo + ganancia

print(f"El precio de venta del artículo es: {precio_venta:.2f}")