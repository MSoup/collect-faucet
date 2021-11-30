import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

"""
NOTES:
This script does 3 things:
1. Opens a browser instance and points to https://seleniumhq.github.io
2. Opens a new tab by finding a link that matches a specified text, then CTRL clicking a link. 
3. Opens a new window, focuses on it, then closes it. 
"""

# Constants

URL1 = "https://seleniumhq.github.io"
CLICK_ON_TEXT = "@shs96c" #Twitter handle of lead for Selenium

# These options makes python not complain about errors about random Chromium settings
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options)

try: 
    # Open URL
    driver.get("https://seleniumhq.github.io")
    driver.maximize_window()

    actions = ActionChains(driver)

    # Setup wait for later
    wait = WebDriverWait(driver, 10)

    # Store the ID of the original window
    original_window = driver.current_window_handle

    # Check we don't have other windows open already
    assert len(driver.window_handles) == 1

    # Click the link which opens in a new window
    webElement = driver.find_element(By.LINK_TEXT, CLICK_ON_TEXT)

    actions.move_to_element(webElement).key_down(Keys.LEFT_CONTROL).click(webElement).key_up(Keys.LEFT_CONTROL).perform()
    new_window = None

    # Wait for the new window or tab, otherwise selenium goes too fast
    wait.until(EC.number_of_windows_to_be(2))
    time.sleep(1)
    
    # Switch over to the new window then wait 2s
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            new_window = window_handle
            driver.switch_to.window(new_window)
            time.sleep(2)

    # Switch to original window
    driver.switch_to.window(original_window)
    time.sleep(2)


    # open a new browser window
    driver.switch_to.new_window("window")
    time.sleep(1)

    # resize it
    driver.set_window_size(1024, 768)

    # Loop through until we find the newly opened window (window_handle cant equal original or the second window)
    for window_handle in driver.window_handles:
        if window_handle != original_window and window_handle != new_window:
            driver.switch_to.window(window_handle)
            break

    time.sleep(1)
    # This only closes the currently active window, set by the above loop
    driver.close()

    time.sleep(1)
finally:
    driver.quit()