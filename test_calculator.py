from pages.calculator_page import CalculatorPage
import pytest


class TestCalc:

    @pytest.mark.result
    def test_check_result_string_on_calculator_page(self, browser):
        self.page = CalculatorPage(browser)

        self.page.open()
        self.page.go_to_calculator_page()
        self.page.input_numbers_on_calculator()
        self.page.return_result_string()
        self.page.return_memory_string()

    @pytest.mark.memory
    def test_check_memory_string_on_calculator_page(self, browser):
        self.page = CalculatorPage(browser)

        self.page.open()
        self.page.go_to_calculator_page()
        self.page.input_numbers_on_calculator()
        self.page.return_memory_string()
