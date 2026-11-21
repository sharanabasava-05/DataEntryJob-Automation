import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://docs.google.com/forms/d/e/1FAIpQLScwPT4plaRqlJvSNZr-N4Iq492aV_aVlIhhGyzWYAl-ocQ7xQ/viewform"


response = requests.get("https://appbrewery.github.io/Zillow-Clone/")

soup = BeautifulSoup(response.text, 'html.parser')
# get the address
list_address = soup.select(selector='.StyledPropertyCardDataWrapper address')
list_addresses = [address.get_text().replace(" | ", " ").strip() for address in list_address]
# print(list_addresses)

# get the list of price
list_price = soup.find_all('span',class_="PropertyCardWrapper__StyledPriceLine")
list_price = [price.get_text().replace("/mo","").split("+")[0] for price in list_price]
# print(list_price)

#list of links
list_links = soup.select(selector='.StyledPropertyCardDataWrapper a')
list_links = [links.attrs['href'] for links in list_links]
# print(list_links)

# -------using selinum to automate ------
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

for i in range(len(list_addresses)):

    driver.get(URL)
    time.sleep(2)
    address = driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")

    price = driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")

    link = driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")

    address.send_keys(list_addresses[i])
    price.send_keys(list_price[i])
    link.send_keys(list_links[i])

    subbit_button = driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span/span")
    subbit_button.click()



