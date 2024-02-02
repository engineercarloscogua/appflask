#Registro de vistas
from flask import(
    render_template, Blueprint, flash, g, redirect, request, session, url_for   
)

#creando Blue print / Crea todas las vistas
auth = Blueprint('auth', __name__, url_prefix= '/auth') #Url prefijo 

# Registrar Usuario
@auth.route('/register',mothods = ('GET', 'POST') ) # mothods = ('GET', 'POST') DECORADOR DIRECCIONA LA RUTA Y PERMITE ENVIO TEXTO POR GET O HTML CON POST
def register():
    return "Registrar Usuario"