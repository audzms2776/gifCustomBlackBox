import requests
from pprint import pprint
import sys

def get_break_data(vid):
    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': '42368468f63346bbbad78b947727918f',
    }
    url = 'https://videobreakdown.azure-api.net/Breakdowns/Api/Partner/Breakdowns/' + vid
    res = requests.get(url=url, headers=headers)
    result_json = res.json()

    create_time = result_json['createTime']
    video_id = result_json['id']
    breakdowns         = result_json['breakdowns'][0]
    thumbnail_url = breakdowns['thumbnailUrl']
    summarizedInsights = result_json['summarizedInsights']['annotations']

    pprint({
        'create_time': create_time,
        'video_id': video_id,
        'thumbnail_url': thumbnail_url
    })

    annotation_arr = []

    for summary in summarizedInsights:
        # pprint(summary)
        # print('annotation : ', summary['name'])
        start = summary['appearances'][0]['startSeconds']
        end = summary['appearances'][0]['endSeconds']
        # print('time : ', int(end - start))
        annotation_arr.append({
            'annotation': summary['name'],
            'time': int(end - start)
        })

    pprint(annotation_arr)

    return annotation_arr

v = sys.argv[2]
get_break_data(v)