#1. Variable GLOBAL (vive en el programa principal ,accesible por todos)
impuesto_nacional:float = 0.19
def calcular_descuento(precio:float)->float:
 #2. Variable LOCAL (vive SOLO durante este bloque de memoria)
 descuento_local:float =precio*0.10
 #La funcion SI puede leer variables Globales (hacia afuera)
 precio_con_impuesto:float=precio + (impuesto_nacional)
 return precio_con_impuesto-descuento_local
resultado:float=calcular_descuento(1000.0)
#3. ERROR: si intentas hacer print (descuento_local) aqui afuera, el programa col
#la variable 'descuento_local' ya fue destruida de la memoria RAM.
print(f"precio final:{resultado}")