import pytest
from core.ganesha_service import NfsGaneshaService

@pytest.fixture(scope="session", autouse=True)
def setup_nfs_ganesha():
    """Starts NFS-Ganesha before tests and stops after."""
    ganesha = NfsGaneshaService()
    ganesha.start()
    yield ganesha
    ganesha.stop()
