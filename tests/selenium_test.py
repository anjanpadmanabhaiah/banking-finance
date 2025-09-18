from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")  # run headless for Jenkins
driver = webdriver.Chrome(options=options)

driver.get("http://18.216.78.229:8085")  # replace with your test server URL

assert "Banking" in driver.title  # validate page title
print("✅ Homepage test passed!")

driver.quit()

