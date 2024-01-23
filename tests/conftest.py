import pytest
from electricity_usage.daemon import Daemon 
from electricity_usage import em_data


@pytest.fixture
def daemon_instance():
    return Daemon()