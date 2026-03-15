#1.Pedimos dos datos diferentes al usuario
tiene_licencia= input("¿Tienes licencia de conducir? (si/no):")
esta_ebrio = input("¿Has bebido alcohol hoy?(si/no):")
#2. Usamos and(Y). AMBAS  condiciones deben ser verad para entrar
if tiene_licencia== "si" and esta_ebrio=="no":
    print("Puedes conducir el vehiculo.")
else:
    print("Entreger las llaves. No puede conducir.")