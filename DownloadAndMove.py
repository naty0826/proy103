import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/NatyA/Downloads"              # Agrega la ruta a tu carpeta "Descargas".
to_dir = "C:/Users/NatyA/Desktop/Downloaded_Files" #Crea la carpeta "Document_Files" en tu escritorio y actualiza la ruta correspondiente.



dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Clase event handler

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):

        name, extension = os.path.splitext(event.src_path)
        
        time.sleep(1)
        for key, value in dir_tree.items():

            time.sleep(1)
            if extension in value:               

                file_name = os.path.basename(event.src_path)

                print("Descargado " + file_name)

                path1 = from_dir + '/' + file_name
                path2 = to_dir + '/' + key
                path3 = to_dir + '/' + key + '/' + file_name

                time.sleep(1)
                if os.path.exists(path2):

                    print("El directorio Existe...")
                    time.sleep(1)
                                        
                    if os.path.exists(path3):

                        print("El archivo ya existe en " + key + "....")
                        print("Renombrando archivo " + file_name + "....")

                        new_file_name = os.path.splitext(file_name)[0] + str(random.randint(0, 999)) + os.path.splitext(file_name)[1]

                        path4 = to_dir + '/' + key + '/' + new_file_name

                        print("Moviendo " + new_file_name + "....")
                        shutil.move(path1, path4)
                        time.sleep(1)

                    else:
                        print("Moviendo " + file_name + "....")
                        shutil.move(path1, path3)
                        time.sleep(1)

                else:
                    print("Creando Directorio...")
                    os.makedirs(path2)
                    print("Moviendo " + file_name + "....")
                    shutil.move(path1, path3)
                    time.sleep(1)


# Inicia la clase event handler
event_handler = FileMovementHandler()

# Inicia Observer
observer = Observer()

# Programa Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Inicia Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("ejecutando...")
except KeyboardInterrupt:
    print("detenido")
    observer.stop()

