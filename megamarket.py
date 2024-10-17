from typing import Tuple
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from constants import (
    INITIAL_LOGIN_LINK,
    PHONE_LOGIN_BUTTON,
    PHONE_TEXTBOX,
    GET_CODE_BUTTON,
    CODE_TEXTBOX,
    CATALOGUE_BUTTON,
    ELECTRONICS_BUTTON,
    LAPTOPS_ACCS_BUTTON,
    LAPTOPS_BUTTON,
    MACBOOK_BUTTON,
    SPASIBO_CLOSE_BUTTON,
    COOKIES_CLOSE_BUTTON
)

class MegaMarket:
    """Class for MegaMarket automatization
    We will handle login in `init`.
    """
    def __init__(self, phone_number: str):
        self.url = 'https://megamarket.ru/'
        self.driver = webdriver.Firefox()
        self.driver.get(self.url)
        
        # Find and click login button, wait for login window
        login_button = self.driver.find_element(*INITIAL_LOGIN_LINK)
        self._create_action_chain_click(login_button).perform()
        self._wdw_pres_elem(PHONE_LOGIN_BUTTON)

        #Find and click 'Войти по номеру телефона' button, wait for form
        phone_login_button = self.driver.find_element(*PHONE_LOGIN_BUTTON)
        self._create_action_chain_click(phone_login_button).perform()
        self._wdw_pres_elem(PHONE_TEXTBOX)
        
        #Find textbox and 'Получить код' button
        phone_textbox = self.driver.find_element(*PHONE_TEXTBOX)
        get_code_button = self.driver.find_element(*GET_CODE_BUTTON)

        # Click textbox, input phone number and click 'Получить код' button
        self._create_action_chain_click(phone_textbox).perform()
        phone_textbox.send_keys(self._validate_phone_number(phone_number))
        self._create_action_chain_click(get_code_button).perform()

        code = input('Введите полученный код: ')

        # Wait for code verifictaion textbox and send code to the textbox        
        self._wdw_pres_elem(CODE_TEXTBOX)
        code_textbox = self.driver.find_element(*CODE_TEXTBOX)
        self._create_action_chain_click(code_textbox).perform()
        code_textbox.send_keys(code)

        for element in [SPASIBO_CLOSE_BUTTON, COOKIES_CLOSE_BUTTON]:
            try:
                self._wdw_pres_elem(element)
                self._create_action_chain_click(
                    self.driver.find_element(*element)
                ).perform()
            except TimeoutException:
                print('Nothing to close')
        
    def proceed_to_catalogue(self):
        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element(CODE_TEXTBOX))
        
        catalogue_elements = [
            ELECTRONICS_BUTTON,
            LAPTOPS_ACCS_BUTTON,
            LAPTOPS_BUTTON,
            MACBOOK_BUTTON
        ]
        
        self._create_action_chain_click(
            self.driver.find_element(*CATALOGUE_BUTTON)
        ).perform()
        self._wdw_pres_elem(catalogue_elements[0])
        
        for i, element in enumerate(catalogue_elements):
            self._create_action_chain_move(
                self.driver.find_element(*element)
            ).perform()
            
            try:
                self._wdw_pres_elem(catalogue_elements[i+1])
            except IndexError:
                self._create_action_chain_click(
                    self.driver.find_element(*element)
                ).perform()

    def _create_action_chain_click(self, element):
        return ActionChains(self.driver).move_to_element(element).click(element)
    
    def _create_action_chain_move(self, element):
        return ActionChains(self.driver).move_to_element(element)
    
    def _wdw_pres_elem(self, by_element: Tuple):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(by_element))
    
    @staticmethod
    def _validate_phone_number(phone_number: str):
        return phone_number[phone_number.index('9'):]

if __name__ == '__main__':
    MegaMarket('79990870968').proceed_to_catalogue()