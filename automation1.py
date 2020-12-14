from selenium import webdriver

chrome_browser=webdriver.Chrome("./chromedriver")
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

chrome_browser.maximize_window()

assert 'Selenium Easy Demo' in chrome_browser.title

show_message_button=chrome_browser.find_element_by_class_name('btn-default')

# print(show_message_button.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

user_message=chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('I am Rojan Upreti')
# driver.is_element_present_by_css('div[class*="at-cv-lightbox-header"]')

show_message_button.click()
chrome_browser.close()
chrome_browser.close()
chrome_browser.quit()

# output_message=chrome_browser.find_element_by_id('display')
# assert 'I am Rojan Upreti' in output_message.text