import requests

def pp_time(vid):
    headers = {
        'Ocp-Apim-Subscription-Key': '42368468f63346bbbad78b947727918f',
    }

    res = requests.post(url='https://videobreakdown.azure-api.net/Breakdowns/Api/Partner/Breakdowns/' + vid + '/State', headers=headers)
    print(res.json())