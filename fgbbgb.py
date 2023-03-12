from bs4 import BeautifulSoup
import requests

coins = ["bitcoin", "ethereum", "cardano"]

for coin in coins:

    url = f"https://coinmarketcap.com/currencies/{coins}/markets/"


    response = requests.get(url)
    if response.status_code == 200:

        soup = BeautifulSoup(response.text, features="html.parser")
        soup_list = soup.find_all("a", {"href": url})
        res = soup_list[0].find("span")


        print(f"Price of {coin.capitalize()}: {res.text}")
    else:

        print(f"Error retrieving data for {coin.capitalize()}")
