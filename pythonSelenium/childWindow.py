from selenium import webdriver

driver = webdriver.Chrome(executable_path="C://chromedriver.exe")

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element_by_link_text("Click Here").click()
childWindow = driver.window_handles[1]
parentWindow = driver.window_handles[0]
driver.switch_to.window(childWindow)
print(driver.find_element_by_tag_name("h3").text)
driver.close()
driver.switch_to.window(parentWindow)
print(driver.find_element_by_tag_name("h3").text)