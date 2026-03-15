#1.Creación de una lista: Se usan corchetes[] y se separan por comas
inventario_frutas=["Manzana","Pera","Mango","Banana"]
#2. Accediendo a un elemento específico: ¡Los programadores empezamos a contar 
print(f"La primera fruta es:{inventario_frutas[0]}") #Imprime Manzana
print(f"La tercera fruta es:{inventario_frutas[2]}") #Imprime Mango
#La verdadera magia: Combinamos Listas y el ciclo for
print("---Imprimiendo viñetas automaticas---")
#Por cada'fruta' individual dentro de la lista 'inventario_frutas', has lo siguiente
for fruta in inventario_frutas:
    print(f"-{fruta} disponible en bodega.")