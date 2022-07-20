import requests, json
from pprint import pprint

def loadKey():
    with open('key','r') as f:
        return f.read().strip()

def loadConfig():
    with open('config.json','r') as f:
        return json.load(f)

def fetchPrice(priceIdentifier):
    key = loadKey()
    url = "https://api.cryptowat.ch/markets/kraken/" + priceIdentifier + '/price?apikey=' + key

    response = requests.get(url)
    return response.json()['result']['price']

def main():
    config = loadConfig()

    fetchedPrices = {}

    for priceIdentifier in config['priceIdentifiers']:
        fetchedPrices[priceIdentifier] = fetchPrice(priceIdentifier)
    
    print(json.dumps(fetchedPrices))

main()