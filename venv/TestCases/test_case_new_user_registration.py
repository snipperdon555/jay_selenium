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
driver.get("https://jpetstore.aspectran.com/account/newAccountForm")
faker = Faker()


hrome_options = Options()
actions = ActionChains(driver)

def test_find_user_id_textbox():
    # enter user ID
    user_id =''.join(random.choices(string.ascii_letters + string.digits, k=16))
    wj.write_user_id_to_text(user_id)
    user_id_textbox = new_user_page.find_user_id_textbox(driver)
    user_id_textbox.send_keys(user_id)

def test_find_new_passwrod_textbox():
    # enter new password
    password = "Pass123"
    new_passwrod_textbox = new_user_page.find_new_passwrod_textbox(driver)
    new_passwrod_textbox.send_keys(password)

def test_find_confirm_passwrod_textbox():
    # enter confirm password
    password = "Pass123"
    confirm_passwrod_textbox = new_user_page.find_confirm_passwrod_textbox(driver)
    confirm_passwrod_textbox.send_keys(password)

def test_find_first_name_textbox():
    # enter first name
    first_name = faker.first_name()
    first_name_textbox = new_user_page.find_first_name_textbox(driver)
    first_name_textbox.send_keys(first_name)

def test_find_last_name_textbox():
    # enter last name
    last_name = faker.last_name()
    last_name_textbox = new_user_page.find_last_name_textbox(driver)
    last_name_textbox.send_keys(last_name)

def test_find_email_textbox():
    # enter email
    email = faker.email()
    email_textbox = new_user_page.find_email_textbox(driver)
    email_textbox.send_keys(email)

def test_find_phone_textbox():
    # enter phone
    phone_no = random.randint(100000000,999999999)
    phone_textbox = new_user_page.find_phone_textbox(driver)
    phone_textbox.send_keys(phone_no)

def test_find_address_1_textbox():
    # enter address 1
    address1 = faker.address()
    address_1_textbox = new_user_page.find_address_1_textbox(driver)
    address_1_textbox.send_keys('1')

def test_find_address_2_textbox():
    # enter address 2
    address2 = faker.address()
    address_2_textbox = new_user_page.find_address_2_textbox(driver)
    address_2_textbox.send_keys('1')

def test_find_city_textbox():
    # enter city text box
    city = faker.city()
    city_textbox = new_user_page.find_city_textbox(driver)
    city_textbox.send_keys(city)

def test_find_state_textbox():
    # enter state text box
    state = faker.state()
    state_textbox = new_user_page.find_state_textbox(driver)
    state_textbox.send_keys(state)

def test_find_zip():
    # enter state text box
    zip = "inl000"
    # zip = faker.zip()
    zip_textbox = new_user_page.find_zip(driver)
    zip_textbox.send_keys(zip)

def test_find_country():
    # enter country text box
    country = faker.country()
    country_textbox = new_user_page.find_country(driver)
    country_textbox.send_keys(country)

def test_find_dropbox_language():
    # enter language dropbox
    language_value = "English"
    dropbox_language = new_user_page.find_dropbox_language(driver)
    dropbox_language.select_by_visible_text(language_value)

def test_find_dropbox_favorite_category():
    # enter favorite category dropbox
    category_value = "Fish"
    dropbox_favorite_category = new_user_page.find_dropbox_favorite_category(driver)
    dropbox_favorite_category.select_by_visible_text(category_value)

def test_find_inputbox_mylist():
    # enter inputbox my list
    inputbox_mylist = new_user_page.find_inputbox_mylist(driver)
    inputbox_mylist.click()

def test_find_inputbox_mybanner():
    # enter inputbox my list
    inputbox_mybanner = new_user_page.find_inputbox_mybanner(driver)
    inputbox_mybanner.click()

def test_find_submit_button():
    # click on save account info
    button_save_account_info = new_user_page.find_submit_button(driver)
    actions.move_to_element(button_save_account_info).perform()
    button_save_account_info.click()

def test_successful_user_creation():
    # user creation test
    text = "Your account has been created. Please try login."
    assert text in driver.page_source

def test_successful_user_creation():
    #user name for login
    text = "Your account has been created. Please try login."
    assert text in driver.page_source
    driver.close()