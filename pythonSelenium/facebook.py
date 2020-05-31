from selenium import webdriver

driver = webdriver.Chrome(executable_path="C://chromedriver.exe")
driver.get("https://www.expedia.ca/")
driver.find_element_by_class_name("uitk-button-toggle-content").click()