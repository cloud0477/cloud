import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyautogui
from requests_toolbelt.multipart.encoder import MultipartEncoder
import requests

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options = option)

driver.get('https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EB%A5%98%ED%98%84%EC%A7%84%20%EC%8B%9C%EC%A6%8C%202%ED%8C%A8')
time.sleep(3)
url = pyautogui.screenshot('D:/test.png', region=(59, 392, 650, 400))

def upload_test():
    multipart_form_data = {
        'uploadedfile': ('test.png', open('D:\\test.png', 'rb'))
    }

    response = requests.post('https://www.tistory.com/apis/post/attach?access_token=09450665991d67124a544925f1256910_8b4aa229ee099becfefe751485cbcfc2&blogName=clud', files=multipart_form_data)

    xml = response.content
    soup = BeautifulSoup(xml, 'xml')
    notices = soup.select('url')
    print(response.content)
    print(notices[0].get_text())
    return notices[0].get_text()
upload_test()