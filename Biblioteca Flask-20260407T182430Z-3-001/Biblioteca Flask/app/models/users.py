from flask_login import UserMixin
from app import db
from datetime import datetime
from io import BytesIO
import base64
import os
from flask import url_for, current_app
from werkzeug.security import generate_password_hash,check_password_hash
class User(db.Model, UserMixin):
     __tablename__ ='user'
     idUser=db.Column(db.Integer,primary_key=True)
     nameUser=db.Column(db.String(100),unique=True,nullable=False)
     password_hash=db.Column(db.String(255),nullable=False)
     email=db.Column(db.String(150),unique=True,nullable=False)
     creado_en = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
     #relaciones 
     perfil=db.relationship('Perfil',backref="user",uselist=False,cascade='all, delete-orphan')
     publicacion=db.relationship('Publicacion',backref="user",lazy='dynamic',cascade='all, delete-orphan')
     def __init__(self, nameUser, email, password):
        self.nameUser = nameUser
        self.email = email
        self.set_password(password)
     def get_id(self):
        return str(self.idUser)
     def set_password(self, password):
        self.password_hash = generate_password_hash(password)
     def check_password(self, password):
        return check_password_hash(self.password_hash,password)
     def to_dict(self):
        return {
            "idUser": self.idUser,
            "nameUser": self.nameUser,
            "email": self.email,
            "creando_en":self.creado_en
        }
     def save(self):
        db.session.add(self)
        db.session.commit()