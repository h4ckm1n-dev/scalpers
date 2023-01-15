import time
import requests
from bs4 import BeautifulSoup
import webbrowser

url = 'https://www.ldlc.com/fiche/PB00537387.html'

while True:
    page = requests.get(url)
    html = page.content
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.find(class_='price').text
    availability = soup.find(class_='stock').text
    if 'En stock' in availability:  # check if "En stock" appears in the availability text
        print(f'Price: {price}\tAvailability: {availability}')
        webbrowser.open_new_tab(url)  # Open the URL in the default web browser
    else:
        print(f'Price: {price}\tAvailability: {availability}', end='\r')
    time.sleep(60)  # wait for 60 seconds before repeating
