from flask import Blueprint, render_template, request, redirect, url_for, jsonify, send_file,flash
from app.models.users import User
from app import db
from io import BytesIO
import base64
import json

bp = Blueprint('user', __name__, url_prefix='/User')

@bp.route('/')
def index():
    data = User.query.all()
    return render_template('users/index.html', data=data)

@bp.route('/js')
def indexjs():
    data = User.query.all()
        # Serializar los datos usando una comprensión de lista
    result = [user.to_dict() for user in data]  # Asegúrate de que el modelo User tenga un método to_dict()
    
    # Devolver la respuesta JSON
    return jsonify(result)

@bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nameUser = request.form['nameUser']
        password = request.form['passwordUser'] 
        email=request.form.get('email')   
        if User.query.filter_by(email=email).first():
            flash(f"El correo {email} ya está registrado.", "danger")
            return redirect(url_for('user.add'))    
     
        try:
            new_user = User(nameUser=nameUser, email=email,password=password)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            flash(f"Usuario {nameUser} creado con éxito.", "success")
            return redirect(url_for('user.index'))
        except Exception as e:
           db.session.rollback()
           flash(f"Error al crear usuario: {str(e)}", "danger")
        return redirect(url_for('user.add'))
    return render_template('users/add.html')

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    user = User.query.get_or_404(id)
    if request.method == 'POST':
        user.nameUser = request.form['nameUser']
        user.email = request.form['email']
        user.passwordUser = request.form['passwordUser']
        db.session.commit()        
        return redirect(url_for('user.index'))

    return render_template('users/edit.html', user=user)
@bp.route('/detail/<int:id>')
def detail(id):
    user = User.query.get_or_404(id)
    return render_template('users/detail.html', user=user)

@bp.route('/delete/<int:id>')
def delete(id):
    user = User.query.get_or_404(id)    
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('user.index'))


