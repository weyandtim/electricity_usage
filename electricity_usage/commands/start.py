import click
import os
import platformdirs
import threading
from electricity_usage.commands.areas import codes
from electricity_usage import data_dirs
from electricity_usage import daemon

@click.command()
@click.option('--area',type=click.Choice(codes), default='DE', help="area code according to 'electricity_usage areas'")

def start(area):
    '''starts the tool background process (demon)'''
     # Verzeichnis für kommunikation mit dem Daemon erzeugen/path erhalten
    data_dir = data_dirs.create_input_dir_path()
    '''os.makedirs(data_dir, exist_ok=True)
    os.system(f'python3 electricity_usage\daemon.py {area} {data_dir}')''' #pfad anpassen (muss relativ zu start.py sein)
    #alternative: daemon direkt von hier aus ausführen (ohne daemon.py auszuführen) 
    # Instanziieren Sie den Daemon
    daemon_instance = daemon.Daemon(os.getenv("API_KEY"), area, data_dir)

    # Starten Sie die run-Methode des Daemons in einem separaten Thread
    daemon_thread = threading.Thread(target=daemon_instance.run) #daemon=True darf nicht gesetzt werden
    daemon_thread.start()

