# comando para ejecutar debug   (flask --app "nombre del archivo py" --debug run) 
# Importa la aplicación Flask y la base de datos desde el paquete myblog
from myblog import app,db   
# If # Esta condición verifica si el script se está ejecutando directamente como el programa principal.
    # Es una convención en Python para asegurarse de que el código dentro de este bloque solo se ejecute cuando el script es el punto de entrada.
    # En este caso, el bloque de código se ejecutará cuando este archivo (main.py) sea ejecutado directamente como un script,
    # y no cuando sea importado como un módulo en otro archivo.
    # Esto es útil cuando se quiere proporcionar un comportamiento específico cuando el archivo es ejecutado como un programa independiente.
# Se importa el paquete myblog, que contiene el módulo principal __init__.py que configura la aplicación Flask y la base de datos   
# with app.app_context(): Crea un contexto de aplicación para que la aplicación pueda interactuar con la base de datos
# db.create_all() Crea todas las tablas definidas en los modelos de SQLAlchemy en la base de datos
# app.run() Ejecuta la aplicación Flask
if __name__ == "__main__":
    with app.app_context():
        db.create_all() #crea la tabla en la db al ejecutar
        app.run()
