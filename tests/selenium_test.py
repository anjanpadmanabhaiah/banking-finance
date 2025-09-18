from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

# Use localhost since Jenkins is running on the same server as Docker
APP_URL = "http://localhost:8085"

driver.get(APP_URL)

try:
    WebDriverWait(driver, 30).until(EC.title_contains("CBS"))  # your page <title>CBS</title>
    print("✅ Homepage test passed!")
except Exception as e:
    print("❌ Homepage test failed:", e)
    driver.save_screenshot("homepage_failure.png")
    raise
finally:
    driver.quit()
