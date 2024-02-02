import pytest
import os
from electricity_usage.daemon import Daemon 
from electricity_usage import em_data


@pytest.fixture
def daemon_instance():
    return Daemon(os.getenv("API_KEY"))