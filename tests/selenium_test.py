from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

# Open Google to confirm Selenium works
driver.get("https://www.google.com")

assert "Google" in driver.title
print("✅ Simple Selenium test passed!")

driver.quit()
