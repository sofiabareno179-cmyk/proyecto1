mis_amigos=[]
#pedir los nombres y guadarlo en la lista
for i in range(1,4):
    nombre=input("ingresa el nombre de tu amigo ")
    mis_amigos.append(nombre)
#Imprime el mensaje de saludo personalizado con cada nombre
for nombre in mis_amigos:
        print(f"hola {nombre} espero que pase un excelente dia.")
        