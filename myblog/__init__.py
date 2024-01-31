from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

#Carga de Configuraciones de la BD del archivo config.py
# from object se usa porque se esta trabajando clases en este caso el modo desarrollo class DevelopmentConfig
app.config.from_object('config.DevelopmentConfig')
# variable que refleja la BD  mysql de la app
db = SQLAlchemy(app)
# ejecutar todas las consultas de Sql
