import pytest
from unittest.mock import patch, MagicMock
import platformdirs
import os
import time
from click.testing import CliRunner
from electricity_usage.__main__ import cli
from electricity_usage.commands.area_codes import areas_str
from electricity_usage.data_dirs import get_input_dir_path


@pytest.fixture
def runner():
    return CliRunner()
@pytest.fixture
def data_dir():
    data_dir = platformdirs.user_data_dir(appname='electricity_usage')
    return data_dir

######  areas  ######
def test_areas_command(runner):
    longstring = "ElectricityMaps offers data from areas corresponding to the following areas\n"
    for a in areas_str:
        longstring = longstring + f"\n{a}"
    longstring = longstring + "\n"
    result = runner.invoke(cli, ['areas'])
    assert result.exit_code == 0
    assert result.output == longstring


######  queue  ######
def test_queue_command(runner):
    result = runner.invoke(cli, ['queue'])
    test_path = get_input_dir_path()
    assert result.exit_code == 0
    assert test_path in result.output


######  start  ######
def test_start_command_default(runner, daemon_instance):
    result = runner.invoke(cli, ['start'], ['daemon_instance', daemon_instance])
    
    assert result.exit_code == 0

def test_start_command_with_valid_area(runner):
    result = runner.invoke(cli, ['start', '--area', 'BE'])
    assert result.exit_code == 0

def test_start_command_with_invalid_area(runner):
    result = runner.invoke(cli, ['start', '--area', 'FF'])
    assert result.exit_code == 2


######  run  ######
def test_run_command_valid(runner, data_dir):
    result = runner.invoke(cli, ['run', '--estimate 1 --deadline "2025-02-22" --commandline "command"'])
    #assert result.exit_code == 0
    assert os.path.isdir(os.path.join(data_dir, 'input_dirs/input_data')) == True

######  stop  ######
def test_stop_command_valid(runner, data_dir):
    result = runner.invoke(cli, ['stop'])
    assert result.exit_code == 0
    time.sleep(2)  #wait for stop command to be done deleting directories
    assert os.path.isdir(data_dir)==False
