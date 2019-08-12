"""
This file contains python code that will be used to control the Chrome web browser. It
uses the Selenium python package along with a ChromeDriver to use the entered information from the
GUI to navigate through the web pages to automate the Manhattan College class registration
process.

Created by: Erik Mejia
"""

import selenium.common.exceptions as EX
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Function that will preform that actual automation process
def bot(username, password, class_list, chromedriver_filepath):

    # Create webdriver object that will open the chrome browser window
    chrome_browser = webdriver.Chrome(chromedriver_filepath)
    chrome_browser.get('https://manhattan.edu/')

    '''  
    The following code navigates the chrome browser and enters the entered Username, Password, and
    CRN's in their respective entry boxes in the chrome browser. The function is able to navigate the webpages by
    selecting certain elements within the webpages based on the HTML ID tags, Class names, and link texts.
    Multiple Try and Except cases are used along with Explicit Waits to ensure all the elements are loaded properly
    to prevent and/or catch errors.
    '''

    # Navigating to Current Students link
    try:
        page_element = WebDriverWait(chrome_browser, 4).until(EC.presence_of_element_located((By.LINK_TEXT, 'CURRENT STUDENTS')))
        page_element.click()
    except EX.NoSuchElementException:
        return 'error'

    # Navigating to Self Service Portal
    try:
        page_element = WebDriverWait(chrome_browser, 4).until(EC.presence_of_element_located((By.LINK_TEXT, 'Self Service')))
        page_link = page_element.get_attribute('href')
    except EX.NoSuchElementException:
        return 'error'

    chrome_browser.get(page_link)

    # Logging into Self Service Portal
    try:
        username_entry_bar = chrome_browser.find_element_by_id('username')
        password_entry_bar = chrome_browser.find_element_by_id('password')

        username_entry_bar.send_keys(username)
        password_entry_bar.send_keys(password)
        password_entry_bar.send_keys(Keys.ENTER)
    except EX.NoSuchElementException:
        return 'error'

    # Checking if Login Credentials were valid or not
    try:
        page_element = chrome_browser.find_element_by_id('bmenu--P_StuMainMnu___UID4')
        page_element.click()
    except EX.NoSuchElementException:
        return 'invalid'

    # Navigating to class Registration page
    try:
        page_element = WebDriverWait(chrome_browser, 4).until(EC.presence_of_element_located((By.ID, 'bmenu--P_RegMnu___UID0')))
        page_element.click()
    except EX.NoSuchElementException:
        return 'error'

    try:
        page_element = WebDriverWait(chrome_browser, 4).until(EC.presence_of_element_located((By.ID, 'contentItem11')))
        page_element.click()
    except EX.NoSuchElementException:
        return 'error'

    try:
        page_element = WebDriverWait(chrome_browser, 4).until(EC.presence_of_element_located((By.CLASS_NAME, 'defaultButtonSmall')))
        page_element.click()
    except EX.NoSuchElementException:
        return 'error'

    # Loop to refresh the page until class registration opens
    while True:
        try:
            chrome_browser.find_element_by_id('crn_id1')
            break
        except EX.NoSuchElementException:
            chrome_browser.execute_script("window.history.go(-1)")
            page_element = chrome_browser.find_element_by_class_name('defaultButtonSmall')
            page_element.click()

    # Entering the CRN's into their respective entry fields
    count = 1
    for CRN in class_list:
        crn_entry_box = chrome_browser.find_element_by_id('crn_id{}'.format(count))
        crn_entry_box.send_keys(CRN)
        count += 1

    crn_entry_box.send_keys(Keys.ENTER)
    return 'success'
