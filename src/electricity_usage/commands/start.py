import click
import os

area_list=['DE','BE']

@click.command()
@click.option('--area',type=click.Choice(area_list), default='DE', help="area code according to 'electricity_usage areas'")

def start(area):
    '''starts the tool background process (demon)'''
    input_dir = os.path.join((os.path.dirname(os.path.abspath(__file__))),f'input_data_{area}')
    os.system(f'python3 daemon.py')# {area}')

