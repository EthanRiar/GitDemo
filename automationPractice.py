from selenium import webdriver

driver = webdriver.Chrome(executable_path="C://chromedriver.exe")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

list1 = driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(list1))

#list1[1].click()
# OR
for item in list1:
    if item.get_attribute("value") == "option2":
        item.click()
        break
    else:
        continue

list2 = driver.find_elements_by_xpath("//input[@type='radio']")

for r in list2:
    if r.get_attribute("value") == "radio2":
        r.click()
        break
