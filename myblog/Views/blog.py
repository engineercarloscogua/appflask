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
def create():
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
#============================Actualizar una publicación ===========================
# funsión para obtener un posteo
def get_post(id, check_author= True):
    #consulta en la base de datos el id o retorna 404 si no existe
    post = Post.query.get(id) # Obtiene un postero por su ID desde la base de datos o devuelve un error 404 si no se encuentra
    #Condiciones para analizar el error
    if post is None:
        abort(404, f'id{id} de la pubñlicación no existe')        
    #Chequeando el autor si es distingo al id del autor 
    if check_author and post.author != g.user.id:
        abort(404)        
    
    return post #retorna el post

#===========edicioón ==============
# update_blog/<int:id> obteniendo el id en la url y conviertiendolo a entero
@blog.route('/blog/update_blog/<int:id>', methods=('GET','POST')) # mothods = ('GET', 'POST') DECORADOR DIRECCIONA LA RUTA Y PERMITE ENVIO TEXTO POR GET O HTML CON POST
@login_required # Requiere que el usuario esté autenticado para acceder a esta vista
def update(id):
    #verificando el envio de información con el metodo post usado en el Html register
    # Obteniendo el posteo
    post = get_post(id) #le elvia el id que esta recibiendo en el html para verificar el titulo y el cuerpo
    if request.method == 'POST':
        #Actualizando los datos del post obtenido
        post.title = request.form.get('title')
        post.body = request.form.get('body')
        #objeto del modelo User para enviar los valores a la BD definitivo con body encriptado
        #verificación de errores
        error = None
        #Verificando que los campos no esten vacios
        if not post.title:
            error = 'Se requiere agregar un titulo'
        if error is not None:  # Muestra el mensaje de error si hay alguno
            flash(error) #Mostrar el error 
        else:
            #registrar el titulo agregando los datos almacenandolos en post en la DB sql , # Registra el post en la base de datos
            db.session.add(post) #registra un nuevo objeto o sino solo actualiza
            db.session.commit()
            return redirect(url_for('blog.index')) # Redirige al usuario a la página de inicio            
        flash(error) #Muestra el mensaje de error si lo hay
    return render_template('blog/update_blog.html', post= post) #renderiza y envia un objeto posteo para actualizar cada campo
#==========Eliminar un posteo ==============================================================
@blog.route('/blog/delete/<int:id>') #recibe el id del objeto a eliminar 
@login_required # Requiere que el usuario esté autenticado para acceder a esta vista y eliminar
def delete(id): #recibe el id 
    post = get_post(id) #en post se almacena el id y arrastra la info del post en el onjeto
    db.session.delete(post) # elimina todos los datos del objeti post
    db.session.commit() # coemeter el cambio
    
    #redireccionar despues de eliminar
    return redirect(url_for('blog.index'))