import time

from selenium import webdriver


driver = webdriver.Chrome(executable_path="C://chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
#driver.find_element_by_class_name("search-keyword").send_keys("ber")
time.sleep(4)

driver.find_elements_by_xpath("//div[@class='products']/div")
list1 = driver.find_elements_by_xpath("//div[@class='product-action']/button")

list2 = []
for item in list1:
    list2.append(item.find_element_by_xpath("parent::div/parent::div/h4").text)
    item.click()

print(list2)
list3 = []
driver.find_element_by_xpath("//a[@class='cart-icon']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
beforePrice = driver.find_element_by_xpath("//span[@class='discountAmt']").text
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_class_name("promoBtn").click()
veggies = driver.find_elements_by_css_selector("p.product-name")
for i in veggies:
    list3.append(i.text)
print(list3)
print(driver.find_element_by_xpath("//span[@class='promoInfo']").text)
afterPrice = driver.find_element_by_css_selector("span.discountAmt").text
amounts = driver.find_elements_by_xpath("//tr/td[5]/p")
sum = 0
for amount in  amounts:
    sum += int(amount.text)
print(sum)
total = int(driver.find_element_by_xpath("//span[@class='totAmt']").text)
assert list2 == list3
assert float(beforePrice) > float(afterPrice)
assert sum == total








