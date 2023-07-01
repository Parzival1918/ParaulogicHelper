#Functions to scrap paraulogic

#Import libraries to scrap https://www.vilaweb.cat/paraulogic/
import requests
from bs4 import BeautifulSoup
import json
import time

#Cosntants
URL = 'https://www.vilaweb.cat/paraulogic/'
URL_DATE = 'https://www.vilaweb.cat/paraulogic/?data=' #Date in format YYYY-MM-DD

#Function to obtain the words of a paraulogic game
def get_raw_json(url: str = URL):
    #Get the words
    page = requests.get(url)
        
    soup = BeautifulSoup(page.content, 'html.parser')
    rawScript = soup.find_all('script')[3] #This is specific for this page

    #extract the content of var t = {...} and convert it to a dictionary
    #THIS CODE SHOULD BE IMPORVED
    rawJSON = rawScript.contents[0].split('var t=')[1].split(';')[:8]
    rawJSON = ''.join(rawJSON)

    return json.loads(rawJSON)