import os 
from flask import Flask
from dotenv import load_dotenv
load_dotenv()
#[instanciación]
app=Flask(__name__)
#[encapsulamiento de configuracion]
app.config['SQLALCHEMY_DATABASE_URI']=os.getenv('DATABASE_URI','sqlite:///defau')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['JWT_SECRET_KEY']=os.getenv('JWT_SECRET_KEY','clave_insegura')
from models import db
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
#[acoplamiento]
db.init_app(app)
migrate=Migrate(app,db)
jwt=JWTManager(app)
if __name__=='__main__':
    puerto=int(os.getenv('PORT',5000))
    mode_debug=os.getenv('FLASK_DEBUG')=='True'
    app.run(port=puerto,debug=mode_debug)
#registrar el blueprint
from routes import api_bp 
app.register_blueprint(api_bp,url_prefix='/api')