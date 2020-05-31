
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C://chromedriver.exe")

driver.get("https://rahulshettyacademy.com/angularpractice/")

# driver.find_element_by_name("name").send_keys("Barinder")
driver.find_element_by_css_selector("input[name='name']").send_keys("Barinder")
# driver.find_element_by_name("email").send_keys("riarbarinder@outlook.com")

driver.find_element_by_id("exampleInputPassword1").send_keys("test")
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)


driver.find_element_by_id("exampleCheck1").click()
driver.find_element_by_xpath("//input[@type='submit']").click()
message = driver.find_element_by_class_name("alert-success").text

assert "success" in message

