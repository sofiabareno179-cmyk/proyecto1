#Crear una clase MascotaVirtual
class  MascotaVirtual:
    def __init__ (self,nombre:str,energia:int =10):
        self.nombre:str=nombre
        self.energia:int=energia
    #Creacion de metodos 
    def jugar (self,jugando:int=3)->None:
      self.energia-=jugando
      print(f"{self.nombre} le queda de energia: {self.energia}")
    def dormir (self,durmiendo:int=5)->None:
       self.energia+=durmiendo
       print(f"{self.nombre} esta durmiendo. Tienes de energia:{self.energia}")
mascota=MascotaVirtual("Toby")
mascota.jugar()
mascota.dormir()     

    
