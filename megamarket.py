import time
from typing import Tuple
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
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
    COOKIES_CLOSE_BUTTON,
    RESOLUTION_FILTER,
    DISPLAY_FILTER,
    PROCESSOR_FILTER,
    ORDERING_DROPBOX,
    IN_STOCK_FILTER,
    ALL_ITEM_CARDS,
    CLEAR_FILTERS_BUTTON
)

class MegaMarket:
    """Class for MegaMarket automatization
    We will handle login in `init`.
    """
    def __init__(self, phone_number: str):
        self.url = 'https://megamarket.ru/'
        self.driver = webdriver.Firefox()
        self.driver.set_window_size(1920, 1080)
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
        
        self.driver.execute_script('window.scroll(0, 0);')
        
    def proceed_to_catalogue(self):
        """ 
        Method for opening the catalogue.
        Catalogue item is hardcoded.
        """
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
    
    def apply_filters(self):
        try:
            self._wdw_pres_elem(ORDERING_DROPBOX)
        except TimeoutError:
            print('You didn`t proceed to catalogue')
            return
        
        in_stock_toggle = self.driver.find_element(*IN_STOCK_FILTER)
        self.driver.execute_script('arguments[0].scrollIntoView(true); window.scrollBy(0, -80);', in_stock_toggle)
        self._create_action_chain_click(in_stock_toggle).perform()
        time.sleep(5)

        for element in self.driver.find_elements(By.CLASS_NAME, 'filters-desktop__filter-groups.list'):
            for subelement in element.find_elements(By.CLASS_NAME, 'filters-desktop__filter-item'):
                checkboxes = subelement.find_elements(
                        By.CLASS_NAME,
                        'form-group.form-group-checkbox.error-top-left.listing-filter-checkbox'
                    )
                
                try:
                    first_enabled_checkbox = [cb for cb in checkboxes if not cb.get_attribute('disabled')][0]
                except IndexError:
                    print('No available items. Skipping filter.')
                    continue
                self.driver.execute_script('arguments[0].scrollIntoView(true); window.scrollBy(0, -80);', subelement)
                
                element_to_click = first_enabled_checkbox.find_element(By.CLASS_NAME, 'checkbox-text')
                self._create_action_chain_click(element_to_click).perform()
                time.sleep(5)
    
    def add_to_cart(self):
        self.driver.execute_script(
            'arguments[0].scrollIntoView(true); window.scrollBy(0, -80)',
            self.driver.find_element(*CLEAR_FILTERS_BUTTON)
            )
        
        try:
            item_cards = self.driver.find_elements(*ALL_ITEM_CARDS)
        except NoSuchElementException:
            print('No items in stock')
                
        button = item_cards[0].find_element(By.CLASS_NAME, 'catalog-buy-button__button.btn.sm')

        self._create_action_chain_click(button).perform()
        self._create_action_chain_click(
            self.driver.find_element(By.CLASS_NAME, 'mini-cart__info.mini-cart__info_no-radius')
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
    import sys
    mm = MegaMarket(sys.argv[1])
    mm.proceed_to_catalogue()
    mm.apply_filters()
    mm.add_to_cart()