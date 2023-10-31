from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest

url = "http://127.0.0.1:8000/"

def test_valid_user_login(driver):
    driver.get(url)  # Replace with your website"s URL
    time.sleep(1)
    login_btn = driver.find_element(By.CSS_SELECTOR, "a#login_btn.main-button-slider")
    login_btn.click()
    time.sleep(2)
    print("Testing Valid Data for Login")
    fill_login_form(driver, "valid_username", "Valid!123")
    validate_successful_login(driver)

def test_invalid_username_login(driver):
    driver.get(url)  # Replace with your website"s URL
    time.sleep(2)
    login_btn = driver.find_element(By.CSS_SELECTOR, "a#login_btn.main-button-slider")
    login_btn.click()
    time.sleep(2)
    print("Testing Invalid Data for Login username")
    fill_login_form(driver, "invalid_username", "Valid!123")
    validate_successful_login(driver)

def test_invalid_password_login(driver):
    driver.get(url)  # Replace with your website"s URL
    time.sleep(2)
    login_btn = driver.find_element(By.CSS_SELECTOR, "a#login_btn.main-button-slider")
    login_btn.click()
    time.sleep(2)
    print("Testing Invalid Data for invalid password")
    fill_login_form(driver, "Valid_username", "inValid!123")
    validate_successful_login(driver) 

def test_missing_username(driver):
    driver.get(url)  # Replace with your website"s URL
    time.sleep(2)
    login_btn = driver.find_element(By.CSS_SELECTOR, "a#login_btn.main-button-slider")
    login_btn.click()
    time.sleep(2)
    print("Testing missing username")
    fill_login_form(driver, "", "inValid!123")
    validate_successful_login(driver) 

def test_missing_password(driver):
    driver.get(url)  # Replace with your website"s URL
    time.sleep(2)
    login_btn = driver.find_element(By.CSS_SELECTOR, "a#login_btn.main-button-slider")
    login_btn.click()
    time.sleep(2)
    print("Testing missing password")
    fill_login_form(driver, "Valid_username", "")
    validate_successful_login(driver) 

def fill_login_form(driver,username,passwd):
    driver.find_element(By.XPATH, "//input[@id='username']").send_keys(username)
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys(passwd)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(1)

def validate_successful_login(driver):
    time.sleep(1)  # Add delay to allow the registration process to complete
    try:
        Logout_btn = driver.find_element(By.XPATH, '/html/body/header/div/div/div/nav/ul/li[4]/a')  # Example success message element
        assert "Logout" in Logout_btn.text  # Example validation condition
        Logout_btn.click()
        print("Success: User Logged in Successfully")
    except:
        print("Failed: Invalid Username or password")

driver = webdriver.Chrome()  # Use the appropriate driver (Chrome, Firefox, etc.)

def main():
    test_valid_user_login(driver)
    test_invalid_username_login(driver)
    test_invalid_password_login(driver)
    test_missing_username(driver)
    test_missing_password(driver)