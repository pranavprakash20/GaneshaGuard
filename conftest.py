import pytest

@pytest.fixture(scope="session")
def nfs_server():
    return "nfs-server-ip"

@pytest.fixture(scope="session")
def ceph_cluster():
    return "ceph-cluster-ip"