from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

driver.get("http://18.216.78.229:8085")

try:
    WebDriverWait(driver, 30).until(EC.title_contains("Banking"))
    print("✅ Homepage test passed!")
except Exception as e:
    print("❌ Homepage test failed:", e)
    driver.save_screenshot("homepage_failure.png")  # saves screenshot for debugging
    raise
finally:
    driver.quit()
