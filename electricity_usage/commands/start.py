import click
import os
from electricity_usage.commands.areas import codes

@click.command()
@click.option('--area',type=click.Choice(codes), default='DE', help="area code according to 'electricity_usage areas'")

def start(area):
    '''starts the tool background process (demon)'''
    here = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(os.path.join(here, '../input_data'), exist_ok=True)
    input_dir = os.path.join(here, f'../input_data/input_dir_{area}')
    os.system(f'python3 electricity_usage\daemon.py {area} {input_dir}') #pfad anpassen (muss relativ zu start.py sein)
    #alternative: daemon direkt von hier aus ausführen (ohne daemon.py auszuführen) 


