import os 
from flask import Flask
from dotenv import load_dotenv
#1.Cargamos el archivo .env a la memoria del Sistema Operativo
load_dotenv()
#2.[INSTANCIACIÓN]:Creamos el Orquestador Central
app=Flask(__name__)
#3.[ENCAPSULAMIENTO DE CONFIGURACIÓN]:Guardamos los secretos dentro de'app'
#Si la variable no existe en el .env, usamos un valor'fallback' por seguridad
app.config['SQLALCHEMY DATABASE URI']=os.getenv('DATABASE_URI','sqlite:///defa')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['JWT_SECRET_KEY']=os.getenv('JWT_SECRET_KEY','clave-insegura')
 #Agregar conectado moedels.py en app.py,debajo de las configuraciones 
from models import db
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
#[ACOPLAMIENTO]:Le pasamos el orquestador 'app' al ORM y utilidades
db.init_app(app)
migrate=Migrate(app,db)#Motor de migraciones
jwt=JWTManager(app)#Motor de seguridad jwt
#(En las siguiente fases conectaremos la Bases de Datos y la seguridad aqui)
if __name__=='__main__':
    #El archivo app.py es el unico que arranca el servidor
    puerto=int(os.getenv('PORT',5000))
    modo_debug=os.getenv('FLASK_DEBUG')=='True'
    app.rin(port=puerto,debug=modo_debug)
#blueprint
from routes import api_bp 
app.register_blueprint(api_bp,url_prefix='/api')