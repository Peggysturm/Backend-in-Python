import requests
from bs4 import BeautifulSoup
import sqlite3

def parser(url:str):
    base_url="https://smauro.ru"
    response = requests.get(url=url)
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    products = soup.find_all("div", class_="item")
    
    urls = []
    for product in products:
        name_elem = product.find("div", itemprop = "name")
        link = name_elem.findNext().get("href")
        urls.append(base_url+link)
    
    args = []
    for url in urls:
        response = requests.get(url=url)
        html = response.text
        soup = BeautifulSoup(html, "lxml")
        name = soup.select_one("h1").text
        price = soup.select_one("span.item_current_price").text
        description =  soup.select_one("div.item_text").text
        args.append((name, price, description))

    conn = sqlite3.connect('mydata.db')
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO plumbing VALUES (?,?,?)", args)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    parser(url="https://smauro.ru/catalog/bytovaya_santekhnika/")

