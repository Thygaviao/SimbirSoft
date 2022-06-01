from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CalculatorPage(BasePage):
    def go_to_calculator_page(self):
        search_field = self.browser.find_element(By.NAME, 'q')
        search_field.send_keys('Калькулятор')
        find_button = self.browser.find_element(By.NAME, 'btnK')
        find_button.click()

    def input_numbers_on_calculator(self):
        button_1 = self.browser.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/div'
                                                       '/div[3]/div/table[2]/tbody/tr[4]/td[1]/div/div')
        button_2 = self.browser.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/div'
                                                       '/div[3]/div/table[2]/tbody/tr[4]/td[2]/div/div')
        button_3 = self.browser.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/div'
                                                       '/div[3]/div/table[2]/tbody/tr[4]/td[3]/div/div')
        button_multiplication = self.browser.find_element(By.XPATH,
                                                          '//*[@id="rso"]/div[1]/div/div/div[1]/div/div'
                                                          '/div[3]/div/table[2]/tbody/tr[3]/td[4]/div/div')
        button_subtraction = self.browser.find_element(By.XPATH,
                                                       '//*[@id="rso"]/div[1]/div/div/div[1]/div/div'
                                                       '/div[3]/div/table[2]/tbody/tr[4]/td[4]/div/div')
        button_addition = self.browser.find_element(By.XPATH,
                                                    '//*[@id="rso"]/div[1]/div/div/div[1]/div/div'
                                                    '/div[3]/div/table[2]/tbody/tr[5]/td[4]/div/div')
        button_equals = self.browser.find_element(By.XPATH,
                                                  '//*[@id="rso"]/div[1]/div/div/div[1]/div/div'
                                                  '/div[3]/div/table[2]/tbody/tr[5]/td[3]/div/div')

        button_1.click()
        button_multiplication.click()
        button_2.click()
        button_subtraction.click()
        button_3.click()
        button_addition.click()
        button_1.click()
        button_equals.click()

    def return_memory_string(self):
        return self.browser.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/div'
                                                   '/div[1]/div[2]/div[1]/div/span').text

    def return_result(self):
        return self.browser.find_element(By.XPATH, '//*[@id="cwos"]').text
