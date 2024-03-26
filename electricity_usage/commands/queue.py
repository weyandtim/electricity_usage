import click
import os
from electricity_usage.data_dirs import get_input_dir_path

@click.command()

def queue():
    '''shows a list of processes in queue'''
    main = get_input_dir_path()
    dirs = os.listdir(main)
    print("Currently queued processes:\n")
    for d in dirs:
        print(d+':')
        path_to_dir = os.path.join(main,d)
        files = [f for f in listdir(path_to_dir) if isfile(join(path_to_dir, f))]
        for f in files:
            #with open(f) as j:
            #    c = j.commandline
            #    print(f, c)
            print(f)
        print("\n")
    
