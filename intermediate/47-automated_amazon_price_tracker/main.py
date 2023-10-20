import requests
import lxml
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import smtplib

load_dotenv(verbose=True)
USER_AGENT = os.environ['USER_AGENT']
ACCEPT_LANG = os.environ['ACCEPT_LANGUAGE']

headers = {
    'User-Agent': USER_AGENT,
    'Accept-Language': ACCEPT_LANG,
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
}

product_url = 'https://www.amazon.com/Nike-Romaleos-Training-White-Black/dp/B01FZ3H4TQ/ref=sr_1_13?crid=RWB8BXT454CN&keywords=adidas%2Bpowerlift%2Bshoes&qid=1697802294&sprefix=adidas%2Bpowerlift%2Bshoe%2Caps%2C186&sr=8-13&th=1&psc=1'
second_product_url = 'https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6'
response = requests.get(url=product_url, headers=headers)

webpage_text = response.text
soup = BeautifulSoup(webpage_text, 'lxml')

price = soup.find(name='span', class_='a-price-whole').getText()
price_fraction = soup.find(name='span', class_='a-price-fraction').getText()
product_name = soup.find(name='span', id='productTitle').getText()

whole_price = float(price + price_fraction)
desired_price = 200


mail = os.environ['MAIL_SENDER']
password = os.environ['MAIL_PASS']

if whole_price <= desired_price:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=mail, password=password)
        connection.sendmail(
            from_addr=mail,
            to_addrs=mail,
            msg=f"Subject:Amazon Price Alert\n\nDesired product {product_name} is on daily deal of ${whole_price}.\nLink to the product {product_url}"
        )