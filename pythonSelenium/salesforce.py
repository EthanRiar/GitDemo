from selenium import webdriver

driver = webdriver.Chrome(executable_path="C://chromedriver.exe")

driver.get("https://login.salesforce.com/")
driver.find_element_by_css_selector("#username").send_keys("barinder90")
print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)
driver.find_element_by_css_selector("#password").send_keys("barinder90")

driver.find_element_by_link_text("Forgot Your Password?").click()
driver.find_element_by_link_text("Cancel").click()
driver.find_element_by_xpath("//a[text()='Cancel']").click()
