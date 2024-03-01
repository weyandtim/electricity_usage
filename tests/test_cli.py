from click.testing import CliRunner
from electricity_usage.__main__ import cli


def test_start_command():
    runner = CliRunner()
    result = runner.invoke(cli, ['start', '--area', 'BE'])
    assert result.exit_code == 0

def test_start_command_default():
    runner = CliRunner()
    result = runner.invoke(cli, ['start'])
    assert result.exit_code == 0

def test_areas_command():
    runner = CliRunner()
    result = runner.invoke(cli, ['areas'])
    assert result.exit_code == 0
