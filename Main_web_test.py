# import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://creddit.tech")

driver.maximize_window()
print(driver.title)
# Wait for some time before quitting
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "non-existent-id")))
# time.sleep(5)
driver.quit()