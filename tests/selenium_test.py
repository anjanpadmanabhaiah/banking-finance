from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--headless")  # Run in headless mode for Jenkins
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
driver.get("http://18.216.78.229:8085")  # Test server URL

try:
    # ✅ Check page title
    WebDriverWait(driver, 20).until(EC.title_contains("CBS"))
    print("✅ Title check passed!")

    # ✅ Check banner heading
    banner_heading = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Customer Banking Services')]"))
    )
    assert "Customer Banking Services" in banner_heading.text
    print("✅ Banner heading check passed!")

    # ✅ Check services section heading
    services_heading = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'WELCOME TO CUSTOMER BANKING SERVICES')]"))
    )
    assert "WELCOME TO CUSTOMER BANKING SERVICES" in services_heading.text
    print("✅ Services section check passed!")

    print("🎉 All homepage checks passed successfully!")

except Exception as e:
    print("❌ Test failed:", e)
    driver.save_screenshot("homepage_failure.png")
    raise
finally:
    driver.quit()
