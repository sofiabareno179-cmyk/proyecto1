#A veces nesecitamos saber exactamente  QUE tipo de dato tiene una caja
#Usamos la funcion type()para que python nos revele el secreto 
dato_desconocido ="100" # ¡Atencion! es un numero, pero esta entre comillas.Es
print (f"El dato es : {dato_desconocido} y su tipo es:{type(dato_desconocido)}")
#Conversion (casting): Transformado la caja de texto a numero (Integer)
dato_convertido =int(dato_desconocido)
print(f"Ahora el dato es:{dato_convertido} y su tipo es:{type(dato_convertido)}")
#Ahora si podemos hacer matematicas 
print(f"Suma matematicas real: {dato_convertido+50}")