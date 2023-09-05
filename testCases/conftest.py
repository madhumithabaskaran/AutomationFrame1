import pytest
from selenium import webdriver
@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("Launching Chrome browser....")
    elif browser=='edge':
        driver=webdriver.Edge()
        print("edge is lanuching.....")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

def pytest_configure(config):
    config._metadata = {
        "Tester": "Madhu",
        "Project Name": "AutomationFrame1",
    }

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)