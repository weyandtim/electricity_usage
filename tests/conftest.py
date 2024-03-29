import pytest
import json
import os
from unittest.mock import MagicMock
from unittest.mock import patch
from electricity_usage import data_dirs

@pytest.fixture
def mock_em_data():
    with patch('electricity_usage.em_data.get_power_data') as mock_get_power_data:
        yield mock_get_power_data

@pytest.fixture
def daemon_instance():
    from electricity_usage.daemon import Daemon
    daemon = Daemon(em_API_key='dummy_key', area='DE', input_dir=data_dirs.create_input_dir_path())
    yield daemon
    daemon.stop()


@pytest.fixture
def create_accepted_json_files(daemon_instance):
    # Liste von akzeptierten Daten für die JSON-Dateien
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

@pytest.fixture
def mock_create_input_dir_path():
    yield data_dirs.get_input_dir_path()
