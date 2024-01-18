import client
import daemon
import threading
import time

"""client1 = client.Client(client_id=1, estimate=10, deadline="2023-12-31", area="DE", commandline="some_command")
print(client1.client_id)
print(client1.deadline)"""

# Erzeuge eine Instanz des Daemons
daemon_instance = daemon.Daemon.get_instance()

# Starte die Methode run des Daemons in einem separaten Thread
daemon_thread = threading.Thread(target=daemon_instance.run, daemon=True)
daemon_thread.start()

# Rufe die Methode start_client des Daemons auf
estimate = 100  # Beispielwert für die Schätzung
deadline = "2023-12-31"  # Beispielwert für die Frist
area = "DE"  # Beispielwert für den Bereich
commandline = "your_command_here"  # Beispielwert für die Befehlszeile
daemon_instance.start_client(estimate, deadline, area, commandline)

time.sleep(10)

daemon_instance1 = daemon.Daemon.get_instance() #daemon_instance1 und daemon_instance verweisen auf das gleiche Objekt, es existiert also nur ein Daemon
daemon_instance1.start_client(50, "2023-12-12", "DE", "test")

# Füge optional eine Verzögerung hinzu, um die Ausführung des Daemons und des Clients zu sehen
#time.sleep(30)

