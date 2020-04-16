import time, configparser, csv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

config = configparser.ConfigParser()
config.read('config.ini')

LOGIN_URL = "https://www.linkedin.com/uas/login"

class BrowserNavigator:
    # ZOOMERS
    def zoom_out_browser(self):
        self.browser.execute_script("document.body.style.zoom = '65%'")

    def wait_and_zoom_out(self):
        time.sleep(1)
        self.zoom_out_browser()
        time.sleep(1)

    # HELPERS

    def export_users_to_csv(self):
        print("Exporting users list to csv")
        with open('users.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.users_list)

    def go_to_research_page_by_url(self):
        # Url copiato e incollato fa filtering su country Italy e basta
        people_url = 'https://www.linkedin.com/search/results/people/?facetGeoRegion=%5B%22it%3A0%22%5D&origin=FACETED_SEARCH'
        self.browser.get(people_url)
        self.wait_and_zoom_out()

    def find_element(self, css_selector):
        element = self.browser.find_element_by_class_name(css_selector)
        return element

    def try_find_element(self, css_selector):
        try:
            return self.find_element(css_selector)
        except NoSuchElementException:
            pass
    
    def wait_to_find_element_by_css(self, css_selector):
        sleep_time = self.SLEEP_TIME
        for attempts in range(self.MAX_LOADING_ATTEMPTS):
            print("Attempt n°" + str(attempts + 1) + ". Current page: " + self.browser.current_url + " element searched: " + css_selector)

            time.sleep(sleep_time)
            element = self.try_find_element(css_selector)
            if element is not None:
                time.sleep(sleep_time)
                return element
        
        raise NoSuchElementException("after ", sleep_time, " attempts the element is still not \ found.")

    def verify_all_page_is_loaded(self):
        print("Scrolling the page...")

        pre_scroll_page_height = self.browser.execute_script("return document.body.scrollHeight")
        self.scroll_page()
        after_scroll_page_height = self.browser.execute_script("return document.body.scrollHeight")

        # change the id of the element in order to looking for ending elements
        indicator_projects_still_loading = len(self.browser.find_elements_by_id('globalfooter-copyright'))

        if after_scroll_page_height == pre_scroll_page_height and indicator_projects_still_loading != 0:
            page_is_fully_loaded = True
        else:
            page_is_fully_loaded = False

        return page_is_fully_loaded

    def go_to_next_page_by_clicking(self):
        next_page_btn_cname = 'artdeco-pagination__button--next'
        next_page_btn = self.browser.find_element_by_class_name(next_page_btn_cname)
        # next_page_btn.click()
        self.browser.execute_script("arguments[0].click();", next_page_btn)

    # SCROLLERS

    def scroll_page(self):
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_element_height(self, elem):
        # Distanza da top pagina
        elem_scroll_height = elem.get_attribute("offsetTop")
        # Altezza elemento
        elem_offset_height = elem.get_attribute("offsetHeight")
        to_scroll = str(int(elem_scroll_height) + int(elem_offset_height) - (int(elem_offset_height) / 2) )
        print("scrolling to %s element height" % (to_scroll))
        self.browser.execute_script("window.scrollTo(0, %s);" % (to_scroll))

    def scroll_page_to_end(self):
        sleep_time = self.SLEEP_TIME

        page_is_fully_loaded = False
        while page_is_fully_loaded is False:
            page_is_fully_loaded = self.verify_all_page_is_loaded()
            time.sleep(sleep_time)

        print("Finished scrolling the page.")

    def scroll_to_pagination(self):
        next_page_btn_cname = 'artdeco-pagination__button--next'
        next_page_btn = self.browser.find_element_by_class_name(next_page_btn_cname)
        self.scroll_to_element_height(next_page_btn)
        self.wait_to_find_element_by_css(next_page_btn_cname)
    
    # MAIN
    def retreive_users_url(self):
        self.go_to_research_page_by_url()

        while True:
            if len(self.users_list) >= self.USERS_TO_SCRAPE:
                break
                
            self.scrape_result_page()
            self.scroll_page_to_end()
            self.scroll_to_pagination()
            self.go_to_next_page_by_clicking()

            time.sleep(2)
            
            if len(self.users_list) >= self.USERS_TO_SCRAPE:
                break

        self.export_users_to_csv()

    def scrape_result_page(self):
        self.wait_and_zoom_out()
        results_ul_cname = 'search-results__list'
    
        # aspetto trovi la lista di risultati
        self.wait_to_find_element_by_css(results_ul_cname)
        results_ul = self.browser.find_element_by_class_name(results_ul_cname)

        options = results_ul.find_elements_by_tag_name("li")
        search_info_cname = 'search-result__info'
        for option in options:
            # Scrollo all'altezza della singola persona
            self.scroll_to_element_height(option)
            # Aspetto che le informazioni vengano renderizzate
            self.wait_to_find_element_by_css(search_info_cname)
            
            search_info = option.find_element_by_class_name(search_info_cname)

            anchor_el = search_info.find_element_by_tag_name('a')
            url = anchor_el.get_property('href')
            print(url)

            name = search_info.find_element_by_class_name('actor-name')
            print(name.text)

            print('\n')
            
            self.users_list.append([name.text, url])

    def log_in(self):
        print('Logging in...')
        # Login
        username = config['LOGIN']['EMAIL']
        password = config['LOGIN']['PASSWORD']

        elementID = self.browser.find_element_by_id('username')
        elementID.send_keys(username)

        elementID = self.browser.find_element_by_id('password')
        elementID.send_keys(password)

        elementID.submit()

        while self.browser.current_url == LOGIN_URL:
            time.sleep(3)

        print("Logged")

    def __init__(self, browser):
        # App config
        self.SLEEP_TIME = int(config['CONFIG']['SLEEP_TIME'])
        self.USERS_TO_SCRAPE = int(config['CONFIG']['USERS_TO_SCRAPE'])
        self.MAX_LOADING_ATTEMPTS = int(config['CONFIG']['MAX_LOADING_ATTEMPTS'])
        self.browser = browser
        self.users_list = []

        browser.get(LOGIN_URL)

