#Inicio
#Leer precio
# Leer Vip
#Si vip == "si" Entonces
#Precio = precio - (precio * 0.20)
#Fin Si
#Si precio > 500 Entonces
#descuento = precio * 0.10
#precio = precio - descuento
# Fin Si
#Si precio > 1000 Entonces
#descuento_adicional = precio * 0.15
#precio = precio - descuento_adicional
#Fin Si
#Mostrar "Precio final: ", precio
#Fin

precio = float(input("Ingrese el precio del videojuego: "))
vip = input("¿El cliente es VIP? (si/no): ").lower()

# Descuento VIP
if vip == "si":
    precio = precio - (precio * 0.20)

# Descuento por precio > 500
if precio > 500:
    precio = precio - (precio * 0.10)

# Descuento adicional por precio > 1000
if precio > 1000:
    precio = precio - (precio * 0.15)

print("Precio final a pagar:", precio)