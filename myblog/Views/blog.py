from flask import (
    render_template, # renderizza rtemplate
    Blueprint, # regirtrar la vista
    flash, #
    g, # verificacion de logueos
    redirect, # redireccionar
    request,  # obtener todos los registros
    url_for 
)
#manejo de erroe
from werkzeug.exceptions import abort
# imprtando las BD de usuario y de publicacion de poster
from myblog.DBmodels.post import Post
from myblog.DBmodels.user import User

#llamando función de auth para verificar logeuo
from myblog.Views.auth import login_required
#configuración a la conexion de la DB
from myblog import db  

#regtrando el blueprint
blog = Blueprint('blog', __name__)

#---------FUNSION PARA OBTENER EL NOMBRE DE UN USUARIO MEDIANTE EL ID-----------------
def get_user(id):
    #consulta en la base de datos el id o retorna 404 si no existe
    user = User.query.get_or_404(id)
    return user #retorna el usuario obtenido

#---------LISTADO DE TODAS LAS PUBLICACIONES -------------------
#decorando que todo empiece desde el inicio
@blog.route("/")
def index():
    #recuperar todas las publicaciones
    posts = Post.query.all()
    #enviando la consulta a la DB
    db.session.commit()
    #renderizando el templagte   -estas variables son las que van a ser iteradas en el for en los templates del index
    return render_template('blog/index.html', posts = posts, get_user=get_user) #retornando los datos en un diccionario (clave:contenido)

#-------REGISTRAR O PUBLICAR -----------una copia base de user register-----------------------

@blog.route('/blog/create_blog', methods=('GET','POST')) # mothods = ('GET', 'POST') DECORADOR DIRECCIONA LA RUTA Y PERMITE ENVIO TEXTO POR GET O HTML CON POST
@login_required #requerir que el usuario este logueado
def register():
    #verificando el envio de información con el metodo post usado en el Html register
    if request.method == 'POST':
        #capturando temporalmente los datos del formulario
        title = request.form.get('title')
        body = request.form.get('body')
        #objeto del modelo User para enviar los valores a la BD definitivo con body encriptado
        
        #variable que contiene el post importado envia el id el titutlo y el cuerpo
        posts = Post(g.user.id , title, body) 
        
        #verificación de errores
        error = None
        #Verificando que los campos no esten vacios
        if not title:
            error = 'Se requiere agregar un titulo'
        if error is not None:
            flash(error) #Mostrar el error 
        else:
            #registrar el titulo agregando los datos almacenandolos en post en la DB sql
            db.session.add(posts)
            db.session.commit()
            return redirect(url_for('blog.index'))
            
        flash(error) #devuelve un error en caso de exitir
    return render_template('blog/create_blog.html')
