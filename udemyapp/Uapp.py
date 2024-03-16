from flask import (
    Flask,
    render_template,
    request, #? extrae argumemntos de los formularios
    redirect, #? redirecciona a otros templates
    url_for,
    flash #permite mostrar mensaje semergentes
    )
import json #? El módulo json proporciona funciones para trabajar con datos en formato JSON.
import os.path #? El módulo os proporciona funciones para interactuar con el sistema operativo.
from werkzeug.utils import secure_filename  #? # secure_filename es una función proporcionada por Werkzeug, una biblioteca WSGI para Python, que ayuda a garantizar que los nombres de archivo sean seguros para su almacenamiento en el sistema de archivos.
from forms import Loginform, CreateUserForm #? importando los campos desde el modelo de form
#* Name app must be the same as princiapl file 
Uapp = Flask(__name__)
#* estableciendo clave secreta
Uapp.secret_key = 'hghgfhfhfhdffgc'

#?--------------------RUTES, ALL RUTES MUST HAVE YOUR OWN FUNTION-----------------------------------
#*Rute's name must be equal to funtion name
@Uapp.route("/home") 
@Uapp.route("/") #the decorete associated a rute with the funtion
def home ():
    #llamando la estrctura de loguin desde el archivo form
    login = Loginform()
    #retona formi es una valirable que contiene los atributos del login al html
    return render_template('form2.html', formi= login) # this line renders the template, and passing a date witjh jinja2 in the template
@Uapp.route("/registro")
def login ():
    login = CreateUserForm() # usando l la clase del archivo forms.py
    return  render_template('register.html', regis= login)

#* ---------------------FORMULARIO ----------------------------------------------------------------------------------------------------------
@Uapp.route("/form")
def formulario ():
    return render_template('form.html')
#*------------------------------Creating a dinamic rute / Ruta dinámica que maneja peticiones GET y POST----------------------------------------
@Uapp.route("/dinamic", methods = ['GET', 'POST'])  # for work with post method always must out the methods in the rute
def dinamic():
    #validation if there is a method POST in the rute /Si la petición es POST, se procesa el formulario
    if request.method == 'POST':
        #* ---------------Verificación si el nombre del user y la url ya han sido ingresados para ser fedirigidos al home , 2 if -----------------
        # inicializate var utls empty /Diccionario para almacenar las URLs
        urls = {}
        #*-----------------Si existe el archivo 'urls.json', carga su contenido en el diccionario urls-----------------------------
        if os.path.exists('urls.json'):
            with open('urls.json') as url_file: # Abre el archivo urls.json en modo lectura ('r').
                urls = json.load(url_file) #Lee el contenido de urls.json como un objeto JSON y lo almacena en el diccionario urls.
        
        #Comprueba si el código enviado (accedido mediante request.form['code']) existe como clave en el diccionario urls.-
        #*---------------------Verifica si el código enviado en el formulario ya existe como clave en el diccionario urls   -----------------    
        if request.form['code'] in urls.keys():
            #flash funciona en base a request 
            flash('Esa clave o nombre ya esta ocupada')
            return redirect(url_for('formulario'))  #redirija al form atravez de la funcion formulario en este archivo        
        #* ----------------------Si se proporciona una URL en el formulario------------------------------------------------
        if 'url' in request.form.keys():
            # Guarda la URL en el diccionario urls
            urls = {request.form['code']: request.form['url']}
        else:
            # variable para recibir el dato de file / se carga un archivo en el formulario
            f = request.files['file']
            #* no sobreescribit el archivo
            full_name = request.form['code'] + secure_filename(f.filename) # Genera un nombre único para el archivo
            f.save('static/uploads/' + full_name) #save in a uploads folder and concatenate fullname / # Guarda el archivo en el directorio 'uploads'
            urls [request.form['code']] = {'file':full_name} # Guarda la información del archivo en el diccionario urls       
        #*-----------------Crea un nuevo par clave-valor en el diccionario / Guarda el diccionario urls en el archivo 'urls.json'----------------------
        with open('urls.json', 'w') as url_file: # Abre el archivo urls.json en modo escritura ('w').
            json.dump(urls, url_file) # Escribe el diccionario urls actualizado como un objeto JSON al archivo, Asigna el objeto del archivo abierto a url_file.
            # Si el archivo no existía, se creará.
            flash("Se ha creado el registro correctamente" , "success") # SE AGREGO UNA CATEGORIA PARA ASIGNAR UN ESTILO E ITERAR EN EL HTML /Muestra un mensaje de éxito
        return render_template('dinamic.html', nombre=request.form['code']) #* send args to form html template with the name / Renderiza el template 'dinamic.html' y pasa el nombre del código como parámetro 'nombre'
    #*Si la petición es GET, redirige al usuario a la ruta 'form'
    else:
        return redirect(url_for('form')) #* This metohd for using Get and don't pass params when it is redirecting another template
        #return redirect('https://www.youtube.com/watch?v=hFCi-SCOZJM') #* maybe you can redirect another external website
        
#? ------------Rute for show images from Form-------------------------------

@Uapp.route('/<string:code>')
def redirigir(code):
    #Si el archivo urls.json existe, se abre y se lee su contenido.
    if os.path.exists('urls.json'):
        with open('urls.json') as url_file:
            #Se carga el contenido del archivo JSON como un diccionario.
            urls = json.load(url_file)
            #Si el código proporcionado existe en el diccionario, se retorna una redirección a la URL asociada.
            if code in urls.keys():
                return redirect(url_for('static', filename='uploads/' + urls[code]['file']))
    # Si el código no existe en el JSON o hay algún problema, retorna una respuesta alternativa
    return "Código no encontrado o error en la redirección", 404  # Retornando un mensaje de error 404
#? ------------Rute for show images from Form------------
#?-------------------END RUTES FUNTIONS ---------------------------------------------------------------
#? -----------RUNNING APP-------------------------------------------------------------------------------
#* Check if the module is running as principal program
if __name__ == "__main__": #When executed an python file, the value of  variable __name__  is as  "__main__".
   with Uapp.app_context():  # This line create a context of aplication for Uaap. This is necessary for that Run funtión working.
    #* If module is executing as principal program, it execute the app Uapp.
    Uapp.run(debug = True) #the funtions execute for stard the local service, this metodh don't have to use in deploy only to use in development
#* En resumen, el modo debug es una herramienta útil para principiantes que están aprendiendo a programar. Te ayuda a encontrar errores, entender tu código y probar cosas nuevas. Sin embargo, no es necesario para el producto final y puede ser un poco lento e informativo.
#? ------------END RUUNING------------------------------------------------------------------------------
