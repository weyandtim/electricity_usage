import json
import threading
import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import em_data
import client
import job

class Daemon:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.client_threads = []
            self.next_client_id = 1
            self.jobs = []  # Liste, um Jobs zu speichern
            self.lock = threading.Lock()
            self.initialized = True
            self.next_job_id = 1  # Hinzugefügte Variable für die Job-ID
            self.stop_event = threading.Event()  # Event für das Beenden des Daemon-Threads

            # Watchdog Setup
            self.event_handler = CustomFileSystemEventHandler(self)
            self.observer = Observer()
            self.observer.schedule(self.event_handler, path='input_data', recursive=False) #recursive
            self.observer.start()


    def run(self):
        while not self.stop_event.is_set():
            print("Daemon is running...")
            auth_token = "your_auth_token_here"
            power_production, power_consumption = em_data.get_power_breakdown(auth_token=auth_token)
            time.sleep(2)

        print("Daemon is terminating...")
        self.observer.stop()
        self.observer.join()  # Warten, bis der Observer-Thread beendet ist


    def stop(self):
        self.stop_event.set()  # Setzen Sie das Event, um den Daemon-Thread zu beenden


    def process_json_file(self, file_path):
        print("Daemon Methode ausgeführt")
        print("job hinzugefügt")
        with open(file_path, 'r') as file:
            params = json.load(file)
        
        # Extract parameters and call start_client
        area = params.get('area')
        estimate = params.get('estimate')
        deadline = params.get('deadline')
        commandline = params.get('commandline')

        if area and estimate and deadline and commandline:
            with self.lock:
                # Erhöhe die job_id vor der Verwendung um sicherzustellen, dass sie fortlaufend ist
                job_id = self.next_job_id
                self.next_job_id = self.next_client_id+1
                new_job=f"job{job_id}" #jobs werden wie folgt benannt: job1, job2, ...
                new_job = job.Job(job_id, estimate, deadline, area, commandline)
                self.jobs.append(new_job) #fügt den job des Liste jobs hinzu
                print(f"Job {job_id} added.")

    """def start_client(self, estimate, deadline, area, commandline):
        with self.lock:
            client_id = self.next_client_id
            self.next_client_id += 1

        print(f"Starting client {client_id}")
        client_instance = client.Client(client_id=client_id, estimate=estimate, deadline=deadline, area=area, commandline=commandline)
        print("Client wurde erstellt")
        client_thread = threading.Thread(target=client_instance.run, daemon=False)
        client_thread.start()

        with self.lock:
            self.client_threads.append({"id": client_id, "thread": client_thread})"""


class CustomFileSystemEventHandler(FileSystemEventHandler):
    def __init__(self, daemon_instance):
        super().__init__()
        self.daemon_instance = daemon_instance

    def on_created(self, event):
        if event.is_directory:
            return
        elif event.event_type == 'created' and event.src_path.endswith('.json'):
            print(f"New JSON file detected: {event.src_path}")
            self.daemon_instance.process_json_file(event.src_path) #ruft die Methode process_json_file des Daemons auf
                



if __name__ == "__main__":
    # Erstellen Sie den input_data-Ordner, wenn er nicht existiert
    os.makedirs("input_data", exist_ok=True)

    # Instanziieren Sie den Daemon
    daemon = Daemon()

    # Starten Sie die run-Methode des Daemons in einem separaten Thread
    daemon_thread = threading.Thread(target=daemon.run, daemon=True)
    daemon_thread.start()

    # Warten Sie einen Moment, um sicherzustellen, dass der Daemon Zeit hat zu starten
    #time.sleep(2)

    if daemon.observer.is_alive():
        print("Observer aktiv")

    # Erstellen Sie einige Beispiel-JSON-Dateien im input_data-Ordner
    json_data_1 = {"area": "Area1", "estimate": 100, "deadline": "2023-12-31", "commandline": "command1"}
    json_data_2 = {"area": "Area2", "estimate": 200, "deadline": "2023-12-31", "commandline": "command2"}

    with open("input_data/data1.json", "w") as file:
        json.dump(json_data_1, file)

    with open("input_data/data2.json", "w") as file:
        json.dump(json_data_2, file)

    time.sleep(6)

    daemon.stop()
    # Warten Sie auf die Beendigung des Daemon-Threads
    #daemon_thread.join()
