import click
import os

@click.command()

def stop():
    '''stops the tool demon and abandons all processes'''
    #print('This will stop the tool later')
    input_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),'input_data')
    if os.path.exists(input_dir):
        if not os.listdir(input_dir):
            os.rmdir(input_dir)
        else: 
            print('Warning: There are still processes the the queue.')
            #yes/no abfrage einbauen für entgültigen abbruch
            for file in input_dir:
                os.remove(file)



