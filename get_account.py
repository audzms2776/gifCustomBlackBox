import requests

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '42368468f63346bbbad78b947727918f'
}

res = requests.get(url='https://videobreakdown.azure-api.net/Breakdowns/Api/Partner/Accounts', headers=headers)
print(res.json())
