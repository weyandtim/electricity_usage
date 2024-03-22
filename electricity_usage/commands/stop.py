import string
import click
import os
import datetime
import random
from electricity_usage import data_dirs

# the "stop" command generates a file in the input directory.
# this file is then detected by the daemon, prompting it to perform its stop method

# path to input_data-directory
input_data_dir = data_dirs.get_input_dir_path()

def generate_stop_token_filename():
    rand = ''.join(random.choice(string.ascii_letters) for _ in range(16))
    time_str = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"stop_token{rand}{time_str}.txt"
    return filename

@click.command()

def stop():
    '''stops the tool demon and abandons all processes'''
    filename = generate_stop_token_filename()  # generates file name
    file_path = os.path.join(input_data_dir, filename)
    with open(file_path, 'w'):
        pass
    print(f"Die Datei wurde erfolgreich im Ordner {input_data_dir} gespeichert: {filename}")




