import os
import time
from core.base_service import BaseService
from utils.config_loader import ConfigLoader

GANESHA_CONF_TEMPLATE = """\
EXPORT {{
    Export_ID=1;
    Path = "{export_path}";
    Pseudo = "{pseudo_path}";
    Access_Type = RW;
    Protocols = 4;
    Transports = TCP;
    SecType = "sys";
    FSAL {{
        Name = "{fsal_name}";
    }}
}}
"""

class NfsGaneshaService(BaseService):
    """Manages the NFS-Ganesha service lifecycle."""

    def __init__(self):
        self.config = ConfigLoader.load_config()
        self.ganesha_bin = self.config["server"]["ganesha_bin_path"]
        self.ganesha_conf = "/etc/ganesha/ganesha.conf"
        self.ganesha_log = self.config["log"]["ganesha_log"]
        self.backend = self.config["nfs"]["backend"]
        self.export_path = self.config["nfs"]["export_path"]
        self.pseudo_path = self.config["nfs"]["pseudo_path"]

    def generate_config(self):
        """Generates ganesha.conf based on backend."""
        fsal_map = {
            "VFS": "VFS",
            "CephFS": "CEPH",
            "GlusterFS": "GLUSTER"
        }

        if self.backend not in fsal_map:
            raise ValueError(f"Unsupported backend: {self.backend}")

        config_content = GANESHA_CONF_TEMPLATE.format(
            export_path=self.export_path,
            pseudo_path=self.pseudo_path,
            fsal_name=fsal_map[self.backend]
        )

        with open(self.ganesha_conf, "w") as conf_file:
            conf_file.write(config_content)

    def start(self):
        """Starts the NFS-Ganesha service."""
        self.generate_config()
        cmd = [self.ganesha_bin, "-f", self.ganesha_conf, "-L", self.ganesha_log]
        _, _, err = self.run_command(cmd)
        time.sleep(5)
        if err:
            raise RuntimeError(f"Failed to start Ganesha: {err}")

    def stop(self):
        """Stops the NFS-Ganesha service."""
        self.run_command(["pkill", "-f", self.ganesha_bin])
