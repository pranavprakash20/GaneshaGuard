import pytest


class BaseTest:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        # Setup code (e.g., initialize connections, create test data)
        print("Setting up the test environment...")
        yield
        # Teardown code (e.g., clean up resources)
        print("Tearing down the test environment...")
