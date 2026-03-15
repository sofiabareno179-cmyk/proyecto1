from flask_sqlalchemy import SQLAlchemy
#Instanciamos la herramienta vacía.Se acoplará a 'app' mas adelante.
db=SQLAlchemy()
#[HERENCIA]:L a clase 'usuario' hereda todo el poder de 'db.model'
class Usuario(db.Model):
    __tablename__='usuarios'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50),unique=True,nullable=False)
    #[ENCAPSULAMIENTO]:Nunca guardamos el password real,solo su representación
    password_hash=db.Column(db.String(55),nullable=False)
    rol=db.Column(db.String(20),default='Operario')
    #[POLIMORFISMO]:Método propio para transformar el objeto a JSON 
    def serializar(self)->dict:
        return{
            "id":self.id,
            "username":self.username,
            "rol":self.rol
        }
