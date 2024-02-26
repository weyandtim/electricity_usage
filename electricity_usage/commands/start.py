import click
import os
from xdg_base_dirs import xdg_data_home
import threading
from electricity_usage.commands.areas import codes
from electricity_usage import daemon

@click.command()
@click.option('--area',type=click.Choice(codes), default='DE', help="area code according to 'electricity_usage areas'")

def start(area):
    '''starts the tool background process (demon)'''

     # Verzeichnis für kommunikation mit dem Daemon erzeugen/path erhalten
    datadir = xdg_data_home()
    os.makedirs(os.path.join(datadir, 'electricity_usage/input_data'), exist_ok=True)
    input_dir = os.path.join(datadir, f'electricity_usage/input_data/input_dir_{area}')
    os.makedirs(input_dir, exist_ok=True)
    #alternative: daemon direkt von hier aus ausführen (ohne daemon.py auszuführen) 
    # Instanziieren Sie den Daemon
    daemon_instance = daemon.Daemon(os.getenv("API_KEY"), area, input_dir)

    # Starten Sie die run-Methode des Daemons in einem separaten Thread
    daemon_thread = threading.Thread(target=daemon_instance.run) #daemon=True darf nicht gesetzt werden
    daemon_thread.start()
