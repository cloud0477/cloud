import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

from time import sleep
import requests

api_key = ""
#--------------------------------------------------------------------------------------------------------
#이미지 업로드 함수 -> return URL
from bs4 import BeautifulSoup
def upload_test(url):
    #현재시간
    #파일이름, 저장경로
    fileName = 'name.pdf'
    filePath = 'C:/Users/user/Downloads'+fileName

    #티스토리 url 생성
    multipart_form_data = {
        'uploadedfile': (fileName, open(filePath, 'rb'))
    }
    response = requests.post('accToken', files=multipart_form_data)
    xml = response.content
    soup = BeautifulSoup(xml, 'xml')
    notices = soup.select('url')

    #return url
    return notices[0].get_text()
#--------------------------------------------------------------------------------------------------------
#pdf업로드방식 charPdf
import sys
def pdf_upload(name):
    #파일이름, 저장경로
    fileName = str(name) + '.pdf'
    filePath = 'C:/Users/user/Downloads/'+fileName

    files = [
        ('file', ('file', open(filePath, 'rb'), 'application/octet-stream'))
    ]
    headers = {
        'x-api-key': api_key
    }

    response = requests.post(
        'https://api.chatpdf.com/v1/sources/add-file', headers=headers, files=files)

    if response.status_code == 200:
        print('Source ID:', response.json()['sourceId'])
        return response.json()['sourceId']
    else:
        print('Status:', response.status_code)
        print('Error:', response.text)
        return False

#----------------------------------------------------------------------------------------------------
#pdf 채팅하기
import requests
def pdf_chat(source, content):
    headers = {
        "x-api-key": api_key,
        "Content-Type": "application/json",
    }

    data = {
        "stream": True,
        "sourceId": source,
        "messages": [
            {
                "role": "user",
                "content": content,
            },
        ],
    }


    url = "https://api.chatpdf.com/v1/chats/message"

    try:
        response = requests.post(url, json=data, headers=headers, stream=True)
        response.raise_for_status()

        if response.iter_content:
            max_chunk_size = 10240
            for chunk in response.iter_content(max_chunk_size):
                text = chunk.decode()
                print("Chunk:", text.strip())
        else:
            raise Exception("No data received")
    except requests.exceptions.RequestException as error:
        print("Error:", error)
#------------------------------------MAIN---------------------------------------------------------------
sourceId = pdf_upload('name')
if(sourceId == False):
    print("pdf 업로드에 실패하였습니다.")
    sys.exit()
else:
    content = "채팅내용"
    #content = """내용을 요약해줄수있어?"""
    pdf_chat(sourceId, content)
