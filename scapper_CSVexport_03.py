import requests
from bs4 import BeautifulSoup
import datetime
import time
import csv
import sys

ID = 0
ID += 1

URL = 'https://www.amazon.es/proyector-port%C3%A1til-pel%C3%ADculas-reproducci%C3%B3n-Exteriores/dp/B07V29NTNX/ref=sr_1_2?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=WKFY0FGBWXPZ&dchild=1&keywords=anker+projector&qid=1617731740&sprefix=anker+projec%2Caps%2C169&sr=8-2'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}


# Get the seconds since epoch
def get_timestamp():
    t = time.localtime()
    return time.strftime('%Y-%m-%d %H:%M:%S', t)


# #create an ID for CSV
def get_id():
    return ID
    
#get price from Amazon 
def main():
    global price
    global converted_price
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text() 
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[2:7].replace(",", ""))

    print(title.strip())
    print(price)
    print(converted_price)
    print()

    if(converted_price > 499):
        print('Price has dropped! \nTimestamp: ')
        get_timestamp()
        send_to_csv()

    else:
        print('Price has not changed.   \nTimestamp: ')
        print(get_timestamp())
      
        

    print('--------------\n')

#Populate price and time to CSV file
def send_to_csv():
    filename = "Proyector_Anker_001"

    fields = ['id', 'price', 'timestamp',]
    rows = [[get_id(), price, get_timestamp()]]

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        # csvwriter.writerows(rows)
        for i in range(5):
            row = (
                i + 1,
                chr(ord('a') + i),
                '01/{:02d}/2019'.format(i + 1),)
            csvwriter.writerow(row)           

    print("Results has printed to CSV")

    #while loop
    while(True):
        main()
        time.sleep(30)


if __name__ == '__main__':
    main()
