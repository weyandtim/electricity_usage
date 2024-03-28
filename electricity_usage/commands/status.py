import click
import os
from ..em_data import get_power_data
from ..data_dirs import get_input_dir_path
from .area_codes import codes

def validate_code(ctx, param, area):
    if (area in codes) or (area==None):
        return area
    raise click.BadParameter("Area Code must be in the list of provided codes, not {area}")

@click.command()
@click.option("--area", type=str, required=False, callback=validate_code, help="If you wish to check the status of your connection to the Electricity Maps API, enter your area code and it will be provided for you.")

def status(area):
    '''shows a list of processes in queue and optionally the current connection status to Electricity Maps'''
    path_to_dir = get_input_dir_path()
    print(f"In your input directory {path_to_dir}, you currently have the following jobs in your queue:\n")
    files = [f for f in path_to_dir if os.path.isfile(os.path.join(path_to_dir, f))]
    for f in files:
        #with open(f) as j:
        #    c = j.commandline
        #    print(f, c)
        print(f)
    print("\n")
    if(area!=None):
        print("Electricity Maps Info:")
        prod, con = get_power_data(area, os.getenv("EM_API_KEY"))
        print("Power Production:", prod, "\nPower Consuption:", con, "\nDifference:", prod-con)

    
