import click
import json
import os
import random
import string
from datetime import datetime
from electricity_usage.commands.areas import codes
from electricity_usage import data_dirs 

input_data_directory = data_dirs.get_input_dir_path()


def generate_filename():
    rand = ''.join(random.choice(string.ascii_letters) for _ in range(16))
    time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return f"{time}_{rand}.json"

@click.command()
@click.option('--estimate', type=float, help='estimated runtime of the program in hours', required=True)
@click.option('--deadline', type=click.DateTime(formats=['%Y-%m-%d', '%Y-%m-%dT%H:%M:%S', '%Y-%m-%d %H:%M:%S']), help='latest date when the program should be finished', required=True)
@click.option('--commandline', type=str, help='the command line to be executed', required=True)

def run(estimate,deadline,commandline): 
    if deadline.time() == datetime.min.time():  # Wenn die Uhrzeit nicht im Parameter enthalten ist
        deadline = deadline.replace(hour=0, minute=0, second=0)  # Setze die Uhrzeit auf 00:00:00

    
    deadline_str = deadline.strftime("%Y-%m-%d %H:%M:%S")
    data = {
        "estimate": estimate,
        "deadline": deadline_str,
        "commandline": commandline
    }
    
    json_document = json.dumps(data)
    json_filename = generate_filename()
    print('argumente entgegen genommen')
    with open(os.path.join(input_data_directory, json_filename), 'w') as f:
        f.write(json_document)
    
    return os.path.join(input_data_directory, json_filename)

