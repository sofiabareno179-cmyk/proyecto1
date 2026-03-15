print("Por favor, ingrese su contraseña:")
#pedir al usuario que iegite la contraseña
contraseña=input()
#Verifica si la contraseña es verdadera
if contraseña=="secreto123":
    #si es correcta saldra un me mensaje como Bienvenido al sistema
    print("Bienvenido al sistema")
else:
    #si no es correcta saldran intruso detectado
    print("Intruso detectado")
