import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

driver = webdriver.Chrome()
time.sleep(5)

driver.get("http://127.0.0.1:8000/admin")
time.sleep(5)

login = driver.find_element_by_id("id_username")
login.send_keys("vasil")
password = driver.find_element_by_id("id_password")
password.send_keys("KH123456")

submit_button = driver.find_element_by_xpath("//*[@type='submit']").click()
time.sleep(2)
admin_page = driver.find_element_by_xpath("//*[text() = 'Posts']").click()
add_post = driver.find_element_by_xpath("//a[contains(text(),'Add post')]").click()
add_author = driver.find_element_by_id("id_author").click()
select_author = driver.find_element_by_xpath("//option[text()='vasil']").click()
title = driver.find_element_by_id("id_title")
title.send_keys("This is my manifest")
text = driver.find_element_by_id("id_text")
text.send_keys("Your ads could be here")
driver.execute_script("window.scrollBy(0, 200);")
date = driver.find_element_by_css_selector('body.app-blog.model-post.change-form:nth-child(2) div.main.shifted:nth-child(3) div.content:nth-child(3) div.colM:nth-child(1) fieldset.module.aligned:nth-child(1) div.form-row.field-published_date:nth-child(5) div:nth-child(1) p.datetime:nth-child(2) span.datetimeshortcuts:nth-child(2) > a:nth-child(1)')
date.click()
time = driver.find_element_by_xpath('//div[5]//div[1]//p[1]//span[2]//a[1]').click()
button = driver.find_element_by_name("_save").click()
success_message = driver.find_elements_by_class_name("success")
assert True

driver.get('http://127.0.0.1:8000/')
name = driver.find_element_by_xpath("//a[contains(text(),'This is my manifest')]")
assert True
driver.quit()
