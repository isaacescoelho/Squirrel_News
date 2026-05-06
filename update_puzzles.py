from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

# Use an existing Chrome profile so puzzle sessions/logins are preserved
chrome_options.add_argument("--user-data-dir=/Users/isaac.coelho/Library/Application Support/Google/Chrome")
chrome_options.add_argument("--profile-directory=Profile 6")

# Suppress the "Chrome is being controlled by automated software" banner
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://puzzleme.amuselabs.com/pmm/dashboard?set=2f329e7cb0eba95a30592abf0de92cf3196fef60eabf8ff13e095072ed5a443b")