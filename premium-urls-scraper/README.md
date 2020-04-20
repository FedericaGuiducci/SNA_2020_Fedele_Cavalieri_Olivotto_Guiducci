# LinkedIn Free-account Users Url Scraper
Linkedin scraper per account free.
Permette di scaricare gli url di un tot di utenti settabile tramite il file config.ini

## Disclaimer
Scraping data off of LinkedIn is against their User Agreement. This is purely intended for educational purposes.

## Dependencies 
It is based on selenium 

## How to use
First, download the Chrome Driver from [here](http://chromedriver.chromium.org/) and extract it into the driver folder.

Set the number of users you want to scrape (2500 max) in the config.ini file.
Set your linkedin email and password in the config.ini file.

Finally, to scrape users run
```python3 main.py```

## N. employess filters
| Description       | KEY           |
| ----------------- | ------------- |
| 1 (Freelance)     | A             |
| 1 - 10            | B             |
| 11 - 50           | C             |
| 51 - 200          | D             |
| 201 - 500         | E             |
| 501 - 1000        | F             |
| 1001 - 5000       | G             |
| 5001 - 10000      | H             |
| more than 10000   | I             |

## Location geo filters
| Description   | KEY           |
| ------------- | ------------- |
| Italia        | 103350119     |
| Europa        | 100506914     |


