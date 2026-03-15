#Avaces . nesecitamos tomar una decisión DENTRO de otra decisión.
print("---Diagnostico de red---")
hay_internet=input("¿El modem tiene luces encedidas?(si/no):")
if hay_internet=="si":
    print("paso 1:El equipo recibe energia.")
    #Este IF esta DENTRO del IF principal. solo se evalúa si el primero fue"si"
    luz_roja=input("¿Alguna de la luces es color ROJO (si/no)")
    if luz_roja=="si":
        print("Fallo detectado _Problema en la fibra optica. Llame a soporte.")
    else:
        print("Todo normal: Su conexion esta operando al 100%. ")
else: 
 print("Fallo critico:Verifique que el equipo esté conectado a la corriente.")
