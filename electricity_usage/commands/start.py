import click
import os
from electricity_usage.data_dirs import create_input_dir_path
from areas import codes

@click.command()
@click.option('--area',type=click.Choice(codes), default='DE', help="area code according to 'electricity_usage areas'")

def start(area):

    '''starts the tool background process (demon)'''
    input_dir = create_input_dir_path(area)
    #alternative: daemon direkt von hier aus ausführen (ohne daemon.py auszuführen)
    # Instanziieren Sie den Daemon
    daemon_instance = daemon.Daemon(os.getenv("API_KEY"), area, input_dir)

    # Starten Sie die run-Methode des Daemons in einem separaten Thread
    daemon_thread = threading.Thread(target=daemon_instance.run) #daemon=True darf nicht gesetzt werden
    daemon_thread.start()

