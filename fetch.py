import requests

def loadKey():
    with open('key','r') as f:
        return f.read()

def fetchPrice(priceIdentifier):
    key = loadKey()
    url = "https://api.cryptowat.ch/markets/kraken/" + priceIdentifier + '/price?apikey=' + key

    response = requests.get(url)
    return response.json()['result']['price']