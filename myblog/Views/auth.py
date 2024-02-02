#Registro de vistas
from flask import(
    render_template, Blueprint, flash, g, redirect, request, session, url_for   
)
#libreria para encriptar claves
from werkzeug.security import check_password_hash, generate_password_hash
#importación del modelo usuario el cual crea la tabla dentro de la base de datos
from myblog.DBmodels.user import User
#importación de motor interno de BD sqlalchemy
from myblog import db

#creando Blue print / Crea todas las vistas
auth = Blueprint('auth', __name__, url_prefix= '/auth') #Url prefijo 

# Registrar Usuario
@auth.route('/register', methods = ('GET','POST')) # mothods = ('GET', 'POST') DECORADOR DIRECCIONA LA RUTA Y PERMITE ENVIO TEXTO POR GET O HTML CON POST
def register():
    #verificando el envio de información con el metodo post usado en el Html register
    if request == 'POST':
        #capturando temporalmente los datos del formulario
        username = request.form.get('username')
        password = request.form.get('password')
        #objeto del modelo User para enviar los valores a la BD definitivo con password encriptado
        user = User(username,generate_password_hash(password))
        
        #verificación de errores
        error = None
        #Verificando que los campos no esten vacios
        if not username:
            error = 'Se requiere nombre de usuario'
        elif not password:
            error = 'Sen requiere una Contraseña'
            # verificación de usuarios repetidos verifica como consulta en la BD comparando al primer usuario
            user_name = User.query.filter_by(username=username).first()
            if username == None:
                #empezando a agregar nuevo registro a la base de datos con ayuda de sqlalchemy 
                db.session.add(user) #se envia el objeto el cual tiene usuario y clave encriptada
                #Aplicando el cambio
                db.session.commit()
                #si existe el mismo usuario
            else:
                error = f'El usuario {username} ya existe' #mensaje formateado
                flash(error) #captura el error y lo envia al HTML register
    return render_template('auth/register.html')