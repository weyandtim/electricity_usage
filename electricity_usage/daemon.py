import json
import threading
import os
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

            # commandline ausführen wenn Strom da ist
            if power_production is not None and power_consumption is not None:
                if power_consumption < power_production:
                    # run processes
                    with self.lock:
                        for job_instance in self.jobs:
                            commandline = job_instance.commandline
                            job_id = job_instance.job_id
                            print(f"Executing commandline for Job {job_id}: {commandline}")
                            # Führe die Commandline aus
                            subprocess.run(commandline, shell=True, check=True)
                            # lösche den job aus der Liste self.jobs damit er nicht nochmal ausgeführt wird
                            self.jobs.remove(job_instance)

            # commandline ausführen um die deadline zu halten
            with self.lock:
                for job_instance in self.jobs:  
                    # Berechne den Zeitpunkt deadline - estimate
                    latest_starting_point = job_instance.deadline - datetime.timedelta(hours=job_instance.estimate)
                    # Überprüfe, ob latest_starting_point kleiner oder gleich der aktuellen Zeit ist
                    if latest_starting_point <= datetime.datetime.now():
                        commandline = job_instance.commandline
                        job_id = job_instance.job_id
                        print(f"Executing commandline for Job {job_id}: {commandline}")
                        # Führe die Commandline aus
                        subprocess.run(commandline, shell=True, check=True)
                        # lösche den job aus der Liste self.jobs damit er nicht nochmal ausgeführt wird
                        self.jobs.remove(job_instance)

            # time.sleep(900)
            self.stop_event.wait(timeout=10)

        self.observer.stop()  # Observer-Thread beenden
        self.observer.join()  # Warten bis der Observer-Thread beendet ist"""
        print("Daemon Terminated")



    def stop(self):
        self.stop_event.set()  # Stop Event setzen, um den Daemon-Thread zu beenden
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
        try:
            with open(file_path, 'r') as file:
                params = json.load(file)
        
            # Parameter auslesen
            estimate = float(params.get('estimate'))
            deadline = datetime.datetime.strptime(params.get('deadline'), "%Y-%m-%d %H:%M:%S")
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
                    
        except Exception as e:
            print("Something went wrong. Please check your input Parameters (estimate, daedline, commandline)")
    


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
   
