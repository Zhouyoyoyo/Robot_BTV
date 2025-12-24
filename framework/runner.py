import pytest
from framework.utils.config_loader import load_config
from framework.utils.mailer import send_mail

def run_tests():
    config = load_config()
    result = pytest.main(["-s", "tests"])
    send_mail(config["project"]["report_email"], "Test Finished", f"Result={result}")
