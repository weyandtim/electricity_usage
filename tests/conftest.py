import pytest
import json
import os
import platformdirs
from unittest.mock import MagicMock
from unittest.mock import patch
from click.testing import CliRunner
from electricity_usage import data_dirs

@pytest.fixture
def mock_em_data():
    with patch('electricity_usage.em_data.get_power_data') as mock_get_power_data:
        yield mock_get_power_data

@pytest.fixture
def create_temp_input_dir_path():
    # Get directory for application data
    data_dir = platformdirs.user_data_dir(appname='electricity_usage')
    # Create electricity_usage directory if it doesn't exist
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    # Create input_dirs directory if it doesn't exist
    input_dirs = os.path.join(data_dir, 'temp_input_dirs')
    if not os.path.exists(input_dirs):
        os.makedirs(input_dirs)
    # Create input_dir in the input_dirs directory if it doesn't exist
    input_dir = os.path.join(input_dirs, 'temp_input_dir')
    if not os.path.exists(input_dir):
        os.makedirs(input_dir)
    return input_dir

@pytest.fixture
def daemon_instance(create_temp_input_dir_path):
    from electricity_usage.daemon import Daemon
    daemon = Daemon(em_API_key='dummy_key', area='DE', input_dir=create_temp_input_dir_path)
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

@pytest.fixture
def runner():
    return CliRunner()
