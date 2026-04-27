from flask import Blueprint, render_template, request, redirect, url_for, jsonify, send_file,flash
from app.models.etiqueta import Etiqueta
from app import db
from io import BytesIO
import base64
import json

bp = Blueprint('etiqueta', __name__, url_prefix='/Etiqueta')


@bp.route('/')
def index():
    data = Etiqueta.query.all()
    return render_template('etiqueta/index.html', data=data)

@bp.route('/js')
def indexjs():
    data = Etiqueta.query.all()
        # Serializar los datos usando una comprensión de lista
    result = [etiqueta.to_dict() for etiqueta in data]
    # Devolver la respuesta JSON
    return jsonify(result)

@bp.route('/add', methods=['GET', 'POST'])
def add():
 if request.method == 'POST':
        nombre = request.form.get('nombre')
        slug = request.form.get('slug') 
        etiqueta_existente = Etiqueta.query.filter_by(slug=slug).first()
        
        if etiqueta_existente:
            flash("Error: El slug ya está en uso. Elige uno diferente.", "danger")
            return render_template('etiqueta/add.html')
        try:
            new_etiqueta = Etiqueta(nombre=nombre, slug=slug)
            db.session.add(new_etiqueta)
            db.session.commit()
            flash("Etiqueta creada con éxito", "success")
            return redirect(url_for('etiqueta.index'))
        except Exception as e:
            db.session.rollback()
            flash(f"Error: {str(e)}", "danger")
    
 return render_template('etiqueta/add.html')
  

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    etiqueta = Etiqueta.query.get_or_404(id)
    if request.method == 'POST':
         etiqueta.nombre = request.form.get('nombre')
         etiqueta.slug=request.form.get('slug')
         db.session.commit()
         flash("etiqueta actualizada", "info")
         return redirect(url_for('etiqueta.index'))

    return render_template('etiqueta/edit.html', etiqueta=etiqueta)
@bp.route('/detail/<int:id>')
def detail(id):
    etiqueta = Etiqueta.query.get_or_404(id)
    return render_template('etiqueta/detail.html', etiqueta=etiqueta)

@bp.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    etiqueta = Etiqueta.query.get_or_404(id)    
    db.session.delete(etiqueta)
    db.session.commit()
    return redirect(url_for('etiqueta.index'))