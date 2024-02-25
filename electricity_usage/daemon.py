import json
import threading
import time
import os
import sys
import subprocess
import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from electricity_usage import job
from electricity_usage import em_data

class Daemon:
    _instance = None
    _lock = threading.Lock()

    def __init__(self, em_API_key, area, input_dir):
        if not hasattr(self, 'initialized'):
            self.jobs = []  # Liste, um Jobs zu speichern
            self.lock = threading.Lock()
            self.initialized = True
            self.next_job_id = 1  # Hinzugefügte Variable für die Job-ID
            self.stop_event = threading.Event()  # Event für das Beenden des Daemon-Threads
            self.em_API_key = em_API_key
            self.area = area
            self.input_dir = input_dir

            # Watchdog Setup
            self.event_handler = CustomFileSystemEventHandler(self)
            self.observer = Observer()
            self.observer.schedule(self.event_handler, path=input_dir, recursive=False) #recursive
            self.observer.start()


    def run(self):
        while not self.stop_event.is_set():
            print("Daemon is running...")
            
            power_production, power_consumption = em_data.get_power_data(self.area, self.em_API_key)
            print(power_production, power_consumption)

            # check conditions
            if power_production is not None and power_consumption is not None:
                if power_consumption < power_production:
                    # run processes
                    with self.lock:
                        for job_instance in self.jobs:
                            deadline = datetime.datetime.strptime(job_instance.deadline,"%Y-%m-%d %H:%M:%S")
                            if deadline <= datetime.datetime.now():
                                commandline = job_instance.commandline
                                job_id = job_instance.job_id
                                print(f"Executing commandline for Job {job_id}: {commandline}")

                                # Führe die Commandline aus
                                subprocess.run(commandline, shell=True, check=True)
            
            # time.sleep(900)
            time.sleep(10)

        print("Daemon is terminating...")
        self.observer.stop()
        self.observer.join()  # Warten, bis der Observer-Thread beendet ist


    def stop(self):
        self.stop_event.set()  # Setzen Sie das Event, um den Daemon-Thread zu beenden
        try:
            # Überprüfen, ob der Ordner existiert
            if os.path.exists(self.input_dir):
                # Liste aller Dateien im Ordner
                files = os.listdir(self.input_dir)
                for file_name in files:
                    # Pfad zur Datei erstellen
                    file_path = os.path.join(self.input_dir, file_name)
                    # Überprüfen, ob das Element ein reguläres File ist
                    if os.path.isfile(file_path):
                        # Datei löschen
                        os.remove(file_path)
                print("Alle Dateien im Ordner wurden erfolgreich gelöscht.")
            else:
                print(f"Der Ordner {self.input_dir} existiert nicht.")
        except Exception as e:
            print(f"Fehler beim Löschen der Dateien: {str(e)}")



    def process_json_file(self, file_path):
        print("Daemon process_json_file Methode ausgeführt")
        with open(file_path, 'r') as file:
            params = json.load(file)
        
        # Extract parameters and call start_client
        estimate = params.get('estimate')
        deadline = params.get('deadline')
        commandline = params.get('commandline')

        if estimate and deadline and commandline:
            with self.lock:
                # Erhöhe die job_id vor der Verwendung um sicherzustellen, dass sie fortlaufend ist
                job_id = self.next_job_id
                self.next_job_id = self.next_job_id+1
                new_job=f"job{job_id}" #jobs werden wie folgt benannt: job1, job2, ...
                new_job = job.Job(job_id, estimate, deadline, commandline)
                self.jobs.append(new_job) #fügt den job des Liste jobs hinzu
                print(f"Job {job_id} added.")

    


class CustomFileSystemEventHandler(FileSystemEventHandler):
    def __init__(self, daemon_instance):
        super().__init__()
        self.daemon_instance = daemon_instance

    def on_created(self, event):
        if event.is_directory:
            print("event erkannt")
            return
        elif event.event_type == 'created':
            if event.src_path.endswith('.json'):#ruft die Methode process_json_file des Daemons auf
                print(f"New JSON file detected: {event.src_path}")
                self.daemon_instance.process_json_file(event.src_path)     
            elif event.src_path.endswith('txt'):#ruft die Methode stop des Daemons auf
                print("Stop token file detected. Stopping daemon.")
                self.daemon_instance.stop() 



'''elif event.src_path.startswith('stop_token'):#ruft die Methode stop des Daemons auf
                print("Stop token file detected. Stopping daemon.")
                self.daemon_instance.stop() '''   

if __name__ == "__main__":

    # use given arguments (cf commands/start.py)
    area = sys.argv[1]
    input_dir = sys.argv[2]

    # Erstellen Sie den input_data-Ordner, wenn er nicht existiert
    os.makedirs(input_dir, exist_ok=True)

    # Instanziieren Sie den Daemon
    daemon = Daemon(os.getenv("API_KEY"), 'DE', 'C:\git\electricity_usage\input_data')

    # Starten Sie die run-Methode des Daemons in einem separaten Thread
    daemon_thread = threading.Thread(target=daemon.run) #daemon=True darf nicht gesetzt werden
    daemon_thread.start()

    if daemon.observer.is_alive():
        print("Observer aktiv")

    # Erstellen Sie einige Beispiel-JSON-Dateien im input_data-Ordner
    '''json_data_1 = { "estimate": 100, "deadline": "2023-12-31", "commandline": 'echo "test erfolgreich"'}
    json_data_2 = { "estimate": 200, "deadline": "2023-12-31", "commandline": 'echo "test 2 erfolgreich"'}
    
    with open("input_data/data1.json", "w") as file:
        json.dump(json_data_1, file)

    with open("input_data/data2.json", "w") as file:
        json.dump(json_data_2, file)


    with open("input_data/stop_token213.txt", 'w'):
        pass'''

    time.sleep(15)

    #daemon.stop()
