#modelo para los ususarios
from myblog import db

# para crear un model se debe crear un modelo de DB
class User(db.Model): #hereda del modelo db de __init.py__ 
    #creando la tabla
    __tablename__ = 'users'  #nombre de la tabla
    #columnas de la tabla o atributos de la clases
    id = db.Column(db.Integer, primary_key =True)
    username = db.Column(db.String(50))
    password = db.Column(db.Text)
    
    # contructor para poder reutilizar la clase, crear usuarios 
    # el contructor recibe una nombre de usuario y contraseña
    def __init__(self,username, password) -> None: 
        self.username = username
        self.password = password
            
        
    def __repr__(self) -> str:
        return f'User: {self.username}'
    
    