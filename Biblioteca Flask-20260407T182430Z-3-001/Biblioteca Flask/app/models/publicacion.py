from flask import Flask 
from app import db
from io import BytesIO
import base64
import os
from flask import url_for, current_app
publicacion_etiqueta = db.Table('publicacion_etiqueta',
    db.Column('publicacion_id', db.Integer, db.ForeignKey('publicacion.id'), primary_key=True),
    db.Column('etiqueta_id', db.Integer, db.ForeignKey('etiqueta.id'), primary_key=True)
)
class Publicacion(db.Model):
     __tablename__ ='publicacion'
     id=db.Column(db.Integer,primary_key=True)
     titulo=db.Column(db.String(100),unique=True,nullable=False)
     contenido=db.Column(db.String(250),unique=True,nullable=False)
     usuario_id  = db.Column(db.Integer, db.ForeignKey('user.idUser'), nullable=False)
     etiqueta = db.relationship('Etiqueta', secondary='publicacion_etiqueta', back_populates='publicaciones')
     def get_id(self):
        return str(self.id)
     def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "contenido":self.contenido,
            "usuario_id": self.usuario_id
        }
     def save(self):
        db.session.add(self)
        db.session.commit()