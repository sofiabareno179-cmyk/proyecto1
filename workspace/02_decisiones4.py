print("Por favor, ingrese su nota del examen")
#ingresar la nota del examen
nota_examen= int(input())
#verifica si es mayor o igual a 60
if nota_examen>=60:
    #si es mayor a 60 APROBO
    print("Aprobado")
else:
    #pero si es menor que 60 REPROBO
    print("Reprobado")