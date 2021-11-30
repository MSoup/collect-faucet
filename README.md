# collect-faucet
om nom nom faucets are delicious

## Requirements:
ChromeDriver: https://chromedriver.chromium.org/downloads  
*IMPORTANT*  
Without some sort of web driver, this will not work. I have excluded ChromeDriver from the repository because every user has different versions of operating systems and web browsers, so you may download the wrong version by simply cloning this repository. Please fetch the right version for your browser. Don't know the right version? Find the version of your web browser, then go to the download link above and fetch the corresponding driver. 

**IMPORTANT2*  
If you're not using Chrome, then you may need to update bits and pieces of the scripts. The scripts have been created for me only, and since I only intend to use Selenium with Chrome, I have hardcoded the instance of the webdriver. Please look at the code and adjust accordingly to your use case.

## Usage:
1. Download the correct version of chromedriver.exe from above
2. Activate your virtual environment
3. Run chromedriver
4. Run test scripts

## Installation:
```
$ git clone git@github.com:MSoup/collect-faucet.git
$ cd <root directory>
$ source venv/scripts/activate
$ pip install -r requirements.txt
```

## References:
ChromeDriver is a separate executable that Selenium WebDriver uses to control Chrome. It is maintained by the Chromium team with help from WebDriver contributors. If you are unfamiliar with Selenium WebDriver, you should check out the Selenium site.

Follow these steps to setup your tests for running with ChromeDriver:

Ensure Chromium/Google Chrome is installed in a recognized location

ChromeDriver expects you to have Chrome installed in the default location for your platform.
Download the ChromeDriver binary for your platform under the downloads section of the above requirements link.

For further references, please see REFERENCE.md

## Changelog:
11/29: Project start
11/30: Learned mouse navigation, tab switching, opening and closing windows, searching for elements


# Project Timeline
Nov 29 - Dec 2: Learn Selenium  
Dec 3 - Dec 6: Make a script that uses Selenium  
Dec 7 - Dec 10: Refactor, test  
Dec 11 - Dec 14: Upload and run  
Dec 15 onwards: ??? profit  
