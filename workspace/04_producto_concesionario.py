#Crear una lista vacia llamada concesionario
concesionario=[]
#Agregarle un for para que se repita 3 veces pidiendo la marca, el modelo y el predion de un carro 
for datos in range (3):
  marca=str(input("Ingrese la marca del auto: " ))
  modelo=str(input("Ingrese el modelo del auto: "))
  precio=float(input("Ingrese el precio del auto: "))
  #Agregar esos datos en un diccionario temporal
  concesionario_temporal={
    "marca":marca,
    "modelo": modelo,
    "precio":precio
  }
  #Agregar esos datos a la lista concesionario
  concesionario.append(concesionario_temporal)
#Crear un segundo for para poder recorre la lista e imprimir esos datos
for vehiculo in concesionario:
  print(f"Vehiculo registrado:Marca {vehiculo['marca']},Modelo {vehiculo['modelo']},Precio ${vehiculo['precio']}.")


