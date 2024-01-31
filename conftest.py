from datetime import datetime
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Base configuration
BaseUrl = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
Username = "Admin"
Password = "admin123"


# Driver setup
@pytest.fixture(scope="class", autouse=True)
def browser_setup(request):
    service = Service(
        executable_path=r'D:\TUTORIAL\python_wkspace\udemy_selenium_with_python\capstoneCopy\drivers\chromedriver.exe')
    options = webdriver.ChromeOptions()
    # chrome_options = Options()
    # request.cls.driver = webdriver.Chrome("D:/GUVI/chromedriver_win32/chromedriver.exe", options=chrome_options)
    request.cls.driver = webdriver.Chrome(service=service, options=options)
    request.cls.driver.maximize_window()


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    today = datetime.now()
    report_dir = Path("reports", today.strftime("%Y%m%d"))
    report_dir.mkdir(parents=True, exist_ok=True)
    pytest_html = report_dir / f"Report_{today.strftime('%Y%m%d%H%M')}.html"
    config.option.htmlpath = pytest_html
    config.option.self_contained_html = True

def pytest_html_report_title(report):
    report.title = "HRM Test Report"
