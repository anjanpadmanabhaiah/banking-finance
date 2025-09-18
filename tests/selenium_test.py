from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

# Use public EC2 IP for test server
driver.get("http://18.216.78.229:8085")

try:
    WebDriverWait(driver, 20).until(EC.title_contains("Banking"))
    print("✅ Page loaded successfully!")
except Exception as e:
    print("❌ Test failed:", e)
    driver.save_screenshot("selenium_failure.png")
    raise
finally:
    driver.quit()
