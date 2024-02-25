import click
from .area_codes import areas_str

# build list of codes to choose from
codes = []
for a in areas_str: 
    codes.append(a.split()[0])

@click.command()
def areas():
    '''shows list of possible area codes and the corresponding area codes'''
    print('Electricitymaps offers data from corresponding to the following areas\n')
    for a in areas_str:
        print(a)
