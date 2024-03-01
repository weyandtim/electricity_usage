import click
import os
from xdg_base_dirs import xdg_data_home
from electricity_usage.data_dirs import get_input_dir_path

@click.command()

def queue():
    '''shows a list of processes in queue'''
    main = get_input_dir_path()
    dirs = os.listdir(main)
    print("Currently queued processes:\n")
    for d in dirs:
        print('For Subdirectory '+d+':')
        path_to_dir = os.path.join(main,d)
        files = [f for f in listdir(path_to_dir) if isfile(join(path_to_dir, f))]
        for f in files:
            print(f)
            # add-on to print commandline as well as filename would be cool
        print("\n")
    
