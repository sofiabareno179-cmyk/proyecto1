#Creamos la clase Vehiculo 
class Vehiculo:
    def __init__ (self,marca:str,modelo:str,año:int):
        self.marca:str=marca
        self.modelo:str=modelo
        self.año:int=año
 #Crear dos ojectos para imprimir sus datos
mi_auto=Vehiculo("Audi","A3 sedan",2013)
ve_ca=Vehiculo("Chevrolet"," Blazer EV",2024)
# Salida de datos 
print(f"El vehiculo {mi_auto.marca},{mi_auto.modelo} y {mi_auto.año}")
print(f"El vehiculo {ve_ca.marca},{ve_ca.modelo} y {ve_ca.año}")

