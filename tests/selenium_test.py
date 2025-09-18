from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

try:
    driver.get("http://18.216.78.229:8085")

    # ✅ Wait until page title contains "CBS" (your <title>CBS</title>)
    WebDriverWait(driver, 30).until(EC.title_contains("CBS"))

    print("✅ Homepage test passed!")

except Exception as e:
    print("❌ Homepage test failed:", e)
    driver.save_screenshot("homepage_failure.png")  # screenshot saved in Jenkins workspace
    raise

finally:
    driver.quit()
