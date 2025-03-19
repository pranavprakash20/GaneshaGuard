from core.base_service import BaseService
from utils.config_loader import ConfigLoader

class NfsClient(BaseService):
    """Handles NFS mount, unmount, and I/O operations."""

    def __init__(self):
        self.config = ConfigLoader.load_config()
        self.server_ip = self.config["server"]["ip"]
        self.export_path = self.config["nfs"]["pseudo_path"]
        self.mount_point = self.config["nfs"]["mount_point"]

    def start(self):
        """Mounts the NFS share."""
        cmd = ["mount", "-t", "nfs", f"{self.server_ip}:{self.export_path}", self.mount_point]
        returncode, _, err = self.run_command(cmd)
        if returncode != 0:
            raise RuntimeError(f"NFS mount failed: {err}")

    def stop(self):
        """Unmounts the NFS share."""
        self.run_command(["umount", self.mount_point])
