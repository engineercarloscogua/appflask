# Importa la clase Flask desde el módulo flask
#* No esta aquí pero es request, se puede importar y se usa para crear objetos que contiene información del cliente como IP, desde el navegador al servidor
#* make response permite Hacer una redireccion para el client en el servidor
from flask import Flask
# Importa la clase SQLAlchemy desde el módulo flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy 
# Crea una instancia de la aplicación Flask
app = Flask(__name__)

# Carga de configuraciones de la base de datos desde el archivo config.py
# Utiliza la clase DevelopmentConfig del archivo config.py para configurar la aplicación
app.config.from_object('config.DevelopmentConfig')

# Crea una instancia de SQLAlchemy y pasa la aplicación Flask como argumento
# para configurar la base de datos de la aplicación
db = SQLAlchemy(app)

# ------------------------------Registrando el Blueprint / Importar Vistas-----TODAS LAS VISTAS DEBEN REGISTRARSE AQUI-------------------------------
# Todos los blueprints o vistas deben ser registrados aquí para que la aplicación los reconozca
# Importa y registra el blueprint o vista llamado 'auth' desde el módulo myblog.Views.auth
from myblog.Views.auth import auth  
# Registra el blueprint 'auth' en la aplicación Flask
app.register_blueprint(auth) # Registra el blueprint 'auth' en la aplicación Flask
# Importa y registra el blueprint o vista llamado 'blog' desde el módulo myblog.Views.blog
from myblog.Views.blog import blog
app.register_blueprint(blog) # Registra el blueprint 'blog' en la aplicación Flask


#db.create_all() esto no va aqui se puso en main.py
# db.create_all() no debería estar aquí. Esto normalmente se llama desde el archivo main.py
# cuando se ejecuta la aplicación para crear las tablas en la base de datos.

# Este archivo inicializa la aplicación Flask, configura la base de datos y registra las vistas o blueprints.
# Es el punto de entrada de la aplicación donde se configuran todos los componentes principales.


