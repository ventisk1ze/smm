from selenium.webdriver.common.by import By


# ------------------------------- LOGIN ELEMENTS -------------------------------
INITIAL_LOGIN_LINK = (By.XPATH, '/html/body/div[2]/div[1]/div[3]/div[2]/header/div/div[1]/div/div/div/div[4]/div/div/a')
PHONE_LOGIN_BUTTON = (By.XPATH, '/html/body/div[2]/div[1]/div[1]/div/div/div/div/div[1]/div/div/div[2]/div[2]/button')
PHONE_TEXTBOX = (By.XPATH, '/html/body/div[2]/div[1]/div[1]/div/div/div/div/div[1]/div/div/form/div[1]/label/input')
GET_CODE_BUTTON = (By.XPATH, '/html/body/div[2]/div[1]/div[1]/div/div/div/div/div[1]/div/div/form/div[2]/button/span[1]')
CODE_TEXTBOX = (By.XPATH, '/html/body/div[2]/div[1]/div[1]/div/div/div/div/div[1]/div/div/div[2]/div[1]/input')

# ------------------------------- POPUPS BUTTONS -------------------------------
SPASIBO_CLOSE_BUTTON = (By.XPATH, '/html/body/div[2]/div[1]/div[3]/div[2]/header/div/div[1]/div/div/div/div[4]/div/div/div/div/div/div/div/div[3]/div/button')
COOKIES_CLOSE_BUTTON = (By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[2]/article/button[1]')

# ------------------------------- CATALOGUE ELEMENTS -------------------------------
CATALOGUE_BUTTON = (By.XPATH, '/html/body/div[2]/div[1]/div[3]/div[2]/header/div/div[1]/div/div/div/div[2]/div/div/div[1]/span')
ELECTRONICS_BUTTON = (By.XPATH, '/html/body/div[2]/div[1]/div[3]/div[2]/header/div/div[1]/div/div/div/div[2]/div/div/div[2]/nav/div/div[1]/div/div[5]/a/div[2]')
LAPTOPS_ACCS_BUTTON = (By.XPATH, '/html/body/div[2]/div[1]/div[3]/div[2]/header/div/div[1]/div/div/div/div[2]/div/div/div[2]/nav/div/div[2]/div[2]/div[1]/div/div[5]/a/div')
LAPTOPS_BUTTON = (By.XPATH, '/html/body/div[2]/div[1]/div[3]/div[2]/header/div/div[1]/div/div/div/div[2]/div/div/div[2]/nav/div/div[2]/div[2]/div[2]/div/div[1]/a')
MACBOOK_BUTTON = (By.XPATH, '/html/body/div[2]/div[1]/div[3]/div[2]/header/div/div[1]/div/div/div/div[2]/div/div/div[2]/nav/div/div[2]/div[2]/div[3]/div/div[2]/a/div')