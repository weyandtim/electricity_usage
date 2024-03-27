import click
import os
from ..data_dirs import get_input_dir_path

@click.command()

def queue():
    '''shows a list of processes in queue'''
    path_to_dir = get_input_dir_path()
    print(f"In your input directory {path_to_dir}, you currently have the following jobs in your queue:\n")
    files = [f for f in path_to_dir if os.path.isfile(os.path.join(path_to_dir, f))]
    for f in files:
        #with open(f) as j:
        #    c = j.commandline
        #    print(f, c)
        print(f)
        print("\n")
    
