from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import pytest

# username = herlan.wiajaya30@gmail.com
# pass     = Testing123

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.bukalapak.com/login")
    yield driver
    driver.quit()

def test_pass_salah(driver):
    driver.find_element_by_id("user_session_username").send_keys("herlan.wijaya30@gmail.com")
    driver.find_element_by_id("user_session_password").send_keys("123Testing")
    driver.find_element_by_class_name("c-btn--spinner__icon").click()
    driver.implicitly_wait(10)
    assert (driver.find_element_by_class_name("c-fld__error"))

def test_user_salah(driver):
    driver.find_element_by_id("user_session_username").send_keys("herlan.wijaya@gmail.com")
    driver.find_element_by_id("user_session_password").send_keys("Testing123")
    driver.find_element_by_class_name("c-btn--spinner__icon").click()
    driver.implicitly_wait(10)
    assert (driver.find_element_by_class_name("c-fld__error"))

def test_userpass_salah(driver):
    driver.find_element_by_id("user_session_username").send_keys("herlan.wijaya@gmail.com")
    driver.find_element_by_id("user_session_password").send_keys("123Testing")
    driver.find_element_by_class_name("c-btn--spinner__icon").click()
    driver.implicitly_wait(10)
    assert (driver.find_element_by_class_name("c-fld__error"))

def test_benar_semua (driver):
    driver.find_element_by_id("user_session_username").send_keys("herlan.wijaya30@gmail.com")
    driver.find_element_by_id("user_session_password").send_keys("Testing123")
    driver.find_element_by_class_name("c-btn--spinner__icon").click()
    driver.implicitly_wait(10)
    assert (driver.find_element_by_class_name("bl-avatar"))
