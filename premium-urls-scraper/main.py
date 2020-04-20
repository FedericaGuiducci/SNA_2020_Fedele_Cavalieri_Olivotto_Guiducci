import time
from selenium import webdriver
from browser_navigator import BrowserNavigator

def main():
    # Browser Driver
    browser = webdriver.Chrome("./driver/chromedriver")

    page = BrowserNavigator(browser)
    page.log_in()
    page.wait_two_seconds()

    page.go_to_sales_navigator_people_search()
    page.wait_two_seconds()

    page.create_users_csv()
    page.retreive_users_url()

    page.save_screenshot("screenshot_closing.png")
    print("Closing browser...")
    browser.close()


if __name__ == '__main__':
    main()
