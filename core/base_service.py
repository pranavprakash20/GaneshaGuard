from abc import ABC, abstractmethod
import subprocess

class BaseService(ABC):
    """Abstract base class for managing services."""

    @abstractmethod
    def start(self):
        """Start the service."""
        pass

    @abstractmethod
    def stop(self):
        """Stop the service."""
        pass

    def run_command(self, command):
        """Runs a shell command and returns output."""
        result = subprocess.run(command, capture_output=True, text=True)
        return result.returncode, result.stdout, result.stderr
