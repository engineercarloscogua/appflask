#modelo para las aplicaciones
#modelo para los posteos en la pagina web
from datetime import datetime # sus funciones permiten almacenar la fecha de la publicacion con el
from myblog import db # Importa la instancia de la base de datos desde el módulo myblog
# Define el modelo de la tabla 'posts' en la base de datos
class Post(db.Model): #hereda del modelo db de __init.py__ 
    #creando la tabla
    __tablename__ = 'posts'  # Define el nombre de la tabla en la base de datos
    # Define las columnas de la tabla
    id = db.Column(db.Integer, primary_key =True)
    #relación de 1 a muchos (1 autor puede tener muchas publicaciones)
    author = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) # Relación con la tabla de usuariosllamado de la ky de la tabla users
    title = db.Column(db.String(100))
    body = db.Column(db.Text)
    #fecha de ceración del posteo
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) #no acepta campos vacios o nulos, Fecha de creación del post
    
    #================ Constructor de la clase Post, recibe autor, título y cuerpo del post=========================
    # el contructor recibe una nombre de usuario y contraseña
    #en la representacion  __repr__ le pasamos la clase y el titulo  / Método para representar el objeto Post como una cadena    
    def __init__(self,author, title, body) -> None: 
        self.author = author
        self.title = title
        self.body = body
            
    
    def __repr__(self) -> str: 
        return f'Post: {self.title}'
    
    