#modelo para los ususarios
from myblog import db # Importa la instancia de la base de datos desde el módulo myblog

# Define el modelo de la tabla 'users' en la base de datos
class User(db.Model): #hereda del modelo db de __init.py__ 
    # Define el nombre de la tabla en la base de datos
    __tablename__ = 'users'  #nombre de la tabla
    # Define las columnas de la tabla
    id = db.Column(db.Integer, primary_key=True) # Define la columna 'id' como clave primaria de tipo entero en la tabla de la base de datos.
    username = db.Column(db.String(50))
    password = db.Column(db.Text)
    
    # contructor para poder reutilizar la clase, crear usuarios / # Constructor de la clase User, recibe nombre de usuario y contraseña
    # el contructor recibe una nombre de usuario y contraseña
    # El constructor __init__ inicializa los atributos de la clase con los valores proporcionados
    # __reor__ define cómo se representa el objeto User como una cadena. En este caso, muestra el nombre de usuario.
    def __init__(self,username, password) -> None:  
        self.username = username
        self.password = password
                
    def __repr__(self) -> str:
        return f'User: {self.username}'
            
        
    
    
    