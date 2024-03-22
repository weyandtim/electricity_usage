import click
import os
import platformdirs
import threading
from electricity_usage.commands.areas import codes
from electricity_usage import data_dirs
from electricity_usage import daemon

# the start command creates a daemon instance and starts its run method as a daemon process

@click.command()
@click.option('--area',type=click.Choice(codes), default='DE', help="area code according to 'electricity_usage areas'")

def start(area):
    '''starts the tool background process (demon)'''
     # Verzeichnis für kommunikation mit dem Daemon erzeugen/path erhalten
    data_dir = data_dirs.create_input_dir_path()
    # Daemon instanz erzeugen
    daemon_instance = daemon.Daemon(os.getenv("EM_API_KEY"), area, data_dir)

    # run-Methode des Daemons in einem separaten Thread starten
    daemon_thread = threading.Thread(target=daemon_instance.run) #daemon=True darf nicht gesetzt werden
    daemon_thread.start()

