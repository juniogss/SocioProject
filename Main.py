from selenium import webdriver
from selenium.webdriver.common.by import By

username = "xxx"
password = "xxx"

url = "https://socio5estrelas.com.br/"

path = "chromedriver"
driver = webdriver.Chrome(path)

driver.get(url)
driver.find_element(By.CSS_SELECTOR, ".header-7__content-navigation a").click()

driver.find_element(By.ID, "mat-input-0").send_keys(username)
driver.find_element(By.ID, "mat-input-1").send_keys(password)
driver.find_element(By.CLASS_NAME, "login-btn").click()

