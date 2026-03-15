print("Simulacion caja registradora")
acumuladora=0
for acumuladora in range(1,6):
 print("Ingrese el precio del producto")
 #ingrese los precios de 5 productoss
 precio=float(input())
 total=acumuladora+precio#suma el precio total de los precios ingresados
print(f"Costo total de la compra:{total}")
