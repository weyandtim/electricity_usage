import os
#import platformdirs
from xdg_base_dirs import xdg_data_home


#erstellt einen input_dir Ordner zur Kommunikation mit dem Daemon
def create_input_dir_path(area):
    '''
    # Verzeichnis für Anwendungsdaten erhalten
    data_dir = platformdirs.user_data_dir(appname='electricity_usage')
    
    # electricity_usage Verzeichnis erstellen, wenn es nicht existiert
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # input_dirs Verzeichnis erstellen, wenn es nicht existiert
    input_dirs_dir = os.path.join(data_dir, 'input_dirs')
    if not os.path.exists(input_dirs_dir):
        os.makedirs(input_dirs_dir)

    # input_dir im input_dirs Verzeichnis erstellen, wenn es nicht existiert
    input_dir = os.path.join(input_dirs_dir, f'input_dir_{area}')
    if not os.path.exists(input_dir):
        os.makedirs(input_dir)
    '''

    # alternative for xdg-base-dirs
    data_dir = xdg_data_home()
    os.makedirs(os.path.join(data_dir, 'electricity_usage/input_data'), exist_ok=True)
    os.makedirs(os.path.join(data_dir, 'electricity_usage/input_data/input_dirs'), exist_ok=True)
    input_dir = os.path.join(data_dir, f'electricity_usage/input_data/input_dirs/input_dir_{area}')
    os.makedirs(input_dir, exist_ok=True)

    return input_dir



# gibt den Pfad zum input_dir Ordner zurück 
def get_input_dir_path(area):
    '''
    # Verzeichnis für Anwendungsdaten erhalten
    data_dir = platformdirs.user_data_dir(appname='electricity_usage')

    # input_dirs Verzeichnis erstellen
    input_dirs_dir = os.path.join(data_dir, 'input_dirs')

    # input_dir im input_dirs Verzeichnis erstellen
    input_dir = os.path.join(input_dirs_dir, f'input_dir_{area}')
    '''

    # aternative for xdg-base-dirs
    data_dir = xdg_data_home()
    input_dir = os.path.join(data_dir, f'electricity_usage/input_data/input_dirs/input_dir_{area}')

    return input_dir

