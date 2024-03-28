import click
import os
import platformdirs
import threading
from electricity_usage.commands.area_codes import codes
from electricity_usage import data_dirs
from electricity_usage import daemon

# the start command creates a daemon instance and starts its run method as a daemon process

@click.command()
@click.option('--area',type=click.Choice(codes), default='DE', help="area code corresponding to the local area as shown by 'electricity_usage areas'. The default value for this is 'DE' corresponding to Germany")

def start(area):
    '''starts the tool background process (demon)'''
    # build directory for daemon communication
    data_dir = data_dirs.create_input_dir_path()
    # create daemon instance
    daemon_instance = daemon.Daemon(os.getenv("EM_API_KEY"), area, data_dir)

    # start daemon.run in seperate thread
    daemon_thread = threading.Thread(target=daemon_instance.run) 

    daemon_thread.start()

