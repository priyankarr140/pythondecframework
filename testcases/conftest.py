import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")

@pytest.fixture(scope="class")
def setup(request):
    #browser=request.config.getoption("browser_name")
    browser='chrome'
    if browser=='chrome':
        service = Service(executable_path="D:\\driver\\December\\chromedriver.exe")
        driver = webdriver.Chrome(service=service)
    else:
        service = Service(executable_path="D:\\driver\\December\\geckodriver.exe")
        driver = webdriver.Firefox(service=service)

    driver.get("https://in.bookmyshow.com/explore/home/delhi")

    request.cls.driver=driver
    yield
    driver.close()