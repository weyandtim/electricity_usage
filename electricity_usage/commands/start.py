import click
import os
from areas import codes

@click.command()
@click.option('--area',type=click.Choice(codes), default='DE', help="area code according to 'electricity_usage areas'")

def start(area):
    '''starts the tool background process (demon)'''
    here = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(here, f'../input_dir_{area}')
    os.system(f'python3 daemon.py {area} {input_dir}')
