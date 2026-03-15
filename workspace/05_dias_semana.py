dias_semana=("Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo")
#perdile al usario que ingrese un numero 
numero_elegido=int(input("Ingrese un numero de 0 al 6: "))
#mostar el dia semana utilizado el numero ingresado como indice 
print(f"El dia correspondiente es:{dias_semana[numero_elegido]}")