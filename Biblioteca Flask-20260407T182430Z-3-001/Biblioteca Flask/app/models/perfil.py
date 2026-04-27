from flask import Flask 
from app import db
from io import BytesIO
import base64
import os
from flask import url_for, current_app
class Perfil (db.Model):
     __tablename__ ='perfil'
     id=db.Column(db.Integer,primary_key=True)
     bio=db.Column(db.String(100),unique=True,nullable=False)
     usuario_id  = db.Column(db.Integer, db.ForeignKey('user.idUser'), unique=True)
     def get_id(self):
        return str(self.id)
     def to_dict(self):
        return {
            "id": self.id,
            "bio": self.bio,
            "usuario_id": self.usuario_id
        }
     def save(self):
        db.session.add(self)
        db.session.commit()