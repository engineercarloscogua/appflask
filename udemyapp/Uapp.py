from flask import (
    Flask,
    render_template,
    request, #? extrae argumemntos de los formularios
    redirect, #? redirecciona a otros templates
    url_for
    )
import json #* El paquete json en Flask serializa y deserializa datos JSON, facilitando el intercambio de datos con aplicaciones web y APIs.

#* Name app must be the same as princiapl file 
Uapp = Flask(__name__)

#?--------------------RUTES, ALL RUTES MUST HAVE YOUR OWN FUNTION-----------------------------------
#*Rute's name must be equal to funtion name
@Uapp.route("/home") 
@Uapp.route("/") #the decorete associated a rute with the funtion
def home ():
    return render_template('home.html', nombre= "el mejor programador") # this line renders the template, and passing a date witjh jinja2 in the template
@Uapp.route("/login")
def login ():
    return "This is the login"

@Uapp.route("/form")
def formulario ():
    return render_template('form.html')
#Creating a dinamic rute
@Uapp.route("/dinamic", methods = ['GET', 'POST'])  #* for work with post method always must out the methods in the rute
def dinamic():
    #validation if there is a method POST in the rute
    if request.method == 'POST':
        # generating un diccionario que recibe los parametros url del formulario
        urls = {request.form['url']: request.form['code']}
        with open('urls.json', 'w') as url_file: # si no existe sarchivos url lo creara
            json.dump(urls, url_file) # pasa el contenido del diccionario al archivo url_file
        return render_template('dinamic.html', nombre=request.form['code']) #* send args to form html template with the name
    else:
        return redirect(url_for('home')) #* This metohd for using Get and don't pass params when it is redirecting another template
        #return redirect('https://www.youtube.com/watch?v=hFCi-SCOZJM') #* maybe you can redirect another external website
#?-------------------END RUTES FUNTIONS ---------------------------------------------------------------
#? -----------RUNNING APP-------------------------------------------------------------------------------
#* Check if the module is running as principal program
if __name__ == "__main__": # When executed an python file, the value of  variable __name__  is as  "__main__".
   with Uapp.app_context(): #  This line create a context of aplication for Uaap. This is necessary for that Run funtión working.
    #* If module is executing as principal program, it execute the app Uapp.
    Uapp.run(debug = True) #the funtions execute for stard the local service, this metodh don't have to use in deploy only to use in development
#* En resumen, el modo debug es una herramienta útil para principiantes que están aprendiendo a programar. Te ayuda a encontrar errores, entender tu código y probar cosas nuevas. Sin embargo, no es necesario para el producto final y puede ser un poco lento e informativo.
#? ------------END RUUNING------------------------------------------------------------------------------
