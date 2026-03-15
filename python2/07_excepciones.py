class CajeroAutomatico:
    def __init__(self):
        self.efectivo_disponible:float=10000.0
    def solicitar_retiro(self)->None:
        print(f"---Bienvenido al cajero---")
        #Bloque TRY:"Intentas hacer esto,pero estare alerta"
        try:
            monto_str=input("Ingresa la cantidad a retirar(solo números)")
            #Si el usuario ingresa letras,esta conversacion generará un ValueERROR
            monto:float= float(monto_str)
            #Si el usuario ingresa cero, lanzaremos nuestra propia excepcion lógica
            if monto == 0:
                raise ValueError("No se puede retirar cero pesos.")
            #Operación matemáticas (riesgo de dividir por ceros,etc.)
            self.efectivo_disponible-=monto
            print(f"Retiro exitoso. Quedan ${self.efectivo_disponible} en el cajero")
         #Bloque EXCEPT:"Si ocurre este error específico, no te apagues, haz esto
        except ValueError as e:
            print(f"ERROR DE FORMATO: Usted ingresó caracteres inválidos. ({e})")
        # Un exception general captura cualquier otro erro inesperado(como un f)
        except Exception as e:
            print(f"ERROR CRITICO DESCONOCIDO:contacte soporte.Detalles : {e}")
        #Bloque FINALLY :"se ejecuta SIEMPRE, haya ocurrido un error o no"
        finally:
            print("Expulsado tarjeta... Gracias por utilizar nuestra red ./n")
#Prueba
mi_cajero=CajeroAutomatico()
#Intentas ingresar letras como "Hola" en vez de numeros para probar la resiliencia
mi_cajero.solicitar_retiro()
