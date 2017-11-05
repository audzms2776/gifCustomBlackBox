import requests
from pprint import pprint
import time


headers = {
    'Ocp-Apim-Subscription-Key': '{Key}',
}

data = {
    # Request parameters
    'name': 'hello' + str(time.time()),
    'privacy': 'Public'
}

files = {
    'file': open('test.avi', 'rb')
}
res = requests.post(url='https://videobreakdown.azure-api.net/Breakdowns/Api/Partner/Breakdowns?name=hellooo&privacy=Public', files=files, headers=headers)
pprint(res.json())

# return str(res.json())