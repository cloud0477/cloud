from time import sleep
import requests
import json
from bs4 import BeautifulSoup
print('test1')
def get_api_test(blog_id, token):
    url = 'https://www.tistory.com/apis/post/write'
    params = { 'access_token': token,
                'output' : 'json',
                'blogName' : blog_id,
                'title': 'test',
                'content': 'test123',
                'visibility': 3,
                'category': 0
    }
    res = requests.post(url, params=params)
    print('test')
    if res.status_code == 200:
        res_json = res.json()
        print(res_json)
    else:
        res_json = res.json()
        print(res_json)
get_api_test('cloud0477','accToken')