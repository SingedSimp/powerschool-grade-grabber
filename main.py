from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
from dotenv import load_dotenv
import os
load_dotenv()
def tabSwitch():
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
PASS = os.getenv('PASS')
NUM = os.getenv("NUM")
driver = webdriver.Firefox()
driver.get("https://wakeid2.wcpss.net/")
assert "WakeID Portal" in driver.title
while True:
    try:
        select = Select(driver.find_element_by_id("ember470"))
    except:
        sleep(0.5)
    else:
        select.select_by_visible_text('Student')
        break
elem = driver.find_element_by_id("identification")
elem.clear()
elem.send_keys(str(NUM))
elem.send_keys(Keys.RETURN)
sleep(1)
while True:
    try:
        elem = driver.find_element_by_id("ember549")
    except:
        sleep(0.5)
    else:
        break
elem.clear()
elem.send_keys(str(PASS))
elem.send_keys(Keys.RETURN)
sleep(1)
while True:
    try:
        assert "Applications | RapidIdentity" in driver.title
    except:
        sleep(1)
    else:
        break
while True:
    try:
        driver.find_element_by_xpath('//*[@title="WakeID Portal"]').click()
    except:
        sleep(0.5)
    else:
        break
sleep(1)
tabSwitch()
while True:
    try:
        assert "WakeID Portal" in driver.title
    except:
        sleep(1)
    else:
        sleep(3)
        break
while True:
    try:
        driver.find_element_by_xpath('//*[@aria-label="Homebase"]').click()
    except:
        sleep(0.5)
    else:
        sleep(0.5)
        break
tabSwitch()
while True:
    try:
        elem = driver.find_element_by_id("identification")
    except:
        sleep(0.5)
    else:
        break
elem.clear()
elem.send_keys(str(NUM))
elem.send_keys(Keys.RETURN)
sleep(1)
while True:
    try:
        assert "RapidIdentity" in driver.title
    except:
        sleep(1)
    else:
        sleep(5)
        break
while True:
    try:
        driver.find_element_by_xpath('//*[@title="PowerSchool Student - LEA 920"]').click()
    except:
        sleep(0.5)
    else:
        break
tabSwitch()
while True:
    try:
        assert "Grades and Attendance" in driver.title
    except:
        sleep(1)
    else:
        sleep(3)
        break
grades = driver.find_elements_by_xpath('//*[@class="bold"]')
classes = driver.find_elements_by_xpath('//*[@align="left"]')
for i in range(len(classes)):
    clas = classes[i]
    cla = clas.text.split('\n')
    #print(cla[0])
try:
    grades[9].text
    grades[11].text
    grades[13].text
    grades[15].text
except:
    pass
else:
    for i in range(len(grades)):
        grad = grades[i]
        gra = grad.text.split('\n')
form = [[classes[1].text.split('\n')[0], grades[1].text.split('\n')], [classes[3].text.split('\n')[0], grades[3].text.split('\n')], [classes[5].text.split('\n')[0], grades[7].text.split('\n')], [classes[7].text.split('\n')[0], grades[9].text.split('\n')]]
print(form)
print(len(form), len(grades), len(classes))
for i in range(len(form)):
    print(form[i][0] + "\b:", form[i][1][0], "(" + form[i][1][1] + ")")
##print(form[0][0] + "\b:", form[0][1][0], "(" + form[0][1][1] + ")")
##print(form[1][0] + "\b:", form[1][1][0], "(" + form[1][1][1] + ")")
##print(form[2][0] + "\b:", form[2][1][0], "(" + form[2][1][1] + ")")
##print(form[3][0] + "\b:", form[3][1][0], "(" + form[3][1][1] + ")")

driver.close()
