from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
import time

load_dotenv()

def send_item(href, price, address):
    for a, b, c in zip(href,price,address):
        input_1 = driver.find_element(By.XPATH,
                                      '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        input_2 = driver.find_element(By.XPATH,
                                      '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        input_3 = driver.find_element(By.XPATH,
                                      '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

        input_1.send_keys(a)
        input_2.send_keys(b)
        input_3.send_keys(c)

        submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

        submit.click()
        time.sleep(1)

        driver.get(os.environ["GOOGLE_FORM"])
        time.sleep(1)


#BeautifulSoup
response = requests.get(os.environ["ZILLOW"])
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
tag = soup.select(".List-c11n-8-84-3-photo-cards")

href_tags = [href.find_all('a', href=True) for href in tag]
href = [a['href'] for item in href_tags for a in item if a.has_attr('href')]
href_list = href[1::2]

prices = [text.find_all("span", class_="PropertyCardWrapper__StyledPriceLine") for text in tag]
price_list = [money.getText().strip("+/mo").strip("+ 1bd") for item in prices for money in item]

addresses = [address.find_all("address") for address in tag]
address_list = [text.getText().strip().replace("|","") for item in addresses for text in item]

#Selenium
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get(os.environ["GOOGLE_FORM"])


send_item(href=href_list, price=price_list, address=address_list)
