import os
from flask import Flask,jsonify,Response,request
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()
app=Flask(__name__)
CORS(app)
class Producto:
    def __init__(self):
        self._productos:list[dict]=[]
    def agregar_producto(self,tipo:str,nombre:str)->dict:
        produ={"id":len(self._productos)+1,"tipo":tipo,"nombre":nombre}
        self._productos.append(produ)
        return produ
    def obtener_productos(self)->list[dict]:
        return self._productos
produc=Producto()
@app.route('/api/productos',methods=['GET'])
def ver_productos()->tuple[Response,int]:
    datos_producto=produc.obtener_productos()
    return jsonify({"productos":datos_producto}),200
@app.route('/api/productos',methods=['POST'])
def agregar_producto()->tuple[Response,int]:
    try:
        payload=request.get_json()
        nuevo_producto=produc.agregar_producto(payload["tipo"],payload["nombre"])
        return jsonify({"mensaje":"producto registrado","data":nuevo_producto}),201
    except KeyError:
       return jsonify({"error":"estructura json invalida."}),400
if __name__=='__main__':
      app.run(port=int(os.getenv("PORT",5000)),debug=os.getenv("FLASK_DEBUG")=="1")
