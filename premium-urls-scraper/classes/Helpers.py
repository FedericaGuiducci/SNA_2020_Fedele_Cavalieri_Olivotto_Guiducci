import configparser, csv
from datetime import datetime

config = configparser.ConfigParser()
config.read('config.ini')

# URL CONFIG
PEOPLE_BASE_URL = 'https://www.linkedin.com/sales/search/people?'
MULTI_FILTER_CONJ = '%2C'
GEO_FILTER_QUERY_PARAM = 'geoIncluded'
COMPANY_SIZE_FILTER_QUERY_PARAM = 'companySize'
INDUSTRIES_INCLUDED_FILTER_QUERY_PARAM = 'industryIncluded'

# CSV
CSV_BASE_PATH = 'export/'

class Helpers:
    # CREATE URL FROM CONFIG

    def elab_url_from_config(self):
        geo_filter_length = len(self.FILTER_LOCATION)
        nemployees_filter_length = len(self.FILTER_NEMPLOYEES)
        industries_filter_length = len(self.FILTER_INDRUSTRIES)

        url_to_search = ''
        first_filter_added = 0

        # GEO FILTER
        if geo_filter_length != 0 and self.FILTER_LOCATION[0] != '':
            first_filter_added = 1
            url_to_search = PEOPLE_BASE_URL + GEO_FILTER_QUERY_PARAM + '='

            if geo_filter_length == 1:
                url_to_search += self.FILTER_LOCATION[0]
            else:
                for i, geo_key in enumerate(self.FILTER_LOCATION):
                    geo_key = geo_key.replace(" ", "")

                    url_to_search += geo_key

                    if i+1 != len(self.FILTER_LOCATION):
                        url_to_search += MULTI_FILTER_CONJ

        # N. EMPLOYEES FILTER
        if nemployees_filter_length != 0 and self.FILTER_NEMPLOYEES[0] != '':
            if first_filter_added == 0:
                first_filter_added = 1
                url_to_search = PEOPLE_BASE_URL + COMPANY_SIZE_FILTER_QUERY_PARAM + '='
            else:
                url_to_search += '&' + COMPANY_SIZE_FILTER_QUERY_PARAM + '='


            if nemployees_filter_length == 1:
                url_to_search += self.FILTER_NEMPLOYEES[0]
            else:
                for i, nemmp_key in enumerate(self.FILTER_NEMPLOYEES):
                    nemmp_key = nemmp_key.replace(" ", "")

                    url_to_search += nemmp_key

                    if i+1 != len(self.FILTER_NEMPLOYEES):
                        url_to_search += MULTI_FILTER_CONJ

        # INDUSTRIES FILTER
        if industries_filter_length != 0 and self.FILTER_INDRUSTRIES[0] != '':
            if first_filter_added == 0:
                first_filter_added = 1
                url_to_search = PEOPLE_BASE_URL + INDUSTRIES_INCLUDED_FILTER_QUERY_PARAM + '='
            else:
                url_to_search += '&' + INDUSTRIES_INCLUDED_FILTER_QUERY_PARAM + '='

            if industries_filter_length == 1:
                url_to_search += self.FILTER_INDRUSTRIES[0]
            else:
                for i, industry_key in enumerate(self.FILTER_INDRUSTRIES):
                    industry_key = industry_key.replace(" ", "")

                    url_to_search += industry_key

                    if i+1 != len(self.FILTER_INDRUSTRIES):
                        url_to_search += MULTI_FILTER_CONJ

        return url_to_search

    # CSV HANDLERS

    def create_users_csv(self):
        print('Creating users csv')
        with open(self.FILE_NAME, 'w', newline='') as file:
            writer = csv.writer(file)
            header = ['Name', 'Url']
            writer.writerow(header)

    def append_user_record_to_csv(self, user):
        print("Appending user to csv")
        with open(self.FILE_NAME, "a") as file:
            # Append 'hello' at the end of file
            writer = csv.writer(file)
            writer.writerow(user)

    def __init__(self):
        print('Initializing Helpers class')
        
        # FILTERS
        self.FILTER_LOCATION = config['FILTERS']['LOCATION'].split(',')
        self.FILTER_NEMPLOYEES = config['FILTERS']['NEMPLOYEES'].split(',')
        self.FILTER_INDRUSTRIES = config['FILTERS']['INDUSTRIES'].split(',')

        # CSV
        self.FILE_NAME = CSV_BASE_PATH + str(datetime.now()) + '.csv'
