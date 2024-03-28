import json
import os
import time
import threading
import datetime
from unittest.mock import patch, MagicMock
from electricity_usage.job import Job


### testing creating daemon instance ###

def test_create_daemon_instance(daemon_instance):
    assert daemon_instance.em_API_key == 'dummy_key'
    assert daemon_instance.area == 'DE'
    assert os.path.exists(daemon_instance.input_dir)
    assert hasattr(daemon_instance, 'observer')  # Observer sollte erstellt worden sein
    assert len(os.listdir(daemon_instance.input_dir)) == 0  # Überprüfe, ob alle Dateien im Eingabeverzeichnis gelöscht wurden



### testting process_json_file ###

def test_process_json_file_with_valid_data(daemon_instance):
    # Test with valid JSON data
    file_path = 'valid_data.json'
    data = {
        'estimate': 2.0,
        'deadline': '2024-03-05 12:00:00',
        'commandline': 'python script.py'
    }
    with open(file_path, 'w') as file:
        json.dump(data, file)

    daemon_instance.process_json_file(file_path)
    assert len(daemon_instance.jobs) == 1

    os.remove(file_path)


def test_process_json_file_with_invalid_data(daemon_instance):
    # Test with invalid JSON data
    file_path = 'invalid_data.json'
    data = {
        'invalid_field': 'invalid_value'
    }
    with open(file_path, 'w') as file:
        json.dump(data, file)

    daemon_instance.process_json_file(file_path)
    assert len(daemon_instance.jobs) == 0

    os.remove(file_path)



### testing run ###

def test_run_production_greater_consumption(daemon_instance, mock_em_data):
    mock_em_data.return_value = (100, 50) # Mock power production and consumption data

    # Add a job with a commandline
    job = Job(job_id=1, estimate=1.0, deadline=datetime.datetime.now() + datetime.timedelta(hours=2), commandline='echo command executed')
    daemon_instance.jobs.append(job)

    # Mock subprocess.run
    with patch('subprocess.run') as mock_subprocess_run:
        # Define a function to run the daemon's run method in a separate thread. damit keine endlosschleife entsteht
        def run_daemon():
            daemon_instance.run()
        # Start the daemon's run method in a separate thread
        daemon_thread = threading.Thread(target=run_daemon)
        daemon_thread.start()

        time.sleep(1) # Wait for a short time to allow the daemon to execute
        daemon_instance.stop() # Stop the daemon by calling the stop method
        daemon_thread.join() # Wait for the daemon thread to finish
        mock_subprocess_run.assert_called_once_with('echo command executed', shell=True, check=True) # Check if the subprocess.run method was called with the correct command
        assert len(daemon_instance.jobs) == 0 # Check if the jobs list is empty


def test_run_latest_StartingPoint_reached(daemon_instance, mock_em_data):
    mock_em_data.return_value = (50, 100) # Mock power production and consumption data

    # Add a job with a commandline
    job = Job(job_id=1, estimate=3.0, deadline=datetime.datetime.now() + datetime.timedelta(hours=2), commandline='echo command executed')
    daemon_instance.jobs.append(job)

    # Mock subprocess.run
    with patch('subprocess.run') as mock_subprocess_run:
        # Define a function to run the daemon's run method in a separate thread. Avoiding endless loop
        def run_daemon():
            daemon_instance.run()

        # Start the daemon's run method in a separate thread
        daemon_thread = threading.Thread(target=run_daemon)
        daemon_thread.start()

        time.sleep(1) # Wait for a short time to allow the daemon to execute
        daemon_instance.stop() # Stop the daemon by calling the stop method
        daemon_thread.join() # Wait for the daemon thread to finish
        mock_subprocess_run.assert_called_once_with('echo command executed', shell=True, check=True) # Check if the subprocess.run method was called with the correct command
        assert len(daemon_instance.jobs) == 0  # Check if the jobs list is empty


