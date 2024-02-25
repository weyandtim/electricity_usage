import click
import os
from xdg_base_dirs import xdg_data_home
from .areas import codes

@click.command()
@click.option('--area',type=click.Choice(codes), default='DE', help="area code according to 'electricity_usage areas'")

def start(area):
    '''starts the tool background process (demon)'''
    datadir = xdg_data_home()
    os.makedirs(os.path.join(datadir, 'electricity_usage/input_data'), exist_ok=True)
    input_dir = os.path.join(datadir, f'electricity_usage/input_data/input_dir_{area}')
    os.system(f'python3 daemon.py {area} {input_dir}')


