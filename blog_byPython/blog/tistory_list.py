# -*- coding: euc-kr -*-
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
from time import sleep
import requests
import json
from bs4 import BeautifulSoup
print('test1')
def get_api_test(blog_id, token):
    url = 'https://www.tistory.com/apis/post/list'
    params = { 'access_token': token,
                'output' : 'json',
                'blogName' : blog_id,
                'page': 1
    }
    res = requests.get(url, params=params)
    print('test')
    if res.status_code == 200:
        res_json = res.json()
        print(res_json)
    else:
        res_json = res.json()
        print(res_json)
get_api_test('clud','accToken')