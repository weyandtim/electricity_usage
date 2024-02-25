import os
import platformdirs


#erstellt einen input_dir Ordner zur Kommunikation mit dem Daemon
def create_input_dir_path():
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
    input_dir = os.path.join(input_dirs_dir, 'input_dir')
    if not os.path.exists(input_dir):
        os.makedirs(input_dir)

    return input_dir



# gibt den Pfad zum input_dir Ordner zurück 
def get_input_dir_path():
    # Verzeichnis für Anwendungsdaten erhalten
    data_dir = platformdirs.user_data_dir(appname='electricity_usage')

    # input_dirs Verzeichnis erstellen
    input_dirs_dir = os.path.join(data_dir, 'input_dirs')

    # input_dir im input_dirs Verzeichnis erstellen
    input_dir = os.path.join(input_dirs_dir, 'input_dir')

    return input_dir


'''# Ausführung der Funktionen
create_input_dir_result = create_input_dir_path()
get_input_dir_result = get_input_dir_path()

# Ausgabe der Ergebnisse
print("Ergebnis von create_input_dir_path():", create_input_dir_result)
print("Ergebnis von get_input_dir_path():", get_input_dir_result)'''
