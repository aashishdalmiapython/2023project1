from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver=webdriver.Chrome(executable_path=r"E:\NewPythonSeleniumProjects\Drivers\chromedriver.exe")
driver.get(url="https://buy.insight.com/gb/")
print(driver.current_url)
print(driver.title)
driver.maximize_window()
time.sleep(7)
driver.find_element(By.XPATH,"//div[@class='yCmsContentSlot']/a" ).click()

driver.find_element(By.XPATH,"//form[@name='search_form_SearchBox']/div/input").click()
driver.find_element(By.XPATH,"//form[@name='search_form_SearchBox']/div/input").send_keys("Dynamic 365 Commerce")
driver.find_element(By.XPATH,"//form[@name='search_form_SearchBox']/div/input").send_keys(Keys.ENTER)
time.sleep(7)
driver.find_element(By.XPATH,"//div[@data-product-code='CFQ7TTC0LH2Z0002']/div[2]/a").click()
driver.find_element(By.XPATH,"//button[@id='addToCartButton']").click()
time.sleep(5)

allwindows=driver.window_handles
for win in allwindows:
    driver.switch_to.window(win)
    if driver.find_element(By.XPATH,"//a[contains(text(),'Continue to ch')]").is_displayed():
        driver.find_element(By.XPATH,"//a[contains(text(),'Continue to ch')]").click()
        time.sleep(5)
print(driver.title)
print(driver.current_url)
if driver.title =="Your Shopping Basket | Insight UK Site":
    print("We are on cart page"+"- Passed")
