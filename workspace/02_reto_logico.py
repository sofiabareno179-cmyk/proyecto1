#ingresar la estatura y la edad 
estatura=float(input("ingresa tu estatura "))
edad=int(input("ingrese tu edad "))
#comprobar si es mayor o igual a 12 y tener una estatura mayor o igual que 150cm  para o¿poder subirse en la montaña
if estatura>=150  and edad>=12:
    print("tiene el acceso permitido. Por favor ingrese")
else:
    print("ACCESO DENEGADO")