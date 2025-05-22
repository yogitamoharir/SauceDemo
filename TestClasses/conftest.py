import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from UtilityFiles.readProperties import ReadConfig


@pytest.fixture
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.get(ReadConfig.getAppUrl())
    driver.implicitly_wait(5)
    return driver

# Step2: use to get browser name from command - line & pass value browser to
# openbrowser fixture.


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# step1: set default value of browser.
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="provide browser name - chrome, firefox, edge, etc")


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
   metadata['Project Name'] = 'Swag Labs'
   metadata['Module Name'] = 'LoginSL'
   metadata['Tester Name'] = 'Yogita'