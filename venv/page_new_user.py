from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

# driver =  webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# code to open the browser
# driver.get("https://jpetstore.aspectran.com/account/newAccountForm")

# text_box_userID = chrome_url_app.find_element_by_name("username")

def find_user_id_textbox(driver):
    user_id_textbox = driver.find_element(By.NAME, 'username')
    return user_id_textbox

def find_new_passwrod_textbox(driver):
    new_passwrod_textbox = driver.find_element(By.NAME, 'password')
    return new_passwrod_textbox

def find_confirm_passwrod_textbox(driver):
    confirm_passwrod_textbox = driver.find_element(By.NAME, 'repeatedPassword')
    return confirm_passwrod_textbox

def find_first_name_textbox(driver):
    first_name_textbox = driver.find_element(By.NAME, 'firstName')
    return first_name_textbox

def find_last_name_textbox(driver):
    last_name_textbox = driver.find_element(By.NAME, 'lastName')
    return last_name_textbox

def find_email_textbox(driver):
    email_textbox = driver.find_element(By.NAME, 'email')
    return email_textbox

def find_phone_textbox(driver):
    phone_textbox = driver.find_element(By.NAME, 'phone')
    return phone_textbox

def find_address_1_textbox(driver):
    address_1_textbox = driver.find_element(By.NAME, 'address1')
    return address_1_textbox

def find_address_2_textbox(driver):
    address_2_textbox = driver.find_element(By.NAME, 'address2')
    return address_2_textbox

def find_city_textbox(driver):
    city_textbox = driver.find_element(By.NAME, 'city')
    return city_textbox

def find_state_textbox(driver):
    state_textbox = driver.find_element(By.NAME, 'state')
    return state_textbox

def find_zip(driver):
    state_zip_textbox = driver.find_element(By.NAME, 'zip')
    return state_zip_textbox

def find_country(driver):
    country_textbox = driver.find_element(By.NAME, 'country')
    return country_textbox

def find_dropbox_language(driver):
    dropbox_language  = Select(driver.find_element(By.NAME, 'languagePreference'))
    return dropbox_language

def find_dropbox_favorite_category(driver):
    dropbox_favorite_category = Select(driver.find_element(By.NAME, 'favouriteCategoryId'))
    return dropbox_favorite_category

def find_inputbox_mylist(driver):
    inputbox_mylist = driver.find_element(By.NAME, 'listOption')
    return inputbox_mylist

def find_inputbox_mybanner(driver):
    inputbox_mybanner = driver.find_element(By.NAME, 'bannerOption')
    return inputbox_mybanner

def find_submit_button(driver):
    button_save_account_info = driver.find_element(By.XPATH, '//*[@id="CenterForm"]/form/div/button')
    return button_save_account_info

def find_login_button(driver):
    button_login =driver.find_element(By.XPATH, '//*[@id="Signon"]/form/div/div/button')
    return button_login

