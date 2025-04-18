import smtplib
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By


load_dotenv()

header = {
    "Accept-Language": "en-US,en;q=0.9,fil;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get("https://www.lazada.com.ph/products/windproof-travel-uv-umbrella-for-rain-compact-folding-umbrella-sun-protection-tote-umbrella-i3615305749-s23561763330.html?pvid=92ea3887-3c86-46fd-a011-ded8b477d610&search=jfy&scm=1007.45039.397834.0&priceCompare=skuId%3A23561763330%3Bsource%3Atpp-recommend-plugin-32104%3Bsn%3A92ea3887-3c86-46fd-a011-ded8b477d610%3BoriginPrice%3A7900%3BdisplayPrice%3A7900%3BsinglePromotionId%3A-1%3BsingleToolCode%3AmockedSalePrice%3BvoucherPricePlugin%3A0%3Btimestamp%3A1741771433769&spm=a2o4l.homepage.just4u.d_3615305749")

price = driver.find_element(By.XPATH,'//*[@id="module_product_price_1"]/div/div/span').text.split("₱")[1]
current_price = float(price)
print(current_price)

def send_mail():
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls() #Makes the connection secure
        connection.login(user=os.environ["EMAIL"], password=os.environ["PASSWORD"])
        connection.sendmail(from_addr=os.environ["EMAIL"],
                            to_addrs="jeongyoo03@gmail.com",
                            msg=f"The current price of the item is {current_price}")

driver.quit()

if current_price <= 100:
    send_mail()
