import json
import sqlite3

from DatabaseHandler import DatabaseHandler

'''
# Obtener o establecer configuraciones
    debug = config_manager.obtener_configuracion('debug')
    if debug is None:
        config_manager.establecer_configuracion('debug', True)

    # Guardar las configuraciones actualizadas
    config_manager.guardar_configuraciones()
'''


class Configuracion:
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
        self.configuraciones = {}

    def cargar_configuraciones(self):
        try:
            with open(self.ruta_archivo, 'r') as archivo:
                self.configuraciones = json.load(archivo)
            print(f"Configuraciones cargadas desde {self.ruta_archivo}")
        except FileNotFoundError:

            self.configuraciones = {
                'name': 'GameCreatorWeb',
                'debug': True
            }
            arte_texto = '''
              ____   ____  ___ ___    ___         __  ____     ___   ____  ______   ___   ____       __    __    ___  ____  
             /    | /    ||   |   |  /  _]       /  ]|    \\   /  _] /    ||      | /   \\ |    \\     |  |__|  |  /  _]|    \\ 
            |   __||  o  || _   _ | /  [_       /  / |  D  ) /  [_ |  o  ||      ||     ||  D  )    |  |  |  | /  [_ |  o  )
            |  |  ||     ||  \\_/  ||    _]     /  /  |    / |    _]|     ||_|  |_||  O  ||    /     |  |  |  ||    _]|     |
            |  |_ ||  _  ||   |   ||   [_     /   \\_ |    \\ |   [_ |  _  |  |  |  |     ||    \\     |  `  '  ||   [_ |  O  |
            |     ||  |  ||   |   ||     |    \\     ||  .  \\|     ||  |  |  |  |  |     ||  .  \\     \\      / |     ||     |
            |___,_||__|__||___|___||_____|     \\____||__|\\_||_____||__|__|  |__|   \\___/ |__|\\_|      \\_/\\_/  |_____||_____|
            '''

            print(arte_texto)

            nameapp = input("Nombre de tu juego(GameCreatorWeb): ") or 'GameCreatorWeb'

            database = input("Selecciona el tipo de base de datos (mysql, sql_lite, default=mysql): ")
            while database != 'mysql' and database != 'sql_lite':
                database = input("Selecciona el tipo de base de datos (mysql, sql_lite, default=mysql): ")
            if database == 'mysql':
                usermsql = input("Nombre de usuario de mysql: ") or 'root'
                passmsql = input("Nombre clave de mysql: ") or ''
                hotsmsql = input("Host de mysql: ") or '127.0.0.1'
                portmsql = input("Port de mysql: ") or '3306'
                self.configuraciones['MysqlUser'] = usermsql
                self.configuraciones['MysqlPasswor'] = passmsql
                self.configuraciones['MysqlHost'] = hotsmsql
                self.configuraciones['MysqlPort'] = portmsql
            if database == 'sql_lite':
                self.configuraciones['SQLPath'] = input("Especifica la ruta y el nombre de la db: ") or 'gcw.db'
                conexion = sqlite3.connect(self.configuraciones['SQLPath'])
                handele = DatabaseHandler('sql_lite',self.configuraciones['SQLPath'])

            self.configuraciones['name'] = nameapp
            self.configuraciones['database'] = database

            login = input("Usara usuarios en su juego? Si/No (No): ") or 'No'
            while login != 'Si' or login != 'No':
                login = input("Usara usuarios en su juego? Si/No (No): ") or 'No'




            self.configuraciones['login'] = login

            self.guardar_configuraciones()

    def obtener_configuracion(self, clave):
        return self.configuraciones.get(clave, None)

    def establecer_configuracion(self, clave, valor):
        self.configuraciones[clave] = valor

    def guardar_configuraciones(self):
        with open(self.ruta_archivo, 'w') as archivo:
            json.dump(self.configuraciones, archivo, indent=4)
        print(f"Configuraciones guardadas en {self.ruta_archivo}")
