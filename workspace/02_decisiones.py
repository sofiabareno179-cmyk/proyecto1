#1.Entrada de datos: El programa se pausa y espera a que el usuario escriba algo
#Nota:input()siempre guarda texto. Si queremos numeros, lo lo envolvemos en int()
edad_usuario = int(input("por favor, ingresa tu edad en numeros: "))
#2.Evaluacion lógica: El programa analiza el dato ingresado
print ("Evaluando permisos de acceso...")
#3.Bifurcación(if/elif/else): El codigo toma un solo camino
if edad_usuario>=18:
    #Si la condición es VERDADERA, entra a este bloque
    print("acceso concedid: Eres mayor de edad.")
elif edad_usuario>=13:
    #si la de arriba fue falsa,pero esta es la VERDADERA entra aqui
    print("acceso restringido: Eres adolescente, nesecitas pernisos de un tutor ")
else:
     #si NINGUNA de las anteriores fue la verdadera, por descarte entra aqui
     print ("acceso denegado:Eres menor de edad.")
     #4.Esta linea no tiene espacios a la izquierda, asi que se ejecuta SIEMPRE
print("Gracias por usar el sistema.")