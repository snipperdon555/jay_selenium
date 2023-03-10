from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import page_new_user as new_user_page
from faker import Faker
import random,string
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from Utilities import write_to_json as wj

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver =  webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://jpetstore.aspectran.com/account/signonForm")
hrome_options = Options()
actions = ActionChains(driver)

def get_user_id():
    username_value = wj.read_userid_from_textfile()
    return username_value

def test_user_login():
    # try user login
    username_textbox = new_user_page.find_user_id_textbox(driver)
    password_textbox = new_user_page.find_new_passwrod_textbox(driver)
    login_button = new_user_page.find_login_button(driver)
    user_id = get_user_id()
    print('userid is ',user_id)
    username_textbox.clear()
    password_textbox.clear()
    username_textbox.send_keys(user_id)
    password_textbox.send_keys("Pass123")
    login_button.click()

def test_successful_login_homepage():
    #user name for login
    text = "Sign Out"
    assert text in driver.page_source
    driver.close()