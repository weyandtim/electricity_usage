import click
import json
import os
import random
import string
from datetime import datetime
from areas import codes


## Verzeichnis für die Eingabedaten im Ordner der Datei run.py erstellen, falls es noch nicht existiert
#input_data_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input_data')
#if not os.path.exists(input_data_directory):
#    os.makedirs(input_data_directory)

# define input_dir
input_data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'../input_data')
dirs = os.listdir(input_data_path)

def generate_filename():
    rand = ''.join(random.choice(string.ascii_letters) for i in range(16))
    time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return time+'_'+rand

@click.command()
@click.option('--estimate', type=float, help='estimated runtime of the program in hours') #timedelta
@click.option('--deadline', type=click.DateTime(formats=['%Y-%m-%d', '%Y-%m-%dT%H:%M:%S', '%Y-%m-%d %H:%M:%S']), help='latest date when the program should be finished')
@click.option('--area',type=click.Choice(codes), default=None, help="area code according to codes provided in areas command")
@click.option('--commandline', type=str, help='the command line to be executed')

def run(estimate,deadline,area,commandline):
    '''adds a process to the queue'''
    # define input directory path
    if len(dirs) == 1:
        input_dir = os.path.join(input_data_path, dirs[0])
    else if area:
        input_dir = os.path.join(input_data_path, f'input_dir_{area}')
    else:
        print('Please specify an area when more than one daemon is in use.')
        return
    # solution for only one area at once
    # input_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input_data')

    print(f"Input: estimate {estimate}, deadline {deadline}, commandline {commandline}")
    deadline_str = deadline.strftime("%Y-%m-%d %H:%M:%S") #wandelt click.DateTime in String um, weil click.DateTime nicht json kompatibel ist
    data = {
        "estimate": estimate,
        "deadline": deadline_str,
        "commandline": commandline
    }
	
    # Das JSON-Dokument erstellen
    json_document = json.dumps(data)

    # Den Dateinamen für das JSON-Dokument erstellen
    json_filename = generate_filename()+'.json'

    # Den JSON-Dokument im Ordner input_data speichern
    with open(os.path.join(input_dir, json_filename), 'w') as f:
        f.write(json_document)

    # Die Datei-URL zurückgeben
    return os.path.join(input_dir, json_filename)


