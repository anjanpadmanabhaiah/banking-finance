from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

driver.get("http://18.216.78.229:8085")

# Just check the page title has "Banking"
assert "Banking" in driver.title

print("✅ Simple test passed!")

driver.quit()
