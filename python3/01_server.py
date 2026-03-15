#1. Importamos la clase principal del framework 
from flask import Flask
#2. INSTANCIACIÓN:Creamos el objeto servidor.
#__name__ le dice a Flask dónde vuscar los archivos internos del proyecto.
app=Flask(__name__)
#3.ENRUTAMIENTO:El decorador '@' mapea una URL de red con una función en RAM.
@app.route('/',methods=['GET'])
def home()->str:
    """Función que se ejecuta cuando el cliente hace GET a la raíz del sitio."""
    return "<h1>Sistemas de Control Agroindustrial Activo</h1>"
#4.EJECUCIÓN DEL BUCLE DE ESCUCHA
if __name__=='__main__':
   #host='0.0.0.0' expone el servidor a todas las interfaces de tu red local
   #port=5000 es el puerto TCP asignado. debung=True reiniciando el server 
    print("Iniciando servidor en[http://127.0.0.1:5000](http://127.0.0.1_5000)")
    app.run(host='0.0.0.0',port=5000, debug=True)