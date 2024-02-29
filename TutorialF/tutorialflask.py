from flask import Flask, render_template 
#* flask --app tutorialflask  run   con este comando puede correr esta app de pruebas
#! app es el nombre de la variable que se utiliza para almacenar la instancia de la aplicación.
#!Flask es la clase que se utiliza para crear la instancia de la aplicación.
#!__name__ es una variable especial que contiene el nombre del módulo que se está ejecutando.
app = Flask(__name__) # crea una instancia ( Objeto )de la aplicación Flask


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
@app.route('/') #* Este decorador se usa para asociar una vista con una ruta URL específica.
def index():
    return render_template('index.html')

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
    #*Si el módulo se está ejecutando como el programa principal, ejecuta la aplicación Flask.
    app.run(debug = True) #!La función app.run() inicia un servidor web local en el puerto 5000.
#! En resumen, el modo debug es una herramienta útil para principiantes que están aprendiendo a programar. Te ayuda a encontrar errores, entender tu código y probar cosas nuevas. Sin embargo, no es necesario para el producto final y puede ser un poco lento e informativo.


