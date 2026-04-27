from flask import Flask 
from app import db
from io import BytesIO
import base64
import os
from flask import url_for, current_app
class Etiqueta(db.Model):
    __tablename__='etiqueta'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    slug = db.Column(db.String(50), unique=True)
    publicaciones = db.relationship('Publicacion', secondary='publicacion_etiqueta',back_populates='etiqueta')
    def get_id(self):
        return str(self.id)
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "slug": self.slug
        }
    def save(self):
        db.session.add(self)
        db.session.commit()