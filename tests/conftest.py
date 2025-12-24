import pytest
from framework.driver.driver_manager import DriverManager
from framework.utils.config_loader import load_config
from framework.utils.screenshot import take_screenshot

@pytest.fixture(scope="session")
def config():
    return load_config()

@pytest.fixture(scope="session")
def driver(config):
    driver = DriverManager.get_driver(config["project"]["browser"])
    yield driver
    DriverManager.quit_driver()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.session._driver
        take_screenshot(driver, "output/screenshots")
