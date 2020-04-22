import configparser, csv
from datetime import datetime
from classes.Filter import Filter

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

    # CONFIG MANAGER

    def elab_multi_configurations(self):
        url_list = []

        for s in config.sections():
            if not s.startswith('FILTERCONFIG:'):
                continue

            FILTER_LOCATION = config[s]['LOCATION'].split(',')
            FILTER_NEMPLOYEES = config[s]['NEMPLOYEES'].split(',')
            FILTER_INDRUSTRIES = config[s]['INDUSTRIES'].split(',')
            search_url = self.elab_url_from_config(FILTER_LOCATION, FILTER_NEMPLOYEES,FILTER_INDRUSTRIES)

            url_list.append(Filter(FILTER_LOCATION, FILTER_NEMPLOYEES, FILTER_INDRUSTRIES, search_url))

        return url_list

    def elab_url_from_config(self, FILTER_LOCATION, FILTER_NEMPLOYEES, FILTER_INDRUSTRIES):
        geo_filter_length = len(FILTER_LOCATION)
        nemployees_filter_length = len(FILTER_NEMPLOYEES)
        industries_filter_length = len(FILTER_INDRUSTRIES)

        url_to_search = ''
        first_filter_added = 0

        # GEO FILTER
        if geo_filter_length != 0 and FILTER_LOCATION[0] != '':
            first_filter_added = 1
            url_to_search = PEOPLE_BASE_URL + GEO_FILTER_QUERY_PARAM + '='

            if geo_filter_length == 1:
                url_to_search += FILTER_LOCATION[0]
            else:
                for i, geo_key in enumerate(FILTER_LOCATION):
                    geo_key = geo_key.replace(" ", "")

                    url_to_search += geo_key

                    if i+1 != len(FILTER_LOCATION):
                        url_to_search += MULTI_FILTER_CONJ

        # N. EMPLOYEES FILTER
        if nemployees_filter_length != 0 and FILTER_NEMPLOYEES[0] != '':
            if first_filter_added == 0:
                first_filter_added = 1
                url_to_search = PEOPLE_BASE_URL + COMPANY_SIZE_FILTER_QUERY_PARAM + '='
            else:
                url_to_search += '&' + COMPANY_SIZE_FILTER_QUERY_PARAM + '='


            if nemployees_filter_length == 1:
                url_to_search += FILTER_NEMPLOYEES[0]
            else:
                for i, nemmp_key in enumerate(FILTER_NEMPLOYEES):
                    nemmp_key = nemmp_key.replace(" ", "")

                    url_to_search += nemmp_key

                    if i+1 != len(FILTER_NEMPLOYEES):
                        url_to_search += MULTI_FILTER_CONJ

        # INDUSTRIES FILTER
        if industries_filter_length != 0 and FILTER_INDRUSTRIES[0] != '':
            if first_filter_added == 0:
                first_filter_added = 1
                url_to_search = PEOPLE_BASE_URL + INDUSTRIES_INCLUDED_FILTER_QUERY_PARAM + '='
            else:
                url_to_search += '&' + INDUSTRIES_INCLUDED_FILTER_QUERY_PARAM + '='

            if industries_filter_length == 1:
                url_to_search += FILTER_INDRUSTRIES[0]
            else:
                for i, industry_key in enumerate(FILTER_INDRUSTRIES):
                    industry_key = industry_key.replace(" ", "")

                    url_to_search += industry_key

                    if i+1 != len(FILTER_INDRUSTRIES):
                        url_to_search += MULTI_FILTER_CONJ

        return url_to_search

    # CSV HANDLERS

    def create_users_csv(self):
        print('Creating users csv')
        with open(self.FILE_NAME, 'w', newline='') as file:
            writer = csv.writer(file)
            header = ['Name', 'Url', 'LocationFilter', 'nEmployeesFilter', 'IndustriesFilter']
            writer.writerow(header)

    def append_user_record_to_csv(self, user):
        print("Appending user to csv")
        with open(self.FILE_NAME, "a") as file:
            writer = csv.writer(file)
            writer.writerow(user)

    def __init__(self):
        print('Initializing Helpers class')

        # CSV
        self.FILE_NAME = CSV_BASE_PATH + str(datetime.now()) + '.csv'
