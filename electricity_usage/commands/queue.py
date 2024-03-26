import click
import os

@click.command()

def queue():
    '''shows a list of processes in queue'''
    here = os.path.dirname(os.path.abspath(__file__))
    main = os.path.join(here, '../input_data')
    dirs = os.listdir(main)
    for d in dirs:
        print('For Subdirectory '+d+':\n')
        path_to_dir = os.path.join(main,d)
        files = [f for f in listdir(path_to_dir) if isfile(join(path_to_dir, f))]
        for f in files:
            #with open(f) as j:
            #    c = j.commandline
            #    print(f, c)
            print(f)
        print("\n")

    
