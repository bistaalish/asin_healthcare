from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest
# from webdriver_manager.chrome import ChromeDriverManager
def test_valid_user_registration(driver):
    driver.get("http://127.0.0.1:8000/")  # Replace with your website"s URL
    time.sleep(2)
    register_btn = driver.find_element(By.CSS_SELECTOR, "a#register_btn.main-button-slider")
    register_btn.click()
    time.sleep(2)
    fill_registration_form(driver, "valid_username", "valid_email@example.com", "Valid!123", "Valid!123")
    validate_successful_registration(driver)

def test_valid_user2_registration(driver):
    driver.get("http://127.0.0.1:8000/")  # Replace with your website"s URL
    time.sleep(2)
    register_btn = driver.find_element(By.CSS_SELECTOR, "a#register_btn.main-button-slider")
    register_btn.click()
    time.sleep(2)
    fill_registration_form(driver, "valid_username1", "valid_email@example.com", "Valid!123", "Valid!123")
    validate_successful_registration(driver)
    
def test_duplicate_user(driver):
    print("Testing with Duplicate Values")
    try:
        fill_registration_form(driver, "valid_username", "valid_email@example.com", "Valid!123", "Valid!123")
        validate_successful_registration(driver)
        print("Failed: This should have been false")
    except:
        print("Success: Duplicate Value Error")
def test_invalid_email_registration(driver):
    driver.get("http://127.0.0.1:8000/")  # Replace with your website"s URL
    register_btn = driver.find_element(By.CSS_SELECTOR, "a#register_btn.main-button-slider")
    register_btn.click()
    time.sleep(2)
    fill_registration_form(driver, "invalid_username", "invalid_email", "weak", "differentPassword")
    invalid_email_registration(driver)

def test_different_password_registration(driver):
    driver.get("http://127.0.0.1:8000/")  # Replace with your website"s URL
    register_btn = driver.find_element(By.CSS_SELECTOR, "a#register_btn.main-button-slider")
    register_btn.click()
    time.sleep(2)
    fill_registration_form(driver, "invalid_username", "valid@example.com", "weak", "differentPassword")
    different_pass_registration(driver)

def fill_registration_form(driver, username, email, password, confirm_password):
    uname_input = driver.find_element(By.XPATH, "(//input[@id='username'])[2]")
    email_input = driver.find_element(By.XPATH, "//input[@id='email']")
    pass1_input = driver.find_element(By.XPATH, "//input[@id='password1']")
    pass2_input = driver.find_element(By.XPATH, "//input[@id='password2']")
    register_btn = driver.find_element(By.XPATH, "//button[@id='register_button']")

    uname_input.clear()
    email_input.clear()
    pass1_input.clear()
    pass2_input.clear()    
    uname_input.send_keys(username)
    email_input.send_keys(email)
    pass1_input.send_keys(password)
    pass2_input.send_keys(confirm_password)
    register_btn.click()
    time.sleep(1)

def validate_successful_registration(driver):
    print("Testing Valid Data for Registration")
    time.sleep(2)  # Add delay to allow the registration process to complete
    Logout_btn = driver.find_element(By.XPATH, '/html/body/header/div/div/div/nav/ul/li[4]/a')  # Example success message element
    assert "Logout" in Logout_btn.text  # Example validation condition
    Logout_btn.click()
    print("Success: User Created Successfully")


def invalid_email_registration(driver):
    time.sleep(1)  # Add delay to allow the validation process
    print("Testing with invalid email")
    try:
        error_message = driver.find_element(By.XPATH, '/html/body/header/div/div/div/nav/ul/li[4]/a').text  # Example error message element
        print("Failed: Email Validation not working")
        assert "Logout" not in error_message  # Example validation condition
    except:
        print("Success: Warning for invalid email")

def different_pass_registration(driver):
    time.sleep(1)  # Add delay to allow the validation process
    print("Testing with Different password")
    try:
        error_message = driver.find_element(By.XPATH, '/html/body/header/div/div/div/nav/ul/li[4]/a').text  # Example error message element
        print("Failed: Registered with different password")
        # assert "Logout" not in error_message  # Example validation condition
    except:
        print("Success: User Registration Failed using different password")

def main():
# Usage
    driver = webdriver.Chrome()  # Use the appropriate driver (Chrome, Firefox, etc.)
    test_valid_user_registration(driver)
    test_invalid_email_registration(driver)
    test_different_password_registration(driver)
    test_duplicate_user(driver)
    test_valid_user2_registration(driver)
    driver.quit()