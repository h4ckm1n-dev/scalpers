import time
import requests
from bs4 import BeautifulSoup
import webbrowser

urls = ['https://www.amazon.fr/gp/product/B08HN5B8FJ', 'https://www.amazon.com/dp/B08PJQKZM3', 'https://www.amazon.com/dp/B08PJQKZM4']

while True:
    for url in urls:
        try:
            page = requests.get(url)
            html = page.content
            soup = BeautifulSoup(html, 'html.parser')
            title = soup.find(id='productTitle').text.strip()
            price = soup.find(id='priceblock_ourprice').text
            availability = soup.find(id='availability').text.strip()
            if 'In Stock' in availability:  # check if "In Stock" appears in the availability text
                print(f'Title: {title}\tPrice: {price}\tAvailability: {availability}')
                webbrowser.open_new_tab(url)  # Open the URL in the default web browser
            else:
                print(f'Title: {title}\tPrice: {price}\tAvailability: {availability}')
        except Exception as e:
            print(e)
            time.sleep(30)
    time.sleep(90)  # wait for 60 seconds before repeating