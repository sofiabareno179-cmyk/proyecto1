from flask import Blueprint, render_template, request, redirect, url_for, jsonify, send_file,flash
from app.models.publicacion import Publicacion
from app import db
from io import BytesIO
import base64
import json

bp = Blueprint('publicacion', __name__, url_prefix='/Publicacion')


@bp.route('/')
def index():
    data = Publicacion.query.all()
    return render_template('publicacion/index.html', data=data)

@bp.route('/js')
def indexjs():
    data = Publicacion.query.all()
    result = [publicacion.to_dict() for publicacion in data] 
    
    # Devolver la respuesta JSON
    return jsonify(result)
@bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        contenido = request.form.get('contenido') 
        
        try:
            new_publicacion = Publicacion(titulo=titulo, contenido=contenido,usuario_id=1)
            db.session.add(new_publicacion)
            db.session.commit()
            flash("publicacion creada con éxito", "success")
            return redirect(url_for('publicacion.index'))
        except Exception as e:
            db.session.rollback()
            flash(f"Error: {str(e)}", "danger")

    return render_template('publicacion/add.html')


@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    publicacion = Publicacion.query.get_or_404(id)
    if request.method == 'POST':
         publicacion.titulo = request.form.get('titulo')
         publicacion.contenido=request.form.get('contenido')
         db.session.commit()
         flash("publicacion actualizada", "info")
         return redirect(url_for('publicacion.index'))

    return render_template('publicacion/edit.html', publicacion=publicacion)
@bp.route('/detail/<int:id>')
def detail(id):
    publicacion = Publicacion.query.get_or_404(id)
    return render_template('publicacion/detail.html', publicacion=publicacion)

@bp.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    publicacion = Publicacion.query.get_or_404(id)    
    db.session.delete(publicacion)
    db.session.commit()
    return redirect(url_for('publicacion.index'))