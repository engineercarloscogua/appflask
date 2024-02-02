from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

#Carga de Configuraciones de la BD del archivo config.py
# from object se usa porque se esta trabajando clases en este caso el modo desarrollo class DevelopmentConfig
app.config.from_object('config.DevelopmentConfig')

# variable que refleja la BD  mysql de la app
db = SQLAlchemy(app)

# Registrando el Blueprint / Importar Vistas
#importando el prue print o vista llamado auth
from myblog.Views.auth import auth  
#registrando la vista
app.register_blueprint(auth) 
#generando las consultas SQL
#db.create_all() esto no va aqui se puso en main


