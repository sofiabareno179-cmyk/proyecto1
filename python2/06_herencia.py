#1. CLASE PADRE (superclase)
class Empleado:
    def __init__ (self,nombre:str,salario:float):
        self.nombre:str=nombre
        self.salario:float=salario
    def trabajar(self)->None:
        print(f"{self.nombre} esta cumpliendo su horario regular.")
#2.CLASE HIJO(subclase)-Hereda todo de Empleado pasándolo por paréntesis
class Desarrollador(Empleado):
    def programar(self)->None:
        print(f"{self.nombre} está escribiendo código Python.")
#3.CLASE HIJO CON POLIMORFISMO
class Gerente(Empleado):
    #Sobrescribe el metodo del Padre
    def trabajar(self)->None:
        print(f"{self.nombre} está en una reunión estratégica.")
#Pruebas de campo 
dev=Desarrollador("Carlos",3500.0)
jefe=Gerente("Ana",6000.0)
dev.trabajar()#Sube a RAM y usa el método del padre
dev.programar()#Usa su método propio
jefe.trabajar()# Usa su propio método sobrescrito(polimorfismo)
