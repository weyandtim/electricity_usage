import pytest
from mock import patch
from click.testing import CliRunner
from electricity_usage.__main__ import cli

@pytest.fixture
def runner():
    return CliRunner()

######  areas  ######
def test_areas_command(runner):
    result = runner.invoke(cli, ['areas'])
    assert result.exit_code == 0

######  queue  ######
def test_queue_command(runner):
    pass

#@patch('electricity_usage.daemon.Daemon')
#def blubb():
#    pass


######  start  ######
def test_start_command_default(runner):
    result = runner.invoke(cli, ['start'])
    assert result.exit_code == 0

def test_start_command_with_valid_area(runner):
    result = runner.invoke(cli, ['start', '--area', 'BE'])
    assert result.exit_code == 0

def test_start_command_with_invalid_area(runner):
    result = runner.invoke(cli, ['start', '--area', 'FF'])
    assert result.exit_code == 2

######  stop  ######
def test_stop_command_default(runner):
    result = runner.invoke(cli, ['stop'])
    assert result.exit_code == 0
