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
ORDERING_DROPBOX = (By.XPATH, '/html/body/div[2]/div[1]/div[3]/main/div/div[1]/div[3]/div/div[2]/div/div[2]/div[2]/div[1]/div/div[1]/div/div/input')
CATALOGUE_BUTTON = (By.XPATH, '/html/body/div[2]/div[1]/div[3]/div[2]/header/div/div[1]/div/div/div/div[2]/div/div/div[1]/span')
ELECTRONICS_BUTTON = (By.XPATH, '/html/body/div[2]/div[1]/div[3]/div[2]/header/div/div[1]/div/div/div/div[2]/div/div/div[2]/nav/div/div[1]/div/div[5]/a/div[2]')
LAPTOPS_ACCS_BUTTON = (By.XPATH, '/html/body/div[2]/div[1]/div[3]/div[2]/header/div/div[1]/div/div/div/div[2]/div/div/div[2]/nav/div/div[2]/div[2]/div[1]/div/div[5]/a/div')
LAPTOPS_BUTTON = (By.XPATH, '/html/body/div[2]/div[1]/div[3]/div[2]/header/div/div[1]/div/div/div/div[2]/div/div/div[2]/nav/div/div[2]/div[2]/div[2]/div/div[1]/a')
MACBOOK_BUTTON = (By.XPATH, '/html/body/div[2]/div[1]/div[3]/div[2]/header/div/div[1]/div/div/div/div[2]/div/div/div[2]/nav/div/div[2]/div[2]/div[3]/div/div[2]/a/div')

# ------------------------------- FILTER ELEMENTS -------------------------------
CLEAR_FILTERS_BUTTON = (By.XPATH, '/html/body/div[2]/div[1]/div[3]/main/div/div[1]/div[3]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div')
RESOLUTION_FILTER = (By.XPATH, '/html/body/div[2]/div[1]/div[3]/main/div/div[1]/div[3]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/nav/div[5]/div[1]')
DISPLAY_FILTER = (By.XPATH,'/html/body/div[2]/div[1]/div[3]/main/div/div[1]/div[3]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/nav/div[5]/div[2]')
PROCESSOR_FILTER = (By.XPATH, '/html/body/div[2]/div[1]/div[3]/main/div/div[1]/div[3]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/nav/div[5]/div[3]')
IN_STOCK_FILTER = (By.XPATH, '/html/body/div[2]/div[1]/div[3]/main/div/div[1]/div[3]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/nav/div[2]/div[3]/div/div/div[1]/div/span')

# ------------------------------- CART ELEMENTS -------------------------------
TO_CART_BUTTON = (By.XPATH, '/html/body/div[2]/div[1]/div[3]/main/div/div[1]/div[3]/div/div[2]/div/div[2]/div[2]/div[3]/div/div/div/div[1]/div[6]/div/button')
CART_BUTTON = (By.XPATH, '/html/body/div[2]/div[1]/div[3]/div[2]/header/div/div[1]/div/div/div/div[7]/div/div/a/span')
ALL_ITEM_CARDS = (By.CLASS_NAME, 'catalog-item-regular-desktop.ddl_product.catalog-item-desktop')