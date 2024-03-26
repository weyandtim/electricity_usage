import click
import os
import threading
from electricity_usage.commands.areas import codes
from electricity_usage import data_dirs
from electricity_usage import daemon

@click.command()
@click.option('--area',type=click.Choice(codes), default='DE', help="area code corresponding to the local area as shown by 'electricity_usage areas'. The default value for this is 'DE corresponding to Germany")

def start(area):
    '''starts the tool background process (demon)'''
    # build directory for daemon communication
    data_dir = data_dirs.create_input_dir_path()
    # create daemon instance
    daemon_instance = daemon.Daemon(os.getenv("API_KEY"), area, data_dir)

    # start daemon.run in seperate thread
    daemon_thread = threading.Thread(target=daemon_instance.run) 
    daemon_thread.start()

