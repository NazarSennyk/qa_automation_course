import json
import pytest
from qa_automation_hw.data_classes.peson import Person
from qa_automation_hw.page_objects.login_page import LoginPage
from qa_automation_hw.utilities.configuration import Configuration
from qa_automation_hw.utilities.driver_factory import DriverFactory
from qa_automation_hw.utilities.read_configs import Read_config


@pytest.fixture()
def create_driver():
    driver_chrome = DriverFactory.create_driver(Read_config.get_browser_id())
    driver_chrome.maximize_window()
    driver_chrome.get(Read_config.get_base_urt())
    yield driver_chrome
    driver_chrome.quit()


@pytest.fixture()
def open_login_page(create_driver):
    return LoginPage(create_driver)


@pytest.fixture()
def log_in_user(open_login_page, env):
    open_login_page.open_login_window()
    return open_login_page.login(env.cell_phone, env.password)


@pytest.fixture(scope='session')
def env():
    with open('../configuration/configuration.json') as f:
        data = f.read()
        json_to_dict = json.loads(data)
    config = Configuration(**json_to_dict)
    return config


@pytest.fixture()
def crate_person():
    return Person()





