#1. Bucle for:Automatizando la repetición
#Range(1,6)genera los numeros de 1 al 6 (el ultimo numero no se incluye)
print("Inciando conteo automatico:")
for numero in range(1,6):
    #La variable 'numero ' cambia su valor automaticamente en cada vuelta
   print(f"paso actual:{numero}")
   #2. Iterando sobre un texto(cada letra es un paso)
   palabra_clave ="SENA"
   print(f"Deletreado la palabra{palabra_clave}:")
   for letra in palabra_clave:
      #Imprime una letra por cada vueltadel bucle
      print(f"letra detectada:{letra}")
       