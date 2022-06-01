from pages.calculator_page import CalculatorPage
from selenium import webdriver
import pytest


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    return browser
    browser.quit()


def test_check_result_on_calculator_page(browser):
    link = "https://google.com"
    page = CalculatorPage(browser, link)

    page.open()
    page.go_to_calculator_page()
    page.input_numbers_on_calculator()
    assert page.return_memory_string() == '1 × 2 - 3 + 1 ='
    assert page.return_result() == '0'
