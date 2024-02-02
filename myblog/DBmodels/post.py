#modelo para las aplicaciones

#modelo para los posteos en la pagina web
import datetime # sus funciones permiten almacenar la fecha de la publicacion con el
from myblog import db

# para crear un model se debe crear un modelo de DB
class Post(db.Model): #hereda del modelo db de __init.py__ 
    #creando la tabla
    __tablename__ = 'posts'  #nombre de la tabla
    #columnas de la tabla o atributos de la clases
    id = db.Column(db.Integer, primary_key =True)
    #relación de 1 a muchos (1 autor puede tener muchas publicaciones)
    author = db.Column(db.Integer, db.ForeigKey('users.id'),nullable= False) #llamado de la ky de la tabla users
    title = db.Column(db.String(100))
    body = db.Column(db.Text)
    #fecha de ceración del posteo
    created = db.Column(db.Datatime,nullable= False, default= datetime.utcnow) #no acepta campos vacios o nulos
    # contructor para poder reutilizar la clase, crear aplicaciones 
    # el contructor recibe una nombre de usuario y contraseña
    #en la representacion  __repr__ le pasamos la clase y el titulo
    
    #https://www.youtube.com/watch?v=JTAY5_LO0Ug  45:34
    def __init__(self,author, title, body) -> None: 
        self.author = author
        self.title = title
        self.body = body
            
        
    def __repr__(self) -> str:
        return f'Post: {self.title}'
    
    