from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
from dotenv import load_dotenv # Use you own dotenv script for your authentication username and password, the variables must be PASS and NUM as is configured.
import os
load_dotenv()
def tabSwitch(): # Used to handle things open in new tabs, run this if your authentication ever pops up a new window.
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
PASS = os.getenv('PASS') # School password and ID, will need to be configured in a .env or to your school authentication means.
NUM = os.getenv("NUM")
driver = webdriver.Firefox() # Uses firefox, if you want to run headless use the chrome browers with the headless flag
driver.get("https://wakeid2.wcpss.net/") # Start of authentication, currently configured for Wake County Public School System.
assert "WakeID Portal" in driver.title
while True: # These while loops are needed because it gives the page time to load, and to change if there are any delays in the script.
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
tabSwitch() # Switches to powerschool tab
while True: # This is the start of the grade-grabbing, and is the most important part of the script to change.
    try:
        assert "Grades and Attendance" in driver.title
    except:
        sleep(1)
    else:
        sleep(3)
        break
grades = driver.find_elements_by_xpath('//*[@class="bold"]') # This grabs bold elements because the grade numbers don't have unique identification (ffs)
classes = driver.find_elements_by_xpath('//*[@align="left"]') # This grabs the class names because the class names don't have unique identification (also ffs)
for i in range(len(classes)): # Grabs all classes and strips teacher information
    clas = classes[i]
    cla = clas.text.split('\n')
    #print(cla[0])
try: # Checks if you have your second semester classes yet, will need to be configured for yourself
    grades[9].text
    grades[11].text
    grades[13].text
    grades[15].text
except:
    pass
else: # Splits grades into arrays with the exact grade and the rounded grade
    for i in range(len(grades)):
        grad = grades[i]
        gra = grad.text.split('\n')
form = [[classes[1].text.split('\n')[0], grades[1].text.split('\n')], [classes[3].text.split('\n')[0], grades[3].text.split('\n')], [classes[5].text.split('\n')[0], grades[7].text.split('\n')], [classes[7].text.split('\n')[0], grades[9].text.split('\n')]] # This big array is a list of all of your grades and class names, currently configured for first semester grades. You will need to change the numbers in this array to change which classes and which grades you have.
print(len(form), len(grades), len(classes))
for i in range(len(form)): # Prints each class in the format of "Class name: Rounded Grade (exact grade)
    print(form[i][0] + "\b:", form[i][1][0], "(" + form[i][1][1] + ")")
##print(form[0][0] + "\b:", form[0][1][0], "(" + form[0][1][1] + ")")
##print(form[1][0] + "\b:", form[1][1][0], "(" + form[1][1][1] + ")")
##print(form[2][0] + "\b:", form[2][1][0], "(" + form[2][1][1] + ")")
##print(form[3][0] + "\b:", form[3][1][0], "(" + form[3][1][1] + ")")

driver.close()
