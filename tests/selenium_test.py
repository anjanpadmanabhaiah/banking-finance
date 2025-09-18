from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

driver.get("http://localhost:8085")  # Use service port inside EC2

print("✅ Page loaded successfully!")
driver.quit()
