from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CalculatorPage(BasePage):
    def go_to_calculator_page(self):
        url = "https://google.com"
        search_field = self.browser.find_element(By.XPATH, "//input[@title='Поиск']")
        search_field.send_keys('Калькулятор')
        find_button = self.browser.find_element(By.XPATH, "//div[@class='CqAVzb lJ9FBc']//input[@name='btnK']")
        find_button.click()

    def input_numbers_on_calculator(self):
        button_1 = self.browser.find_element(By.XPATH, "//div[@role='button'][normalize-space()='1']")
        button_2 = self.browser.find_element(By.XPATH, "//div[@role='button'][normalize-space()='2']")
        button_3 = self.browser.find_element(By.XPATH,"//div[@role='button'][normalize-space()='3']")
        button_multiplication = self.browser.find_element(By.XPATH, "//div[@aria-label='умножение']")
        button_subtraction = self.browser.find_element(By.XPATH, "//div[@aria-label='вычитание']")
        button_addition = self.browser.find_element(By.XPATH,"//div[@aria-label='сложение']")
        button_equals = self.browser.find_element(By.XPATH,"//div[@aria-label='равно']")

        button_1.click()
        button_multiplication.click()
        button_2.click()
        button_subtraction.click()
        button_3.click()
        button_addition.click()
        button_1.click()
        button_equals.click()

    def return_memory_string(self):
        return self.browser.find_element(By.XPATH, "//span[@class='vUGUtc']").text

    def return_result(self):
        return self.browser.find_element(By.XPATH, "//span[@id='cwos']").text
