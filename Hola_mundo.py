from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

chromedriver_path = r"C:\Drivers2\chromedriver-win64\chromedriver.exe"

service = Service(executable_path=chromedriver_path)

driver = webdriver.Chrome(service=service)

driver.get('https://demoqa.com/text-box')
driver.maximize_window()
time.sleep(4)

nom = driver.find_element(By.XPATH, "//input[contains(@id,'userName')]")
nom.send_keys("Cintia")
time.sleep(8)

driver.close()
