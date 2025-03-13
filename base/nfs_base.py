from base.base_test import *


class NFSBaseTest(BaseTest):
    @pytest.fixture(autouse=True)
    def nfs_setup(self):
        # NFS-specific setup (e.g., mount NFS share)
        print("Setting up NFS Ganesha...")
        yield
        # NFS-specific teardown (e.g., unmount NFS share)
        print("Tearing down NFS Ganesha...")
