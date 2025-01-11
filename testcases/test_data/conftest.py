import pytest
from selenium import webdriver
@pytest.fixture()
def setup():
    driver = webdriver.Edge("C:\\Drive\\msedgedriver.exe")
    return driver