from flask import (
    Flask,
    render_template, 
    request, #*Sirve oara doferenciar cuando una ruta recibe un metodo get o post
    
    )

# función para encriptar claves
from werkzeug.security import generate_password_hash, check_password_hash, generate_password_hash 


from flask_sqlalchemy import SQLAlchemy 
import os
#* flask --app tutorialflask  run   con este comando puede correr esta app de pruebas
#! app es el nombre de la variable que se utiliza para almacenar la instancia de la aplicación.
#!Flask es la clase que se utiliza para crear la instancia de la aplicación.
#!__name__ es una variable especial que contiene el nombre del módulo que se está ejecutando.

#* Direccion de la BD - sqlite /// es un conector , os.path toma la ruta absoluta actual y le agrega la bd
ruta= "sqlite:///"+ os.path.abspath(os.getcwd())+ "/database.db"

appnueva = Flask(__name__) # crea una instancia ( Objeto )de la aplicación Flask

#confoguraciones de la BD
appnueva.config["SQLALCHEMY_DATABASE_URI"]= ruta
appnueva.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#crea variable almacenando con la clase sqlachemy la appnueva
database= SQLAlchemy(appnueva)

#Creando el esquema o modelo de DB
class Posts(database.Model):
    #columnas / atributos 
    id = database.Column(database.Integer, primary_key =True)
    title = database.Column(database.String(50), unique = True, nullable = True)

class Users(database.Model):
    id = database.Column(database.Integer, primary_key =True)
    username = database.Column(database.String(50), unique = True, nullable= True)
    password = database.Column(database.String(80), nullable = True)
    
    
#! RUTAS 

#
#1. Variables estáticas:

#Se definen en la ruta misma.
#Son valores fijos que no cambian.
#Ejemplo: /usuario/<nombre>

#2. Variables dinámicas:

#Se extraen de la URL cuando un usuario solicita la ruta.
#Pueden ser de diferentes tipos, como números, cadenas o fechas.
#Ejemplo: /usuario/<int:id>

#3. Expresiones regulares:

#Permiten definir patrones más complejos para las variables.
#Se pueden usar para validar la entrada del usuario.
#Ejemplo: /usuario/<regex("[a-zA-Z0-9]+")>

#4. Convertidores personalizados:

#Permiten crear tus propios tipos de variables.
#Se pueden usar para manejar diferentes tipos de datos.
#Ejemplo: Un convertidor para convertir una cadena a una fecha.

#!RUTA SIN VARIABLES NI EXTENCIONES
#* Nomralmente la ruta recibe peticiones tipo get aunque los formularios son post emtonces con una lista llamada methos podemos hacer que reciba ambos metodos
@appnueva.route('/singuptutorial', methods =["GET", "POST"] ) #* Este decorador se usa para asociar una vista con una ruta URL específica.
def singuptutorial():
    #*Valida el tipo de metodo de donde esta extrayendo la información 
    if request.method == "POST":
        # hashed_pwd variable que contiene la contraseña encriptada
        
        #contruyecndo el objeto que se va almacenar en la BD
        # este objeto hereda de la clase Users en la BD es decir el esquema
        #[username] es el nombre del campo en el html
        new_user = Users(username, generate_password_hash(password))  
        #generando el registro en la DB
        database.session.add(new_user) 
        #neviando el cambio
        database.session.Commit() 
        return "Te has registrado Exitosamente"
    return render_template('singuptutorial.html') #renderiza la plantilla html


#! RUTA CON VARIABLE ENTERA
#@app.route("/valor/<int:n>")
#def valor(n):
 #   return "numero: {}".format(n)

#! RUTA CON VARIABLES MIXTAS
#@app.route("/identificador/<int:id>/<string:username>")
#def userid(id,username):
 #   return "El id es: {} y el nombre de usuario {}".format(id, username)

#! RUTA DE CADENA DE TEXTO
#@app.route("/user/<string:user>")
#def user(user):
#   return "Hola"+ user

#! RUTA NORMAL
#@app.route("/hola")
#def hola ():
 #   return "Hola, un saludo"

#! RUTA DEFAUL X DEFECTO
#@app.route("/default/") #* si no se especifica la ruta entonces arignara  yahoo por defecto de lo contrario la ruta seria la palabra cifrado
#@app.route("/default/<string:cifrado>") #*realmente no esta cifrado es solo una palabra de ejemplo
#def dft (cifrado = "Yahoo!!"):
 #   return "El valor indicado es" + cifrado

#! Comprueba si el módulo se está ejecutando como el programa principal.
if __name__ == "__main__": #! Cuando se ejecuta un archivo Python, el valor de la variable __name__ se establece como "__main__".
   with appnueva.app_context(): # esta parte tiene que ir aqui no se para que 
   #*indicando que cuando se cree el modulo se cree la db
    database.create_all()  #crea la base de datos 1 vez  
    #*Si el módulo se está ejecutando como el programa principal, ejecuta la aplicación Flask.
    appnueva.run(debug = True) #!La función app.run() inicia un servidor web local en el puerto 5000.
#! En resumen, el modo debug es una herramienta útil para principiantes que están aprendiendo a programar. Te ayuda a encontrar errores, entender tu código y probar cosas nuevas. Sin embargo, no es necesario para el producto final y puede ser un poco lento e informativo.


