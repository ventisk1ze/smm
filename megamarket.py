from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

# TODO: перевести всё с class на xpath и вынести в константы

class MegaMarket:
    """Class for MegaMarket automatization
    We will handle login in `init`.
    """
    def __init__(self, phone_number: str):
        self.url = 'https://megamarket.ru/'
        self.driver = webdriver.Firefox()
        self.driver.get(self.url)

        # Find and click login button, wait for login window
        login_button = self.driver.find_element(By.CLASS_NAME, 'anon-links__wrapper')
        self._create_action_chain_click(login_button).perform()
        self._wdw_vis_elem_class('pui-button-element__content')

        #Find and click 'Войти по номеру телефона' button, wait for form
        phone_login_button = self.driver.find_element(By.CLASS_NAME, 'pui-button-element__content')
        self._create_action_chain_click(phone_login_button).perform()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[2]/div[1]/div[1]/div/div/div/div/div[1]/div/div/form/div[1]/label/input')
        ))
        
        #Find textbox and 'Получить код' button
        phone_textbox = self.driver.find_element(
            By.XPATH, '/html/body/div[2]/div[1]/div[1]/div/div/div/div/div[1]/div/div/form/div[1]/label/input'
        )
        get_code_button = self.driver.find_element(By.CLASS_NAME, 'pui-button-element__content')

        # Click textbox, input phone number and click 'Получить код' button
        self._create_action_chain_click(phone_textbox).perform()
        phone_textbox.send_keys(self._validate_phone_number(phone_number))
        self._create_action_chain_click(get_code_button).perform()

        code = input('Введите полученный код: ')

        self._wdw_vis_elem_class('sms-verification__field')
        code_textbox = self.driver.find_element(By.CLASS_NAME, 'sms-verification__field')
        self._create_action_chain_click(code_textbox)
        code_textbox.send_keys(code)


    def _create_action_chain_click(self, element):
        return ActionChains(self.driver).move_to_element(element).click(element)
    
    def _wdw_vis_elem_class(self, element_class):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, element_class)))
    
    @staticmethod
    def _validate_phone_number(phone_number: str):
        return phone_number[phone_number.index('9'):]

if __name__ == '__main__':
    MegaMarket('79990870968')