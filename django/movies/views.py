# movies/views.py
import requests
from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(['GET'])
def box_office(request):
    print('dfdfdf')
    url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    params = {
        'key': '2083a37ad3c34c2ad3a8f96bbbaeba31',
        'targetDt': '20190102'  # 기본값으로 오늘 날짜를 설정합니다.
    }
    # response = requests.get(url)
    # request.GET.get('targetDt', '20230501')
    response = requests.get(url, params=params)
    print(response)
    data = response.json()
    return JsonResponse(data)
