from flask import (
    render_template, # renderizza rtemplate
    Blueprint, # regirtrar la vista
    flash, # muestra mensajes flash
    g, # verificacion de logueos, objeto global para manejar datos de la solicitud
    redirect, # redireccionar, redirige a otra ruta
    request,  # obtener todos los registros, obtiene datos de la solicitud HTTP
    url_for # genera URLs para las rutas
)
# Importaciones de modelos y funciones de autenticación
#manejo de erroe, maneja excepciones HTTP
from werkzeug.exceptions import abort
# imprtando las BD de usuario y de publicacion de poster
from myblog.DBmodels.post import Post # Importa el modelo de Post desde el paquete 'myblog.models.post'
from myblog.DBmodels.user import User # Importa el modelo de User desde el paquete 'myblog.models.user'

#llamando función de auth para verificar logeuo
from myblog.Views.auth import login_required  # Importa la función 'login_required' desde el paquete 'myblog.views.auth'
#configuración a la conexion de la DB
from myblog import db  # Importa la instancia de la base de datos 'db' desde el paquete 'myblog'

# Crea un Blueprint llamado 'blog'
blog = Blueprint('blog', __name__)

#==================================== Función para obtener un usuario por su ID ==========================================
def get_user(id):
    #consulta en la base de datos el id o retorna 404 si no existe
    user = User.query.get_or_404(id) # Obtiene un usuario por su ID desde la base de datos o devuelve un error 404 si no se encuentra
    return user #retorna el usuario obtenido

#====================================Vista para la página de inicio =====================================================
#decorando que todo empiece desde el inicio
@blog.route("/") #La decoración @blog.route("/") se utiliza en Flask para asociar una función (en este caso, la función index()) con una ruta específica de la aplicación web.
def index():
    # Obtiene todos los posts desde la base de datos
    posts = Post.query.all()
    # Invierte el orden de los posts obtenidos para mostrar los más recientes primero
    
    #enviando la consulta a la DB
    db.session.commit()  # Confirma los cambios en la sesión de la base de datos (no debería ser necesario aquí)
    #renderizando el templagte   -estas variables son las que van a ser iteradas en el for en los templates del index
    # Renderiza la plantilla 'blog/index.html' con los posts y la función get_user disponibles
    return render_template('blog/index.html', posts = posts, get_user=get_user) #retornando los datos en un diccionario (clave:contenido)

#====================================Vista para crear un nuevo post =======================================================
@blog.route('/blog/create_blog', methods=('GET','POST')) # mothods = ('GET', 'POST') DECORADOR DIRECCIONA LA RUTA Y PERMITE ENVIO TEXTO POR GET O HTML CON POST
@login_required # Requiere que el usuario esté autenticado para acceder a esta vista
def register():
    #verificando el envio de información con el metodo post usado en el Html register
    if request.method == 'POST':
        #capturando temporalmente los datos del formulario
        title = request.form.get('title')
        body = request.form.get('body')
        #objeto del modelo User para enviar los valores a la BD definitivo con body encriptado
        
        # Crea un objeto del modelo Post con los datos del formulario
        posts = Post(g.user.id , title, body)         
        #verificación de errores
        error = None
        #Verificando que los campos no esten vacios
        if not title:
            error = 'Se requiere agregar un titulo'
        if error is not None:  # Muestra el mensaje de error si hay alguno
            flash(error) #Mostrar el error 
        else:
            #registrar el titulo agregando los datos almacenandolos en post en la DB sql , # Registra el post en la base de datos
            db.session.add(posts)
            db.session.commit()
            return redirect(url_for('blog.index')) # Redirige al usuario a la página de inicio            
        flash(error) #Muestra el mensaje de error si lo hay
    return render_template('blog/create_blog.html') # Renderiza la plantilla 'blog/create_blog.html' para el formulario de creación de posts
