# LinkedIn Scraper

## Disclaimer
Scraping data off of LinkedIn is against their User Agreement. This is purely intended for educational purposes.

## Dependencies 
It is based on selenium 

## How to use
First, download the Chrome Driver from [here](http://chromedriver.chromium.org/) and extract it into the driver folder.

Set the number of users you want to scrape in the config.ini file.

Finally, to scrape users run
```python3 main.py```



<!-- Create a python3 virtual environment following [this](https://docs.python.org/3/tutorial/venv.html).
Within the virtual environment
```pip install -r requirements.txt```

Edit the `conf.json` config file accordingly specifying the chrome bin path, e.g. by typying 
```which google-chrome``` in a UNIX shell command line, the chrome driver path, the desired queries
and so forth. 

Finally, to scrape users run 
```python scrape_users.py --conf conf.json```
or jobs
```python scrape_jobs.py --conf conf.json``` -->