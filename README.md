# gifCustomBlackBox

https://azure.microsoft.com/ko-kr/services/cognitive-services/video-indexer/
https://vi.microsoft.com/
https://docs.microsoft.com/en-us/azure/cognitive-services/video-indexer/video-indexer-use-apis
https://videobreakdown.portal.azure-api.net/docs/services/582074fb0dc56116504aed75/operations/5857caeb0dc5610f9ce979e4


* 동영상 촬영<br/>
python save_video.py

* 동영상 업로드 <br/>
python upload_video.py <br/>
=> 동영상 id

* 프로세스 진행 상황 확인 <br/>
curl -v -X GET "https://videobreakdown.azure-api.net/Breakdowns/Api/Partner/Breakdowns/{id}/State" -H "Ocp-Apim-Subscription-Key: {Key}"

* break 데이터 확인 <br/>
python get_break.py id
