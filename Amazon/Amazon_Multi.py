import time
import requests
from bs4 import BeautifulSoup
import webbrowser

urls = ['https://www.ldlc.com/fiche/PB00537387.html', 'https://www.ldlc.com/fiche/PB00537456.html', 'https://www.ldlc.com/fiche/PB00537960.html']

while True:
    for url in urls:
        try:
            page = requests.get(url)
            html = page.content
            soup = BeautifulSoup(html, 'html.parser')
            price = soup.find(class_='price').text
            availability = soup.find(class_='stock').text
            if 'En stock' in availability:  # check if "En stock" appears in the availability text
                print(f'Price: {price}\tAvailability: {availability}')
                webbrowser.open_new_tab(url)  # Open the URL in the default web browser
            else:
                print(f'Price: {price}\tAvailability: {availability}')
        except ConnectionError as e:
            if "Connection reset by peer" in str(e):
                print("Connection reset by peer, waiting for 30 seconds")
                time.sleep(30)
            else:
                raise e
    time.sleep(60)  # wait for 60 seconds before repeating