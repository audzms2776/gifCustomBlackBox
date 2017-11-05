import requests

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '{Key}'
}

res = requests.get(url='https://videobreakdown.azure-api.net/Breakdowns/Api/Partner/Accounts', headers=headers)
print(res.json())
