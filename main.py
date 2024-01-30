# comando para ejecutar debug   (flask --app "nombre del archivo py" --debug run) 
from flask import Flask   #Import Flask library / con esto podemos hacer una app

app = Flask (__name__) #create app / give back a parameter /indicando que aqui se encuentran todos los recursos de los proyectos
#creating routes to use decorators
@app.route("/") #decorador con ruta

#funtion for show message in page
def hola(): 
    return "<h1> Hello world prueba de git ignore 3 <h1>"