#1. Definicion: '-> None' indica que esta función no devuelve datos a la memoria 
def saludar_usuario ()->None:
 """Imprime un mensaje de conexion estándar."""
 print("Iniciando conexión con el servidor...")
 print("Autenticacion exitosa.¡Bienvenido!")
 #2.Llamada (La ejecución): Pedirle a la función que haga su trabajo
 print("---Sistema Principal---")
 saludar_usuario()
 saludar_usuario()