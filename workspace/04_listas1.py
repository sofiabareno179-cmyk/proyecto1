carrito_compras=["Leche","Huevos","Pan"]
print(f"carrito inicial:{carrito_compras}")
#1. agregar al final (.append)
carrito_compras.append("Cafe")
print(f"Agregué Café:{carrito_compras}")
#2. Eliminar un elemento especifico(.remove)
carrito_compras.remove("Leche")
print(f"Quite la Leche:{carrito_compras}")
#3. Cambiar un elemento sabieno su posicion (cajon 0)
carrito_compras[0]="Huevos Campesinos"
print (f"Cambie los huevos normales:{carrito_compras}")