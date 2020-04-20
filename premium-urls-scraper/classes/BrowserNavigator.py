import time, configparser, csv
from selenium.common.exceptions import NoSuchElementException
from classes.Helpers import Helpers

config = configparser.ConfigParser()
config.read('config.ini')

LOGIN_URL = "https://www.linkedin.com/uas/login"

class BrowserNavigator:
    
    # ZOOMERS

    def zoom_out_browser(self):
        self.browser.execute_script("document.body.style.zoom = '70%'")

    def wait_and_zoom_out(self):
        self.wait_default_time()
        self.zoom_out_browser()
        self.wait_default_time()

    # NAVIGATORS

    def go_to_sales_navigator_people_search(self):
        print('Going to sales navigator home page')
        url_to_search = self.Helpers.elab_url_from_config()
        self.browser.get(url_to_search)
        self.Helpers.create_users_csv()
        self.wait_and_zoom_out()

    def go_to_next_page_by_clicking(self):
        nav_pag_cn = 'search-results__pagination'
        self.wait_to_find_element_by_class_name(nav_pag_cn)
        nav_pag = self.browser.find_element_by_class_name(nav_pag_cn)

        next_button_cn = 'search-results__pagination-next-button'
        next_button = nav_pag.find_element_by_class_name(next_button_cn)

        self.force_button_click(next_button)

    def go_to_next_page_by_url(self):
        current_url = self.browser.current_url

        delimiter = '&page=' 
        index = current_url.find(delimiter)

        if index == -1:
            self.go_to_next_page_by_clicking()
        else:
            first_part = current_url[:index]
            second_part = current_url[index:]

            page_number = ''

            # Escludo la prima &page= dal for
            sec_wo_e = second_part[6:]
            remaining_url = ''

            for i in range( len(sec_wo_e) ):
                print(sec_wo_e[i])
                if sec_wo_e[i] != '&':
                    page_number += sec_wo_e[i]
                else:
                    remaining_url += sec_wo_e[i:]
                    break
                    
            new_number = str(int(page_number) + 1)
            new_url = first_part + delimiter + new_number + remaining_url

            print('Moving to page ' + new_url)
            self.browser.get(new_url)

    # HELPERS

    def wait_two_seconds(self):
        time.sleep(2)

    def save_screenshot(self, fn):
        self.browser.save_screenshot(fn)

    def refresh_page(self):
        print('Refreshing page!')
        self.browser.refresh()
        self.wait_and_zoom_out()

    def force_button_click(self, btn):
        self.browser.execute_script("arguments[0].click();", btn)

    def find_element(self, class_name):
        element = self.browser.find_element_by_class_name(class_name)
        return element

    def try_find_element(self, class_name):
        try:
            return self.find_element(class_name)
        except NoSuchElementException:
            pass
    
    def wait_to_find_element_by_class_name(self, class_name):
        sleep_time = self.SLEEP_TIME
        for attempts in range(self.MAX_LOADING_ATTEMPTS):
            print("Attempt n°" + str(attempts + 1) + ". \nCurrent page: " + self.browser.current_url + " element searched: " + class_name)

            if attempts >= int(self.MAX_LOADING_ATTEMPTS) / 2:
                self.refresh_page()

            time.sleep(sleep_time)
            element = self.try_find_element(class_name)
            if element is not None:
                time.sleep(sleep_time)
                return element
        
        self.save_screenshot("screenshot_error.png")
        raise NoSuchElementException("after ", sleep_time, " attempts the element is still not \ found.")

    def verify_all_page_is_loaded(self):
        print("Scrolling the page...")

        pre_scroll_page_height = self.browser.execute_script("return document.body.scrollHeight")
        self.scroll_page()
        after_scroll_page_height = self.browser.execute_script("return document.body.scrollHeight")

        if after_scroll_page_height == pre_scroll_page_height:
            page_is_fully_loaded = True
        else:
            page_is_fully_loaded = False

        return page_is_fully_loaded

    def wait_default_time(self):
        time.sleep(self.SLEEP_TIME)
    
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
    
    # MAIN

    def fetch_users_url(self):
        while True:
            if len(self.users_list) >= self.USERS_TO_SCRAPE:
                break
                
            self.scrape_result_page()
            self.scroll_page_to_end()
            self.go_to_next_page_by_clicking()
            # self.go_to_next_page_by_url()

            self.wait_two_seconds()
            
            if len(self.users_list) >= self.USERS_TO_SCRAPE:
                break

    def scrape_result_page(self):
        self.wait_and_zoom_out()
        
        result_items_cname = 'search-results__result-item'
        
        self.wait_to_find_element_by_class_name(result_items_cname)
        results = self.browser.find_elements_by_class_name(result_items_cname)

        for li in results:
            self.scroll_to_element_height(li)
            
            search_info_cname = 'result-lockup__name'
            
            # Aspetto che le informazioni vengano renderizzate
            self.wait_to_find_element_by_class_name(search_info_cname)
            
            search_info = li.find_element_by_class_name(search_info_cname)
            
            anchor_el = search_info.find_element_by_tag_name('a')
            name = anchor_el.text
            url = anchor_el.get_property('href')

            # 2:-1 per rimuovere la b iniziale e gli apici iniziale e finale
            encoded_name = str(name.encode('utf8'))[2:-1]
            encoded_url = str(url.encode('utf8'))[2:-1]

            user_data = [encoded_name, encoded_url]
            print ('USER DATA: ' + str(user_data))
            
            self.users_list.append(user_data)
            self.Helpers.append_user_record_to_csv(user_data)

            print('\n')

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
        # Class attribute
        self.browser = browser
        self.users_list = []

        # App config
        self.SLEEP_TIME = int(config['CONFIG']['SLEEP_TIME'])
        self.USERS_TO_SCRAPE = int(config['CONFIG']['USERS_TO_SCRAPE'])
        self.MAX_LOADING_ATTEMPTS = int(config['CONFIG']['MAX_LOADING_ATTEMPTS'])

        # Classes
        self.Helpers = Helpers()

        browser.get(LOGIN_URL)
