import threading
import time

class Client:
    def __init__(self, client_id, estimate, deadline, area, commandline):
        self.client_id = client_id
        self.estimate = estimate
        self.deadline = deadline
        self.area = area
        self.commandline = commandline

    def run(self):
        run_time = 10  # Laufzeit in Sekunden
        interval = 2   # Ausgabintervall in Sekunden
        end_time = time.time() + run_time

        while time.time() < end_time:
            print(f"Client {self.client_id} is running...")
            time.sleep(interval)

        print(f"Client {self.client_id} has terminated.")

