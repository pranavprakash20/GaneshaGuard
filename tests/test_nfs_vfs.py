import pytest
from core.nfs_client import NfsClient


@pytest.mark.usefixtures("setup_nfs_ganesha")
def test_nfs_mount_vfs():
    """Tests mounting an NFS export with VFS backend."""
    client = NfsClient()
    client.start()
    assert client.run_command(["mountpoint", "-q", client.mount_point])[0] == 0, "Mount failed!"
    client.stop()

def test_file_creation():
    """Tests creating a file on NFS mount."""
    client = NfsClient()
    client.start()
    test_file = f"{client.mount_point}/testfile.txt"
    assert client.run_command(["touch", test_file])[0] == 0, "File creation failed!"
    client.stop()
