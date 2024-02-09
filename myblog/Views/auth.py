# Este código es una implementación básica de un sistema de registro y inicio de sesión de usuarios utilizando Flask y SQLAlchemy.
from flask import(
    render_template, 
    Blueprint, 
    flash, 
    g, 
    redirect,
    request, 
    session, 
    url_for   
)
import functools
#libreria para encriptar claves
from werkzeug.security import check_password_hash, generate_password_hash
#importación del modelo usuario el cual crea la tabla dentro de la base de datos
from myblog.DBmodels.user import User
#importación de motor interno de BD sqlalchemy
from myblog import db
#creando Blue print / Crea todas las vistas
auth = Blueprint('auth', __name__, url_prefix= '/auth') #Url prefijo 

# =============================================Registrar Usuario==============================================
@auth.route('/register', methods=('GET','POST')) # mothods = ('GET', 'POST') DECORADOR DIRECCIONA LA RUTA Y PERMITE ENVIO TEXTO POR GET O HTML CON POST
def register():
    #verificando el envio de información con el metodo post usado en el Html register
    if request.method == 'POST':
        #capturando temporalmente los datos del formulario
        username = request.form.get('username')
        password = request.form.get('password')
        #objeto del modelo User para enviar los valores a la BD definitivo con password encriptado
        user = User(username, generate_password_hash(password)) # Crea un nuevo objeto usuario con contraseña encriptada.        
        #verificación de errores
        error = None
        #Verificando que los campos no esten vacios
        if not username:
            error = 'Se requiere nombre de usuario'
        elif not password:
            error = 'Sen requiere una Contraseña'
            # verificación de usuarios repetidos verifica como consulta en la BD comparando al primer usuario
        user_name = User.query.filter_by(username=username).first() 
        if user_name == None:
            #empezando a agregar nuevo registro a la base de datos con ayuda de sqlalchemy 
            db.session.add(user)  # Agrega el nuevo usuario a la sesión de la base de datos.
            #Aplicando el cambio
            db.session.commit() # Guarda los cambios en la base de datos.
            return redirect(url_for('auth.login')) # Redirecciona al usuario a la página de inicio de sesión.
            #si existe el mismo usuario
        else:
            error = f'El usuario {username} ya existe' #mensaje formateado
            flash(error) #captura el error y lo envia al HTML register
    return render_template('auth/register.html') # Renderiza la plantilla de registro.

# =================================== VISTA PARA EL LOGIN  INICIO DE SESION Vista para el inicio de sesión=======================
# Registrar Usuario
@auth.route('/login', methods=('GET','POST')) # mothods = ('GET', 'POST') DECORADOR DIRECCIONA LA RUTA Y PERMITE ENVIO TEXTO POR GET O HTML CON POST
def login():
    #verificando el envio de información con el metodo post usado en el Html login
    if request.method == 'POST':
        #capturando temporalmente los datos del formulario
        username = request.form.get('username')
        password = request.form.get('password')
        #verificación de errores
        error = None
        # Objetniendo el obeto de usuario
        user = User.query.filter_by(username = username).first() # Obtiene el usuario de la base de datos por su nombre de usuario.
        #Validando la existencia del Usuario
        if user == None:
            error = 'Nombre de usuario incorrecto'
        elif not check_password_hash(user.password, password): # Verifica si la contraseña ingresada coincide con la almacenada en la base de datos.
            error = 'Contraseña incorrecta'
        #Analisis del error
        if error is None:
            session.clear()
            #inicia la sesión / capura el el del usuario en la variable session
            session['user_id'] = user.id # Inicia la sesión del usuario
            #Redirección a la pagina principal
            return redirect(url_for('blog.index')) # Renderiza la plantilla de inicio de sesión.        
        flash(error) #captura el error y lo envia         
    return render_template('auth/login.html')

#=======FUNCIÓN PARA LA VERIFICACIÓN DEL LOGUEO DE USUSARIO /Función para cargar al usuario logueado antes de cualquier solicitud===========
#decorador de bluepirnt que permite que la función opere
@auth.before_app_request

def load_logged_in_user():
    #--- capturar el ud de un usuario si es logueado
    user_id = session.get('user_id') # Obtiene el usuario logueado.
    #--- si no esta logueado
    if user_id is None:
        #-- libreria g
        g.user = None
    else:
        #carga de usuario logueado y maneja error 404 si no lo encunetra
        g.user = User.query.get_or_404(user_id)

#=============================== FUNCIÓN PARA CERRAR SESIÓN LOGOUT =======================================================
@auth.route('/logout')
def logout():
    #cierrra la sesión
    session.clear() # Limpia la sesión del usuario.
    # Redirecciona al usuario a la página principal del blog.
    return redirect(url_for('blog.index'))

#=======VALIDACIÓN DE LOGEO PARA ACCEDER A VISTAS QUE REQUIEREN PERMISOS / Decorador para requerir inicio de sesión en ciertas vistas ==========
def login_required(view): #decora las vistas que necesitan logueo
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        #verificación de logeo
        if g.user is None:
            #redireccionar a login si no esta logueado
            return redirect(url_for('auth.login'))
        return view(**kwargs) # si el usuario esta lgueado delvuelve todos los argumentos
    # devuelve la función decorada
    return wrapped_view