import json
import threading
import time
import em_data
import client

#Daemon als Singleton damit nur eine Instanz existieren kann
class Daemon:
    _instance = None
    _lock = threading.Lock()


    @classmethod
    def get_instance(cls):
        with cls._lock:
            if not cls._instance:
                cls._instance = cls()
        return cls._instance
    

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.client_threads = []
            self.next_client_id = 1
            self.lock = threading.Lock()
            self.initialized = True


    def run(self):
        while True:
            print("Daemon is running...")
            auth_token = "your_auth_token_here"
            power_production, power_consumption = em_data.get_power_breakdown(auth_token=auth_token)
            time.sleep(5)


    def start_client(self, estimate, deadline, area, commandline):
        with self.lock:
            client_id = self.next_client_id
            self.next_client_id += 1

        print(f"Starting client {client_id}")
        client_instance = client.Client(client_id=client_id, estimate=estimate, deadline=deadline, area=area, commandline=commandline)
        print("client wurde erstellt")
        client_thread = threading.Thread(target=client_instance.run, daemon=False)
        client_thread.start()

        with self.lock:
            self.client_threads.append({"id": client_id, "thread": client_thread})
#####



"""def read_params(filename):
    with open(filename, 'r') as file:
        params = json.load(file)
    return params

if __name__ == "__main__":
    params = read_params('datatransfer.json')
    print("Gelesene Parameter:", params)
    
    #zugriff auf einzelne Parameter
    area = params['area']
    print("area:", area)"""