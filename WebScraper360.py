#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Set up the Selenium WebDriver (make sure to provide the path to your browser driver)
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

# Replace 'https://example.com' with the URL of the website you want to scrape
url = 'https://example.com'
driver.get(url)

# Let the page load (you may need to adjust the sleep duration based on the website)
time.sleep(2)

# Get the page source using BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Close the WebDriver since we have the page source
driver.quit()

# Extract data from the BeautifulSoup object (modify this based on the website structure)
article_titles = soup.find_all('h2', class_='article-title')

# Print the titles of the articles
for title in article_titles:
    print(title.text.strip())

