import time, configparser, csv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from browser_navigator import BrowserNavigator

def main():
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Browser Driver
    browser = webdriver.Chrome("./driver/chromedriver")

    page = BrowserNavigator(browser)
    page.log_in()

    page.retreive_users_url()

    print("Closing browser...")
    browser.close()



if __name__ == '__main__':
    main()
