import yaml
import os


class ConfigLoader:
    """Loads YAML configuration file."""

    CONFIG_PATH = os.path.join(os.path.dirname(__file__), "../config/settings.yaml")

    @staticmethod
    def load_config ():
        """Reads and returns config as a dictionary."""
        with open(ConfigLoader.CONFIG_PATH, "r") as file:
            return yaml.safe_load(file)
