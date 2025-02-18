# Import Dependencies
import os

from linkedin_scraper import actions
from linkedin_scraper import Company
from linkedin_scraper import Person

from selenium import webdriver
driver = webdriver.Chrome()

# Get username and password from local .env file.
email = os.getenv("LINKEDIN_EMAIL")
password = os.getenv("LINKEDIN_PASSWORD")


actions.login(driver, email, password)

person = Person('https://www.linkedin.com/in/david-m-reid/', driver = driver)
company = Company('https://www.linkedin.com/company/monadical/', driver = driver)
