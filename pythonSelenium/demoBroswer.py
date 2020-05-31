from selenium import webdriver

driver = webdriver.Chrome(executable_path="C://chromedriver.exe")

driver.get("https://rahulshettyacademy.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.back()
driver.refresh()
driver.minimize_window()
