import os
import subprocess
import threading
import time
import re
from GlobalData import GlobalData


class ServidorVue:
    def __init__(self):
        self.directorio_vue = os.path.join(os.getcwd(), 'Web')
        self.process = None
        self.hilo_lectura = None

    def leer_salida_proceso(self):
        try:
            while True:
                output = self.process.stdout.readline()
                if not output and self.process.poll() is not None:
                    break
                if 'Local' in output.rstrip():
                    patron_url = re.compile(r'http?://\S+')
                    resultado = patron_url.search(output.rstrip())
                    # Obtener el grupo sin los códigos de formato
                    url_encontrada = resultado.group()
                    # Eliminar los códigos de formato ANSI
                    GlobalData._urlDevHost = re.sub(r'\x1b\[\d+m', '', url_encontrada)
                    # print(f"RCW: Servidor DEVEL {output.rstrip()}")

        except Exception as e:
            print(f"Error al leer la salida del proceso: {e}")

    def iniciar_servidor_vue(self):
        try:
            # Iniciar servidor Vue.js en segundo plano y redirigir la salida a una PIPE
            self.process = subprocess.Popen(
                "npm run dev",
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True,
                cwd=self.directorio_vue,
                text=True  # Habilitar el modo de texto para decodificar la salida correctamente
            )

            # Crear un hilo para leer la salida del proceso sin bloquear
            self.hilo_lectura = threading.Thread(target=self.leer_salida_proceso, daemon=True)
            self.hilo_lectura.start()

            while self.process.poll() is None:  # Mientras el proceso esté en ejecución
                # Tu lógica aquí
                time.sleep(1)

        except Exception as e:
            print(f"Error al ejecutar el comando: {e}")

        finally:
            # Esperar a que el proceso termine y cerrar el hilo de lectura
            self.process.wait()
            self.hilo_lectura.join()
