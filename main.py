import argparse
import threading
from Configuracion import Configuracion
from ServidorVue import ServidorVue
from apiCore import ApiCore


def parse_args():
    parser = argparse.ArgumentParser(description='Script de ejemplo con parámetros')
    return parser.parse_args()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Crear una instancia de la clase
    config_manager = Configuracion('config.json')
    # Cargar configuraciones desde el archivo existente o crear uno nuevo con la configuración predeterminada
    config_manager.cargar_configuraciones()

    api_core = ApiCore()

    # Crear un hilo para iniciar la API Flask
    hilo_api = threading.Thread(target=api_core.run, daemon=True)
    hilo_api.start()

    servidor_vue = ServidorVue()

    debug = config_manager.obtener_configuracion('debug')
    if debug:
        # Crear un hilo para iniciar el servidor Vue.js
        hilo_servidor_vue = threading.Thread(target=servidor_vue.iniciar_servidor_vue, daemon=True)
        hilo_servidor_vue.start()
        hilo_servidor_vue.join()
    else:
        # Se compila el web
        pass

    print("Hilos iniciados. Esperando a que terminen...")

    # Esperar a que ambos hilos terminen antes de salir
    hilo_api.join()

    print("Ambos hilos han terminado. Fin del programa.")
