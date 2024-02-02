#confguracón para la producción y el desarrollo y conexiones a base de datos
class Config:
    DEBUG = True
    TESTING =True
    
    #COnfiguración de DB
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #usuario root + ubicación / clave de DB y puerto nombre del esquema de la DB creado
    #debe estar credala base de datos ejemplo blog_db
    #SQLALCHEMY_DATABASE_URI es una variable sugerida por la documentación de Flask
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Villadavid20@localhost:3308/blog_db"   
    
    #Clase para modo de producción y desarrollo 27:59 https://www.youtube.com/watch?v=JTAY5_LO0Ug

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    SECRET_KEY = 'dev'
    DEBUG = True
    TESTING =True
    
    