# comando para ejecutar debug   (flask --app "nombre del archivo py" --debug run) 
#flask --app main.py  --debug run 
from myblog import app   
#se importo el paquete myblog el cual tiene el __init__ que llama a config.db y ejecuta la configuracion de BD

if __name__ == '__main__':
    app.run()
