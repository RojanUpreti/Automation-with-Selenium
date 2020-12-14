from selenium import webdriver
chrome_browser=webdriver.Chrome('chromedriver.exe')
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
chrome_browser.maximize_window()
user_msg=chrome_browser.find_element_by_id('user-message')
user_msg.send_keys('I am Rojan Upreti')
show_message_button=chrome_browser.find_element_by_class_name('btn-default')
show_message_button.click()