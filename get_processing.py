import requests

def pp_time(vid):
    headers = {
        'Ocp-Apim-Subscription-Key': '{Key}',
    }

    res = requests.post(url='https://videobreakdown.azure-api.net/Breakdowns/Api/Partner/Breakdowns/' + vid + '/State', headers=headers)
    print(res.json())