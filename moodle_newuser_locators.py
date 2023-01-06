import datetime
import moodle_locators as locators
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
s = Service(executable_path='chromedriver')

driver = webdriver.Chrome(service=s)

# Fixture methods

def setup():
    #maximizing the screen
    driver.maximize_window()
    #wait for the browser to load up
    driver.implicitly_wait(30)
    #navigate to the moodle app website
    driver.get(locators.moodle_url)
    #checking that the url is addy is correct and that we are seeing the correct title
    if driver.current_url == locators.moodle_url and driver.title == 'SQA Server 1':
        print(f'We are at the correct homepage---{driver.current_url}')
        print(f'We are seeing the title---"SQA Server 1"')
    else:
        print("We are not at the correct homepage. Please check your code")
        driver.close()
        driver.quit()

def tearDown():
        if driver is not None:
            print(f'--------------')
            print(f'The test was completed at : {datetime.datetime.now()}')
            driver.close()
            driver.quit()

def log_in(username, password):
    if driver.current_url == locators.moodle_url:
        driver.find_element(By.LINK_TEXT,'Log in').click()
        if driver.current_url == locators.moodle_login_url:
            driver.find_element(By.ID, 'username').clear()
            driver.find_element(By.ID,'username').send_keys(username)
            sleep(.25)
            driver.find_element(By.ID,'password').send_keys(password)
            sleep(.25)
            driver.find_element(By.ID,'loginbtn').click()
            if driver.title == 'Dashboard' and driver.current_url == locators.moodle_dashboard_url:
                assert driver.current_url == locators.moodle_dashboard_url
                print('Login is successful and the Dashboard is present')
            else:
                print('Dashboard is not present, try again. D\oh')

def log_out():
    driver.find_element(By.CLASS_NAME, 'usermenu').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT,'Log out').click()
    sleep(0.25)
    if driver.current_url==locators.moodle_url:
       print(f'Log out successfully at:{datetime.datetime.now()}')

def create_new_user():
    driver.find_element(By.LINK_TEXT, "Site administration").click()
    sleep(0.25)
    assert driver.find_element(By.LINK_TEXT, 'Users')
    driver.find_element(By.LINK_TEXT, 'Users').click()
    sleep(0.25)
    assert driver.find_element(By.LINK_TEXT, 'Add a new user').is_displayed()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Add a new user').click()
    sleep(0.25)
    # send fake data to create a new user
    driver.find_element(By.ID, 'id_username').send_keys(locators.new_username)
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Click to enter text').click()
    sleep(0.25)
    driver.find_element(By.ID, 'id_newpassword').send_keys(locators.new_password)
    sleep(0.25)
    driver.find_element(By.ID, 'id_preference_auth_forcepasswordchange').click()
    sleep(0.25)
    driver.find_element(By.ID, 'id_firstname').send_keys(locators.first_name)
    sleep(0.25)
    driver.find_element(By.ID, 'id_lastname').send_keys(locators.last_name)
    sleep(0.25)
    driver.find_element(By.ID, 'id_email').send_keys(locators.email)
    sleep(0.25)
    Select(driver.find_element(By.ID, 'id_maildisplay')).select_by_visible_text('Allow everyone to see my email address')
    sleep(0.25)
    driver.find_element(By.ID, 'id_moodlenetprofile').send_keys(locators.moodle_net_profile)
    sleep(0.25)
    driver.find_element(By.ID, 'id_city').send_keys(locators.city)
    sleep(0.25)
    Select(driver.find_element(By.ID, 'id_country')).select_by_visible_text('Canada')
    sleep(0.25)
    Select(driver.find_element(By.ID, 'id_timezone')).select_by_visible_text('America/Vancouver')
    sleep(0.25)
    driver.find_element(By.ID, 'id_description_editoreditable').send_keys(locators.description)
    sleep(0.25)
    driver.find_element(By.ID,'id_imagealt').send_keys(locators.pic_desc)
    sleep(0.25)
    driver.find_element(By.XPATH, '//a[contains(.,"Additional name")]').click()
    sleep(0.25)
    driver.find_element(By.ID, 'id_firstnamephonetic').send_keys(locators.phonetic_firstname)
    sleep(0.25)
    driver.find_element(By.ID, 'id_lastnamephonetic').send_keys(locators.phonetic_lastname)
    sleep(0.25)
    driver.find_element(By.ID, 'id_middlename').send_keys(locators.phonetic_middle)
    sleep(0.25)
    driver.find_element(By.ID, 'id_alternatename').send_keys(locators.phonetic_alternate)
    sleep(0.25)
    driver.find_element(By.XPATH, '//a[contains(.,"Interest")]').click()
    sleep(0.25)
    for tags in locators.list_of_interests:
        driver.find_element(By.XPATH, '//div[3]/input').click()
        sleep(0.25)
        driver.find_element(By.XPATH, '//div[3]/input').send_keys(tags)
        sleep(0.25)
        driver.find_element(By.XPATH, '//div[3]/input').send_keys(Keys.ENTER)
    sleep(0.25)
    driver.find_element(By.XPATH, '//a[contains(.,"Optional")]').click()
    sleep(0.25)
    driver.find_element(By.CSS_SELECTOR, "input#id_idnumber").send_keys(locators.id)
    sleep(0.25)
    driver.find_element(By.CSS_SELECTOR, "input#id_institution").send_keys(locators.institution)
    sleep(0.25)
    driver.find_element(By.CSS_SELECTOR, "input#id_department").send_keys(locators.department)
    sleep(0.25)
    driver.find_element(By.CSS_SELECTOR, "input#id_phone1").send_keys(locators.phone1)
    sleep(0.25)
    driver.find_element(By.CSS_SELECTOR, "input#id_phone2").send_keys(locators.phone2)
    sleep(0.25)
    driver.find_element(By.CSS_SELECTOR, "input#id_address").send_keys(locators.address)
    sleep(0.25)
    driver.find_element(By.ID, 'id_submitbutton').click()
    sleep(0.25)

def check_user_created():
    #check the users main page
    if driver.current_url == locators.moodle_users_main_page:
        assert driver.find_element(By.XPATH, "//h1[text()='SQA Server 1']").is_displayed()
        driver.find_element(By.XPATH, '//a[contains(.,"Show more...")]').click()
        print('users main page')
        if driver.find_element(By.ID, 'fgroup_id_email_grp') and \
            driver.find_element(By.NAME, 'email'):
            sleep(0.25)
            driver.find_element(By.CSS_SELECTOR, 'input#id_email').send_keys(locators.email)
            sleep(0.25)
            driver.find_element(By.CSS_SELECTOR, 'input#id_addfilter').click()
            sleep(0.25)
            if driver.find_element(By.XPATH, f'//td[contains(.,"{locators.email}")]'):
                print('for the test scenario: check user created----successful, is passed')

def check_new_credentials():
    get_url = driver.current_url
    print("the url for the check credentials page is: " + get_url)
    if driver.find_element(By.XPATH, f"//*[contains(.,'{locators.full_name}')]").is_displayed():
        print('the Full name is: ' + locators.full_name)
    else:
        print('the name is not present')



        #Select(driver.find_element(By.ID,'id_maildisplay')).select_by_visible_text('Allow everyone to see my email address')
    #sleep(.25)
    #breakpoint()

# Calling the methods
#open the chrome browser
setup()
#login
log_in(locators.moodle_username, locators.moodle_password)
#create user
create_new_user()
check_user_created()
log_in(locators.new_username, locators.new_password)
check_new_credentials()
#logout
log_out()
log_in(locators.moodle_username, locators.moodle_password)
log_out()
tearDown()
