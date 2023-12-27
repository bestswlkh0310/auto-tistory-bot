import requests
from util.config import tistoryKey, blogName
from datetime import datetime, timedelta

def post(title, html, published=datetime.now()):
    print('posting html...')

    data = {
    'access_token': tistoryKey,
    'blogName':blogName,
    'published': published,
    'title':title,
    'content':html,
    'visibility': 2,
    }

    response = requests.post('https://www.tistory.com/apis/post/write', data=data)

    print('posting success!!')

    return response.text
