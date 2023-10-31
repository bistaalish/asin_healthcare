from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest

url = "http://127.0.0.1:8000/"
username="valid_username"
username1="valid_username1"
password="Valid!123"
firstName="asin"
email="sb-yugwr27163237@business.example.com"
passwd="U05vrAu^"

def test_buy_products(driver):
    driver.get(url)  # Replace with your website"s URL
    time.sleep(2)
    login_btn = driver.find_element(By.CSS_SELECTOR, "a#login_btn.main-button-slider")
    login_btn.click()
    time.sleep(2)
    fill_login_form(driver,username,password)
    buy_product1(driver,firstName,email,passwd)
    buy_product2(driver)
    buy_product3(driver)
    Logout_btn = driver.find_element(By.XPATH, '/html/body/header/div/div/div/nav/ul/li[4]/a')
    Logout_btn.click()
    time.sleep(2)

def buy_product3(driver):
    print("test Buy Product 3")
    driver.find_element(By.XPATH, '//*[@id="pricing-plans"]/div/div[2]/div[3]/div/div[4]/a').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="payment-submit-btn"]').click()
    print("Success: Buy Product 3")
    time.sleep(10)

def buy_product2(driver):
    print("Test Buy Product 2")
    driver.find_element(By.XPATH, '//*[@id="pricing-plans"]/div/div[2]/div[2]/div/div[4]/a').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="payment-submit-btn"]').click()
    print("Success: Buy Product 2")
    time.sleep(2)
        
def buy_product1(driver,firstName,email,passwd):
    print("Test Buy Product 1")
    driver.find_element(By.XPATH, "//a[contains(text(),'Buy product')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys(firstName)
    driver.find_element(By.XPATH, "(//input[@id='email'])[2]").send_keys(email)
    driver.find_element(By.XPATH, "//form[@id='payment_KYC']/div[4]/label").click()
    driver.find_element(By.XPATH, "//button[@id='submitButton']").click()
    time.sleep(4)
    try:
        driver.find_element(By.XPATH, "//input[@id='email']").send_keys(email)
        # driver.find_element(By.XPATH, "//input[@id='password']").send_keys(passwd)
        driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(passwd)
        driver.find_element(By.XPATH, '//*[@id="btnLogin"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="payment-submit-btn"]').click()
        time.sleep(3)
        print("Success: Buy Product 1")
    except:
        print("Failed: Failed to Buy Product 1")


def fill_login_form(driver,username,passwd):
    driver.find_element(By.XPATH, "//input[@id='username']").send_keys(username)
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys(passwd)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)

def test_buy_all_products(driver):
    print("Test Buy all Products")
    driver.get(url)  # Replace with your website"s URL
    time.sleep(2)
    login_btn = driver.find_element(By.CSS_SELECTOR, "a#login_btn.main-button-slider")
    login_btn.click()
    time.sleep(2)
    fill_login_form(driver,username1,password)
    driver.find_element(By.XPATH, '//*[@id="welcome"]/div/div[2]/div/div/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys(firstName)
    driver.find_element(By.XPATH, "(//input[@id='email'])[2]").send_keys(email)
    driver.find_element(By.XPATH, "//form[@id='payment_KYC']/div[4]/label").click()
    driver.find_element(By.XPATH, "//button[@id='submitButton']").click()
    try:
        driver.find_element(By.XPATH, "//input[@id='email']").send_keys(email)
        # driver.find_element(By.XPATH, "//input[@id='password']").send_keys(passwd)
        driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(passwd)
        driver.find_element(By.XPATH, '//*[@id="btnLogin"]').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="payment-submit-btn"]').click()
        time.sleep(2)
        print("Success: Buy All Product")
    except:
        print("Failed: Faield to buy All Product")
    time.sleep(10)

def main():
    driver = webdriver.Chrome()  # Use the appropriate driver (Chrome, Firefox, etc.)
    test_buy_products(driver)
    test_buy_all_products(driver)