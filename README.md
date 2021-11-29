# collect-faucet
om nom nom faucets are delicious

## Usage:
No idea. Empty repository for now 

## Dev Usage:
```
$ git clone git@github.com:MSoup/collect-faucet.git
$ cd <root directory>
$ source venv/scripts/activate
$ pip install -r requirements.txt
$ I don't know because I didn't actually do any of the above yet.
```

## References:
ChromeDriver is a separate executable that Selenium WebDriver uses to control Chrome. It is maintained by the Chromium team with help from WebDriver contributors. If you are unfamiliar with Selenium WebDriver, you should check out the Selenium site.

Follow these steps to setup your tests for running with ChromeDriver:

Ensure Chromium/Google Chrome is installed in a recognized location

ChromeDriver expects you to have Chrome installed in the default location for your platform. You can also force ChromeDriver to use a custom location by setting a special capability.

Download the ChromeDriver binary for your platform under the downloads section of this site

Help WebDriver find the downloaded ChromeDriver executable

Any of these steps should do the trick:

include the ChromeDriver location in your PATH environment variable

(Python only) include the path to ChromeDriver when instantiating webdriver.Chrome (see sample below)


```
import time

from selenium import webdriver



driver = webdriver.Chrome('/path/to/chromedriver')  # Optional argument, if not specified will search path.

driver.get('http://www.google.com/');

time.sleep(5) # Let the user actually see something!

search_box = driver.find_element_by_name('q')

search_box.send_keys('ChromeDriver')

search_box.submit()

time.sleep(5) # Let the user actually see something!

driver.quit()
```
## Changelog:
11/29: Project start



# Project Timeline
Nov 29 - Dec 2: Learn Selenium  
Dec 3 - Dec 6: Make a script that uses Selenium  
Dec 7 - Dec 10: Refactor, test  
Dec 11 - Dec 14: Upload and run  
Dec 15 onwards: ??? profit  
