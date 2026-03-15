from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()
class Usuario(db.Model):
    __tablename__='usuarios'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(40),unique=True,nullable=False)
    fecha_nacimiento=db.Column(db.Date,nullable=False)
    email=db.Column(db.String(80),unique=True,nullable=False)
   #[encapsulamiento]
    password_hash=db.Column(db.String(100),nullable=False)
    rol=db.Column(db.String(20),default='Operario')
    def serializar(self)->dict:
        return{
            "id":self.id,
            "username":self.username,
            "rol":self.rol
        }
class Producto(db.Model):
    __tablename__='producto'
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(40),nullable=False)
    precio=db.Column(db.Float,nullable=False)
    descripcion=db.Column(db.String(100),nullable=False)
    stock=db.Column(db.Integer,nullable=False)
    def serializar(self)->dict:
        return{
            "id":self.id,
            "nombre":self.nombre,
            "precio":self.precio,
            "descripcion":self.descripcion
        }