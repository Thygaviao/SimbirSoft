import pages.calculator_page
import pytest


@pytest.mark.result
def test_check_result_string_on_calculator_page(browser):
    page = pages.calculator_page.CalculatorPage(browser)

    page.open()
    page.go_to_calculator_page()
    page.input_numbers_on_calculator()
    assert page.return_result() == '0'


@pytest.mark.memory
def test_check_memory_string_on_calculator_page(browser):
    page = pages.calculator_page.CalculatorPage(browser)

    page.open()
    page.go_to_calculator_page()
    page.input_numbers_on_calculator()
    assert page.return_memory_string() == '1 × 2 - 3 + 1 ='