def test_run_no_conditions_met(daemon_instance, mock_em_data):
    mock_em_data.return_value = (50, 100) # Mock power production and consumption data

    # Add a job with a commandline
    job = Job(job_id=1, estimate=3.0, deadline=datetime.datetime.now() + datetime.timedelta(hours=10), commandline='echo command executed')
    daemon_instance.jobs.append(job)

    # Mock subprocess.run
    with patch('subprocess.run') as mock_subprocess_run:
        # Define a function to run the daemon's run method in a separate thread.
        def run_daemon():
            daemon_instance.run()
        
        # Start the daemon's run method in a separate thread
        daemon_thread = threading.Thread(target=run_daemon)
        daemon_thread.start()
        time.sleep(1)  # Wait for a short time to allow the daemon to execute
        daemon_instance.stop() # Stop the daemon by calling the stop method
        daemon_thread.join() # Wait for the daemon thread to finish
        mock_subprocess_run.assert_not_called() # Check if the subprocess.run method was not called
        assert len(daemon_instance.jobs) == 1  # One job should remain in the list as no conditions were met



### testing stop ###
        
def test_stop_removes_txtfiles(daemon_instance):
    # Füge einige Dummy-Dateien im Eingabeverzeichnis hinzu
    file_names = ['file1.txt', 'file2.txt', 'file3.txt']
    for file_name in file_names:
        file_path = os.path.join(daemon_instance.input_dir, file_name)
        open(file_path, 'w').close()  # Erstellt eine leere Datei

    # Rufe die stop() Methode auf, um die Dateien zu löschen
    daemon_instance.stop()
    time.sleep(1) #gibt dem Daemon Zeit die stopmethode auszuführen
    # Überprüfe, ob input_dir gelöscht wurde und damit auch alle txt files
    assert not os.path.exists(daemon_instance.input_dir)
    

def test_stop_remove_jsonfiles(daemon_instance, create_accepted_json_files):
    accepted_data = [
        {
            'estimate': 2.0,
            'deadline': '2024-03-05 12:00:00',
            'commandline': 'python script.py'
        },
        {
            'estimate': 3.0,
            'deadline': '2024-03-06 12:00:00',
            'commandline': 'python script2.py'
        }
    ]

    # Erstelle JSON-Dateien mit den akzeptierten Daten
    for i, data in enumerate(accepted_data):
        file_path = os.path.join(daemon_instance.input_dir, f'accepted_data_{i}.json')
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file)
        
    daemon_instance.stop()
    time.sleep(1)
    # Überprüfe, ob input dir und damit auch alle json files gelöscht wurden
    assert not os.path.exists(daemon_instance.input_dir)


### testing Observer calls Method ###

def test_process_json_file_called(daemon_instance):
    # Erzeuge eine JSON-Datei im input_dir
    json_data = {
        'estimate': 2.0,
        'deadline': '2024-03-05 12:00:00',
        'commandline': 'python script.py'
    }
    json_file_path = os.path.join(daemon_instance.input_dir, 'test.json')
    with open(json_file_path, 'w') as json_file:
        json.dump(json_data, json_file)
    time.sleep(1)
    # Überprüfe, ob die process_json_file-Methode aufgerufen wurde
    assert len(daemon_instance.jobs) == 1
    assert daemon_instance.jobs[0].estimate == 2.0
    assert daemon_instance.jobs[0].deadline == datetime.datetime(2024, 3, 5, 12, 0, 0)
    assert daemon_instance.jobs[0].commandline == 'python script.py'


def test_stop_method_called(daemon_instance):
    # Erzeuge eine TXT-Datei im input_dir
    txt_file_path = os.path.join(daemon_instance.input_dir, 'test.txt')
    with open(txt_file_path, 'w') as txt_file:
        txt_file.write('Stop')

    # Überprüfe, ob die stop-Methode aufgerufen wurde
    assert len(os.listdir(daemon_instance.input_dir)) == 1
    assert len(daemon_instance.jobs) == 0  # Es sollte keine Jobs geben, da der Daemon gestoppt wurde


