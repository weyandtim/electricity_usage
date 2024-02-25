import string
import click
import os
import datetime
import random
from electricity_usage import data_dirs

# Pfad zum input_data-Ordner
input_data_dir = data_dirs.get_input_dir_path()

def generate_stop_token_filename():
    rand = ''.join(random.choice(string.ascii_letters) for _ in range(16))
    time_str = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"stop_token{rand}{time_str}.txt"
    return filename

@click.command()

def stop():
    '''stops the tool demon and abandons all processes'''
    #print('This will stop the tool later')
    filename = generate_stop_token_filename()  # Generiere den Dateinamen
    file_path = os.path.join(input_data_dir, filename)  # Kombiniert den Dateinamen mit dem Ordnerpfad
    with open(file_path, 'w'):
        pass
    print(f"Die Datei wurde erfolgreich im Ordner {input_data_dir} gespeichert: {filename}")

    '''input_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),'input_data')
    if os.path.exists(input_dir):
        if not os.listdir(input_dir):
            os.rmdir(input_dir)
        else: 
            print('Warning: There are still processes the the queue.')
            #yes/no abfrage einbauen für entgültigen abbruch
            for file in input_dir:
                os.remove(file)'''



