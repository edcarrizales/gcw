from flask import Flask, send_file, redirect

from Configuracion import Configuracion
from GlobalData import GlobalData


class ApiCore:
    def __init__(self):
        # Crear una instancia de la clase
        self.config_manager = Configuracion('config.json')
        # Cargar configuraciones desde el archivo existente o crear uno nuevo con la configuración predeterminada
        self.config_manager.cargar_configuraciones()

        self.app = Flask(__name__)
        self.configurar_rutas()

    def configurar_rutas(self):
        self.app.route('/')(self.index)
        self.app.route('/assets/<file>')(self.assets)

    @staticmethod
    def assets(file):
        return send_file("Web/dist/assets/" + file)

    def index(self):
        if self.config_manager.obtener_configuracion('debug'):
            return redirect(GlobalData.getUrlDEvHost())
        else:
            return send_file("Web/dist/index.html")
        # return '¡Bienvenido al servidor Flask!'

    def run(self):
        self.app.run(debug=False)
