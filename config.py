#confguracón para la producción y el desarrollo y conexiones a base de datos
class Config:
    DEBUG = True
    TESTING =True
    
    #COnfiguración de DB
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #usuario root + ubicación / nombre del esquema de la DB creado
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Villadavid20@localhost:3308/blog_db"   
    
    #Clase para modo de producción y desarrollo 27:59 https://www.youtube.com/watch?v=JTAY5_LO0Ug

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    SECRET_KEY = 'Villadavid20'
    DEBUG = True
    TESTING =True
    
    