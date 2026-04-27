from flask import Blueprint, render_template, request, redirect, url_for, jsonify, send_file,flash
from app.models.perfil import Perfil
from app import db
from flask_login import current_user
from io import BytesIO
import base64
import json

bp = Blueprint('perfil', __name__, url_prefix='/Perfil')


@bp.route('/')
def index():
    data = Perfil.query.all()
    return render_template('perfil/index.html', data=data)

@bp.route('/js')
def indexjs():
    data = Perfil.query.all()
        # Serializar los datos usando una comprensión de lista
    result = [perfil.to_dict() for perfil in data]  # Asegúrate de que el modelo User tenga un método to_dict()
    
    # Devolver la respuesta JSON
    return jsonify(result)
@bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        bio = request.form.get('bio')
        if not current_user.is_authenticated:
            flash("Debes iniciar sesión para crear un perfil", "warning")
            return redirect(url_for('auth.login'))
        try:
            new_perfil = Perfil(bio=bio, usuario_id=current_user.idUser)
            db.session.add(new_perfil)
            db.session.commit()
            flash("Perfil creado con éxito", "success")
            return redirect(url_for('perfil.index'))
        except Exception as e:
            db.session.rollback()
            flash(f"Error: {str(e)}", "danger")
            
    return render_template('perfil/add.html')

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    perfil = Perfil.query.get_or_404(id)
    if request.method == 'POST':
         perfil.bio = request.form.get('bio')
         db.session.commit()
         flash("Perfil actualizado", "info")
         return redirect(url_for('perfil.index'))

    return render_template('perfil/edit.html', perfil=perfil)
@bp.route('/detail/<int:id>')
def detail(id):
    perfil = Perfil.query.get_or_404(id)
    return render_template('perfil/detail.html', perfil=perfil)

@bp.route('/delete/<int:id>',methods=['POST'])
def delete(id):
    perfil = Perfil.query.get_or_404(id)    
    db.session.delete(perfil)
    db.session.commit()
    return redirect(url_for('perfil.index'))
