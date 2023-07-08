import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

chrome_driver_path = './chromedriver'
firefox_driver_path = './geckodriver'
chrome_service = ChromeService(executable_path=chrome_driver_path)


def open_firefox_task(url: str, local_driver: bool = False):
    try:
        if(local_driver):
            firefox_options = FirefoxOptions()
            firefox_options.binary_location = firefox_driver_path
            firefox_driver = webdriver.Firefox(options=firefox_options)  # Doesn't work for me
        else:
            firefox_driver = webdriver.Firefox()

        firefox_driver.get(url)
        firefox_driver.quit()
    except Exception as exception:
        print("Error with Firefox Webdriver.")
        print(exception)


def open_chrome_task(url: str):
    try:
        with webdriver.Chrome(service=chrome_service) as driver:
            driver.get(url)
            page_title = driver.title
            print(page_title)
            driver.refresh()
            new_title = driver.title
            print(new_title)
            assert new_title == page_title
            print("New title is the same as the previous title")
    except AssertionError as error:
        print("Website Name isn't equal Website Title")
    except Exception as error:
        print(error)


# Not reusing code only for task purposes, would create a reusable function and variables in production.
def google_translate_task4(url: str, str_to_translate: str, xpath: str):
    try:
        with webdriver.Chrome(service=chrome_service) as driver:
            driver.get(url)
            WebDriverWait(driver, 15).until(presence_of_element_located((By.XPATH, xpath)))
            translation_box = driver.find_element(By.XPATH, xpath)
            translation_box.send_keys(str_to_translate)
            input()
    except Exception as exception:
        print("Error with Chrome Webdriver.")
        print(exception)


# Not reusing code only for task purposes, would create a reusable function and variables in production.
def youtube_task5(url: str, song_to_search: str, input_name: str, search_button_id: str):
    try:
        with webdriver.Chrome(service=chrome_service) as driver:
            driver.get(url)
            WebDriverWait(driver, 15).until(presence_of_element_located((By.TAG_NAME, 'body')))

            search_input = driver.find_element(By.NAME, input_name)
            search_input.send_keys(song_to_search)

            search_button = driver.find_element(By.ID, search_button_id)
            search_button.click()
            input()
    except Exception as exception:
        print("Error with Chrome Webdriver.")
        print(exception)

# Not reusing code only for task purposes, would create a reusable function and variables in production.
def google_translate_task6(url: str):
    try:
        with webdriver.Chrome(service=chrome_service) as driver:
            driver.get(url)
            WebDriverWait(driver, 15).until(presence_of_element_located((By.TAG_NAME, 'body')))

            translate_input_1 = driver.find_element(By.TAG_NAME, 'textarea') # 1st text area is input 26/06/2023
            translate_input_2 = driver.find_element(By.XPATH, '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea')
            translate_input_3 = driver.find_element(By.CSS_SELECTOR, '[aria-label="Source text"]')

            print(translate_input_1)
            print(translate_input_2)
            print(translate_input_3)
            input()
    except Exception as exception:
        print("Error with Chrome Webdriver.")
        print(exception)

# Not reusing code only for task purposes, would create a reusable function and variables in production.
def facebook_task7(url: str, username: str, password: str):
    try:
        with webdriver.Chrome(service=chrome_service) as driver:
            driver.get(url)
            WebDriverWait(driver, 15).until(presence_of_element_located((By.TAG_NAME, 'body')))

            username_input = driver.find_element(By.NAME, 'email')
            username_input.send_keys(username)

            password_input = driver.find_element(By.NAME, 'pass')
            password_input.send_keys(password)

            search_button = driver.find_element(By.NAME, 'login')
            search_button.click()
            input()
    except Exception as exception:
        print("Error with Chrome Webdriver.")
        print(exception)


# Not reusing code only for task purposes, would create a reusable function and variables in production.
def deletecookies_task8(url: str):
    try:
        with webdriver.Chrome(service=chrome_service) as driver:
            driver.get(url)
            WebDriverWait(driver, 15).until(presence_of_element_located((By.TAG_NAME, 'body')))
            driver.delete_all_cookies()
            print(driver.get_cookies())
            input()
    except Exception as exception:
        print("Error with Chrome Webdriver.")
        print(exception)


# Not reusing code only for task purposes, would create a reusable function and variables in production.
def github_task9(url: str, search_string: str):
    try:
        with webdriver.Chrome(service=chrome_service) as driver:
            driver.get(url)
            WebDriverWait(driver, 15).until(presence_of_element_located((By.TAG_NAME, 'body')))
            search_input = driver.find_element(By.NAME, 'q')
            search_input.send_keys(search_string)
            search_input.send_keys(Keys.RETURN)
            input()
    except Exception as exception:
        print("Error with Chrome Webdriver.")
        print(exception)


# Not reusing code only for task purposes, would create a reusable function and variables in production.
def disable_all_extensions_task10(url: str):
    try:
        chrome_options = ChromeOptions()  # I imported Options as ChromeOptions,
        # The same solution is available for all browsers per "Options" passed when starting the driver.
        chrome_options.add_argument("--disable-extensions")
        with webdriver.Chrome(service=chrome_service, options=chrome_options) as driver:
            driver.get(url)
            input()
    except Exception as exception:
        print("Error with Chrome Webdriver.")
        print(exception)


def run_without_extensions_task11(url: str):
    try:
        chrome_options = ChromeOptions()  # I imported Options as ChromeOptions,
        chrome_options.add_argument("--incognito")
        with webdriver.Chrome(service=chrome_service, options=chrome_options) as driver:
            driver.get(url)
            input()
    except Exception as exception:
        print("Error with Chrome Webdriver.")
        print(exception)

# Firefox Task - Uncomment to run:
# open_firefox_task('https://ynet.co.il')

# Chrome Task - Uncomment to run:
# open_chrome_task('https://walla.co.il')

# Answer for task 3: Yes, unless there is a browser specific code in the website for compatibility or other reasons.

# Google Translate 1st Task - Uncomment to run:
# google_translate_task4('https://translate.google.com', 'בדיקה', '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea')

# YouTube Song Search Task - Uncomment to run:
# youtube_task5('https://youtube.com', 'Sound of Silence', 'search_query', 'search-icon-legacy')

# Google Translate 2nd Task - Uncomment to run:
# google_translate_task6('https://translate.google.com')

# Facebook Task - Uncomment to run:
# facebook_task7('https://facebook.com', 'username', 'password')

# Cookies delete task - Uncomment to run:
# deletecookies_task8('https://google.com')

# GitHub Search task - Uncomment to run:
# github_task9('https://github.com', 'Selenium')

# Disable extensions task - Uncomment to run:
# disable_all_extensions_task10('https://google.com')

# No extensions at all task - Ucomment to run:
# Incognito starts up with no extensions
# run_without_extensions_task11('https://google.com')