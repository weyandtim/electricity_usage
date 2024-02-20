import click

with open('electricity_usage/area_codes.txt', encoding='utf-8') as f:
    areas = f.readlines() # read out all codes + translation
    # build list of codes to choose from
    codes = []
    for a in areas: 
        codes.append(a.split()[0])

@click.command()
def areas():
    '''shows list of possible area codes and the corresponding area codes'''
    print('Electricitymaps offers data from corresponding to the following areas\n')
    for a in areas:
        print(a)
