from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

service = ChromeService(executable_path=ChromeDriverManager().install())

chrome_browser = webdriver.Chrome(service=service)
chrome_browser.maximize_window()
chrome_browser.get('http://demo.seleniumeasy.com/basic-first-form-demo.html')

assert 'Selenium Easy' in chrome_browser.page_source
show_message_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-default')
print(show_message_button.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source
user_message = chrome_browser.find_element(By.ID, 'user-message')
user_message.clear()
user_message.send_keys('FILL IN TEXT')

show_message_button.click()

output_message = chrome_browser.find_element(By.ID, 'display')
assert 'FILL IN TEXT' in output_message.text

chrome_browser.close()
# automatically close browser window
