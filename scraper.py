from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time

# Setup Chrome Driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open Website
url = "https://quotes.toscrape.com/"
driver.get(url)

# Wait for page to load
time.sleep(3)

# Parse HTML
soup = BeautifulSoup(driver.page_source, "html.parser")

quotes = []
authors = []

# Extract Data
for item in soup.find_all("div", class_="quote"):
    quote = item.find("span", class_="text").text
    author = item.find("small", class_="author").text

    quotes.append(quote)
    authors.append(author)

# Create DataFrame
data = pd.DataFrame({
    "Quote": quotes,
    "Author": authors
})

# Save CSV
data.to_csv("data.csv", index=False)

print("Data Scraped Successfully!")

# Close Browser
driver.quit()