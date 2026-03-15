colores=["Rojo","Azul","Verde"]
#oedir al usuario que color no le gusta
print(f"usuario al observar la lista de colores:{colores} escriba cual no le gusta")
color=input()
#utilizar remove para eliminar el color que ingreso el usuario
colores.remove(color)
#mostrar la lista actualizada 
print(f"lista de colores:{colores}")