import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C://chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()
"""
driver.get("https://www.familysearch.org/en/")


button = driver.find_element_by_xpath("//button[text()='Search']")
action = ActionChains(driver)
action.move_to_element(button).click().perform()

driver.find_element_by_link_text("Genealogies").click()
"""

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
action = ActionChains(driver)
doubleClick = driver.find_element_by_id("double-click")
action.move_to_element(doubleClick).perform()

alert = driver.switch_to.alert
assert "You double clicked me!!!, You got to be kidding me" == alert.text
alert.accept()
