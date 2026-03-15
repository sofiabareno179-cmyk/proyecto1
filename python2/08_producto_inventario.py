#crea una clase llamada productos
class Producto:
    def __init__(self,nombre:str,precio:float,stock:int):
        self.nombre:str=nombre
        self.precio:float=precio
        self.stock:int=stock
    def vender(self,cantidad:int)->None:
        try:
            if cantidad>self.stock:
                raise ValueError("Stock insuficiente")
            self.stock-=cantidad
            print(f"Nuevo Stock:{self.stock}")
        except ValueError as e:
            print(f"Advertencia {e}:para el producto {self.nombre}")
class ProductoPerecederos(Producto):
    def __init__ (self,dias_vencimiento:int)->None:
        self.dias_vencimiento:int=dias_vencimiento
produ=Producto("Queso",5000.0,12)
produ_preced=ProductoPerecederos("06/03/2026")
produ.vender(4)
produ.vender(9)
