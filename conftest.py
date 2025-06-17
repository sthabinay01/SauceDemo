from datetime import datetime
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--headless")  # Remove if you want to see the browser
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

#generating report
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    today = datetime.now()
    report_dir =Path("Saucereports",today.strftime("%Y%m%d"))
    report_dir.mkdir(parents = True,exist_ok=True)
    report_file = report_dir / f"Report_{today.strftime('%Y%m%d%H%M')}.html"
    config.option.htmlpath = str(report_file)
    config.option.self_contained_html = True


#creating title for report
def pytest_html_report_title(report):
    report.title = "SauceDemo Report"