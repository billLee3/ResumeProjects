
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
#To change the city you are searching go to the zillow city you'd like to search, draw your boundary, copy url, and replace the url in requests.get line.
response = requests.get(url="https://www.zillow.com/homes/for_sale/?searchQueryState=%7B%22mapBounds%22%3A%7B%22west%22%3A-79.52935162207032%2C%22east%22%3A-78.7259763779297%2C%22south%22%3A37.16009286959997%2C%22north%22%3A37.61346516674548%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22price%22%3A%7B%22min%22%3A50000%2C%22max%22%3A150000%7D%2C%22mp%22%3A%7B%22min%22%3A162%2C%22max%22%3A485%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%2C%22pagination%22%3A%7B%7D%7D",
                        headers=header)

data = response.text
soup = BeautifulSoup(data, "html.parser")

all_links_elements = soup.select(".list-card-top a")

all_links = []

for link in all_links_elements:
    href = link["href"]
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)

print(all_links, f"\n Total of {len(all_links)} homes for sale in your selected city.")


