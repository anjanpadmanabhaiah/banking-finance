from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--headless=new")  # newer headless mode
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
driver.get("http://18.216.78.229:8085")

# wait until page loads and title contains "Banking"
WebDriverWait(driver, 10).until(EC.title_contains("Banking"))

assert "Banking" in driver.title
print("✅ Homepage test passed!")

driver.quit()
