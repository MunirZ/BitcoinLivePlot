from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt

def get_price():
    request = requests.get('https://www.bitcoin.de/de')
    soup = BeautifulSoup(request.content, features='html.parser')
    price_string = soup.find('strong', id='ticker_price').text

    price = price_string.replace(".", "")
    price = price.replace(",", ".")
    price = price.replace("€", "")
    price = float(price.strip())
    return price

if __name__ == '__main__':
    plt.ion()
    prices = []

    for i in range(50):
        prices.append(get_price())
        plt.plot(prices)
        plt.draw()
        plt.pause(30)
        plt.clf()
        print(prices)

