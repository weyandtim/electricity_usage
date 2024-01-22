import pytest
from electricity_usage.daemon import Daemon 


@pytest.fixture
def daemon_instance():
    return Daemon()