import click
import os
from xdg_base_dirs import xdg_data_home

@click.command()

def queue():
    '''shows a list of processes in queue'''
    datadir = xdg_data_home()
    main = os.path.join(datadir, 'electricity_usage/input_data')
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
    
