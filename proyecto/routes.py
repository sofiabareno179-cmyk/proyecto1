from flask import Blueprint,request,jsonify,Response
from werkzeug.security import generate_password_hash,check_password_hash
from flask_jwt_extended import create_access_token,jwt_required,get_jwt_identity
from models import db,Usuario,Producto
api_bp=Blueprint('api',__name__)
@api_bp.route('/usuarios/registrar',methods=['POST'])
def registrar_usuarios(self)->tuple[Response,int]:
    try:
       payload=request.get_json()
       clave_segura=generate_password_hash(payload['password'])
       nuevo_user=Usuario(
           username=payload['username'],
           password_hash=clave_segura,
           rol=payload.get('rol','Operario')
       )
       db.session.add(nuevo_user)
       db.session.commit()
       return jsonify({"mensaje":"Exito","data":nuevo_user.serializar()}),200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error":"fallo de integridad","detalle":str(e)}),400
@api_bp.route('/usuarios/',methods=['GET'])
def lista_usuarios(self)->tuple[Response,int]:
    return jsonify()
@api_bp.route('/login',methods=['POST'])
def login()->tuple[Response,int]:
    payload=request.get_json()
    usuario=Usuario.query.filter_by(username=payload.get('username')).first()
    if Usuario and check_password_hash(usuario.password_hash,payload.get('password')):
        identidad={"username":usuario.username,"rol":usuario.rol}
        token_acceso=create_access_token(identity=identidad)
        return jsonify({"mensaje":"Login exitoso","token":token_acceso}),200
    return jsonify({"error":"crendeciales inválidas"}),401
@api_bp.route('/productos/registrar',methods=['POST'])
def registra_producto(self)->tuple[Response,int]:
    payload=request.get_json()
@api_bp.route('/productos/',methods=['GET']) 
def lista_productos(self)->tuple[Response,int]:
    return jsonify()
@api_bp.route('/inventario/producto',methods=['POST'])
def modificar_inventario()->tuple[Response,int]:
    usuario_actual=get_jwt_identity()
    if usuario_actual.get("rol") != "Admin":
        return jsonify({"error":"Forbidden:requiere privilegios de administrador"}),403
    return jsonify({
        "mensaje":"Acceso concebido.",
        "Operador":usuario_actual["username"]
    }),200