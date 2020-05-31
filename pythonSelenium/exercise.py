import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

driver.find_element_by_xpath("//a[text()='Shop']").click()

products = driver.find_elements_by_xpath("//div[@class='card h-100']")

for product in products:
    productName = product.find_element_by_xpath("div/h4/a").text
    if productName == "Blackberry":
        product.find_element_by_xpath("div/button").click()
        break

driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()

driver.find_element_by_xpath("//button[@class='btn btn-success']").click()

driver.find_element_by_id("country").send_keys("Canada")

time.sleep(5)
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_xpath("//input[@class='btn btn-success btn-lg']").click()

assert "Success! Thank you!" in driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text
driver.get_screenshot_as_file("screen.png")