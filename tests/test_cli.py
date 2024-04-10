import pytest
import click
from unittest.mock import patch, MagicMock
import platformdirs
import os
import time
from electricity_usage.__main__ import cli
from electricity_usage.commands.area_codes import areas_str
from electricity_usage.data_dirs import get_input_dir_path


#@pytest.fixture
#def data_dir():
#    data_dir = platformdirs.user_data_dir(appname='electricity_usage')
#    return data_dir

######  areas  ######
def test_areas_command(runner):
    longstring = "ElectricityMaps offers data from areas corresponding to the following areas\n"
    for a in areas_str:
        longstring = longstring + f"\n{a}"
    longstring = longstring + "\n"
    result = runner.invoke(cli, ['areas'])
    assert result.exit_code == 0
    assert result.output == longstring


######  status  ######
def test_status_command_default(runner):
    #with patch('path_to_dir') as create_temp_input_dir_path:
    result = runner.invoke(cli, ['status'])
    test_path = get_input_dir_path()
    assert result.exit_code == 0
    assert test_path in result.output

def test_status_invalid_area(runner):
    result = runner.invoke(cli, ['status','--area','FF'])
    assert result.exit_code == 2

def test_status_valid_area(runner, mock_em_data):
    with patch('electricity_usage.em_data.get_power_data') as mock_em_data
    result = runner.invoke(cli, ['status','--area', 'DE'])
    assert result.exit_code == 0
    assert "Electricity Maps" in result.output

