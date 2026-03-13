#1.Salida estatica:El programa "habla" mostrando texto en pantalla 
print ("Iniciando sistema de diagnosticos..." )
#2.Asignacion de estado:guardando valores en la memoria (creando "cajas")
temperatura_cpu=45        #Guardamos un numero entero (Integer)
voltaje =1.2              #Guardamos un numero decimal(float)
estado_sistema ="Estable" #Guardamos texto (String-siempre entre comillas) 
#3.Recuperacion e interpolación(la letra 'f' antes de las comillas permite met)
print (f"Estado actual:{estado_sistema}")
print (f"Lecturas:{temperatura_cpu}°C a {voltaje}V")
#4.El flujo terminal cuando no hay mas lineas de codigo
print ("Diagnostico finalizado.")