import json
import os
import pytest
import threading
import time 
from watchdog.events import FileSystemEvent
from electricity_usage.daemon import Daemon
from electricity_usage import em_data
from electricity_usage import job


@pytest.fixture
def daemon_instance():
    return Daemon(os.getenv("API_KEY"), 'DE')

def test_process_json_file(daemon_instance):
    # Erstelle eine Beispiel-JSON-Datei
    json_data = {"estimate": 100, "deadline": "2023-12-31", "commandline": 'echo "commandline ausgeführt"'}
    with open("input_data/test_data.json", "w") as file:
        json.dump(json_data, file)

    # Rufe die Methode auf
    daemon_instance.process_json_file("input_data/test_data.json")

    # Überprüfe, ob der Job korrekt hinzugefügt wurde
    assert len(daemon_instance.jobs) == 1
    assert daemon_instance.jobs[0].estimate == 100
    assert daemon_instance.jobs[0].deadline == "2023-12-31"
    assert daemon_instance.jobs[0].commandline == 'echo "commandline ausgeführt"'

def test_on_created(daemon_instance):
    # Erstelle eine Beispiel-JSON-Datei
    json_data = {"estimate": 200, "deadline": "2023-12-31", "commandline": "command2"}
    with open("input_data/test_data.json", "w") as file:
        json.dump(json_data, file)

    # Simuliere ein Ereignis für das Erstellen der JSON-Datei
    event = FileSystemEvent("input_data/test_data.json")
    daemon_instance.event_handler.on_created(event)

    # Überprüfe, ob die Methode process_json_file aufgerufen wurde
    assert len(daemon_instance.jobs) == 1
    assert daemon_instance.jobs[0].estimate == 200
    assert daemon_instance.jobs[0].deadline == "2023-12-31"
    assert daemon_instance.jobs[0].commandline == "command2"

# Zusätzlicher Test für das Beenden des Daemons
def test_stop(daemon_instance):
    # Starte den Daemon in einem separaten Thread
    daemon_thread = threading.Thread(target=daemon_instance.run, daemon=True)
    daemon_thread.start()

    # Warte einen Moment, um sicherzustellen, dass der Daemon Zeit hat zu starten
    time.sleep(2)

    # Rufe die Methode zum Beenden auf
    daemon_instance.stop()

    # Überprüfe, ob der Daemon beendet wurde
    daemon_thread.join(timeout=5)  # Warte maximal 5 Sekunden
    assert not daemon_thread.is_alive()

"""# Aufräumen nach den Tests
def teardown():
    os.remove("input_data/test_data.json")
"""