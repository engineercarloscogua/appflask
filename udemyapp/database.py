
from app import db,app
from flask_sqlalchemy import SQLAlchemy #? import propietis that DB
db = SQLAlchemy(app)

#*inicializate db 
db.init_app(app)
# DATABASE MODEL

#? this class will create db model in sqlalchemy for Sqlite database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username  = db.Column(db.String(80), unique=True, nullable=False) 
    email =  db.Column(db.String(80), unique=True, nullable=False) 
    password = db.Column(db.String(80)) 
    #--------Permite ejecutar consultas sql por consola sin pedir tantas importaciones ----------
    def __repr__(self):
        return f'{self.id, self.username, self.email}'
    

