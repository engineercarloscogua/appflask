from flask import Flask, request, make_response, redirect
#* flask --app tutorialflask  run   con este comando puede correr esta app de pruebas
#! app es el nombre de la variable que se utiliza para almacenar la instancia de la aplicación.
#!Flask es la clase que se utiliza para crear la instancia de la aplicación.
#!__name__ es una variable especial que contiene el nombre del módulo que se está ejecutando.
app = Flask(__name__) # crea una instancia ( Objeto )de la aplicación Flask


@app.route("/index") #* Este decorador se usa para asociar una vista con una ruta URL específica.
def index():    
    return "Hello World"

#* Comprueba si el módulo se está ejecutando como el programa principal.
if __name__ == "__main__": #! Cuando se ejecuta un archivo Python, el valor de la variable __name__ se establece como "__main__".
    #*Si el módulo se está ejecutando como el programa principal, ejecuta la aplicación Flask.
    app.run() #!La función app.run() inicia un servidor web local en el puerto 5000.
    


