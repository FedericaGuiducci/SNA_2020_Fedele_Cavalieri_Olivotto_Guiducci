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
    time.sleep(2)

    page.go_to_sales_navigator_people_search()
    time.sleep(5)

    page.create_users_csv()
    page.retreive_users_url()

    print("Closing browser...")
    browser.close()


if __name__ == '__main__':
    main()
