# -*- coding: euc-kr -*-
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyautogui
from requests_toolbelt.multipart.encoder import MultipartEncoder
import requests
import datetime as dt
import random
import json
import sys

#글쓰기 content
headCt = """
<p id="top" data-ke-size="size16">&nbsp;</p>
<h2 data-ke-size="size26"><b>{{title}}</b></h2>
<table style="border-collapse: collapse; width: 100%; height: 95px;" border="1" data-ke-align="alignLeft" data-ke-style="style4">
<tbody>
<tr style="height: 19px;">
<td style="width: 50%; height: 19px;">1위. <span style="color: #006dd7;"><b><a style="color: #006dd7;" href="#tag1">{{no1}}</a></b></span></td>
<td style="width: 50%; height: 19px;">6위. <span style="color: #006dd7;"><b><a style="color: #006dd7;" href="#tag6">{{no6}}</a></b></span></td>
</tr>
<tr style="height: 19px;">
<td style="width: 50%; height: 19px;">2위. <span style="color: #006dd7;"><b><a style="color: #006dd7;" href="#tag2">{{no2}}</a></b></span></td>
<td style="width: 50%; height: 19px;">7위. <span style="color: #006dd7;"><b><a style="color: #006dd7;" href="#tag7">{{no7}}</a></b></span></td>
</tr>
<tr style="height: 19px;">
<td style="width: 50%; height: 19px;">3위. <span style="color: #006dd7;"><b><a style="color: #006dd7;" href="#tag3">{{no3}}</a></b></span></td>
<td style="width: 50%; height: 19px;">8위. <span style="color: #006dd7;"><b><a style="color: #006dd7;" href="#tag8">{{no8}}</a></b></span></td>
</tr>
<tr style="height: 19px;">
<td style="width: 50%; height: 19px;">4위. <span style="color: #006dd7;"><b><a style="color: #006dd7;" href="#tag4">{{no4}}</a></b></span></td>
<td style="width: 50%; height: 19px;">9위. <span style="color: #006dd7;"><b><a style="color: #006dd7;" href="#tag9">{{no9}}</a></b></span></td>
</tr>
<tr style="height: 19px;">
<td style="width: 50%; height: 19px;">5위. <span style="color: #006dd7;"><b><a style="color: #006dd7;" href="#tag5">{{no5}}</a></b></span></td>
<td style="width: 50%; height: 19px;">10위.<span style="color: #006dd7;"><b><a style="color: #006dd7;" href="#tag10">{{no10}}</a></b></span></td>
</tr>
</tbody>
</table>
<p style="text-align: center;" data-ke-size="size14">(클릭시 해당 타이틀로 이동)</p>
<hr id="tag1" contenteditable="false" data-ke-type="horizontalRule" data-ke-style="style3" />
"""
baseCt = """
<h2 class="newH2" style="color: #000000; text-align: center;" data-ke-size="size26">{{content}}</h2>
<p style="text-align: center;" data-ke-size="size16"><img style="display: block;" src="{{imgUrl}}" alt="" width="1065" height="632" /></p>
<p data-ke-size="size16">&nbsp;</p>
<p data-ke-size="size16"><p style="text-align: center;" data-ke-size="size16">
<a style="background-color: #e6f5ff; color: #0070d1; text-align: center;" href="{{url}}">
<span style="color: #006dd7;">출처(네이버 - 클릭시 뉴스기사 이동)</span></a></p><p style="text-align: right;" data-ke-size="size16">
<a style="text-align: right;" href="#top" data-ke-size="size16">최상위로 이동</a></p>
<hr id="{{tag}}" contenteditable="false" data-ke-type="horizontalRule" data-ke-style="style5" />
"""
blog_id = ''
token = ''

#크롬 연결
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options = option)

#오늘 날짜
date = dt.datetime.now()

#이미지 업로드 함수 -> return URL
def upload_test(url):
    #현재시간
    now = date.strftime("%Y-%m-%d %H:%M:%S")

    #파일이름, 저장경로
    fileName = date.strftime("%Y-%m-%d_%H%M%S") + '.png'
    filePath = 'E:/dev/blog/img/'+fileName

    #스크린샷
    driver.get(url)
    time.sleep(1)
    driver.implicitly_wait(3)
    url = pyautogui.screenshot(filePath, region=(59, 392, 650, 400))
    
    #티스토리 url 생성
    multipart_form_data = {
        'uploadedfile': (fileName, open(filePath, 'rb'))
    }
    response = requests.post('acctoken', files=multipart_form_data)
    xml = response.content
    soup = BeautifulSoup(xml, 'xml')
    notices = soup.select('url')

    #return url
    return notices[0].get_text()

#랜덤 태그 붙이기
def random_tag():
    #200개
    arr = ["엔터테인먼트", "뉴스", "스포츠", "음악", "영화", "텔레비전", "게임", "유명인사", "건강", "패션", "뷰티", "요리", "여행", "기술", "자동차", "과학", "환경", "정치", "경제", "코로나19", "피트니스", "독서", "만화", "애완동물", "사회", "교육", "블로그", "소셜미디어", "쇼핑", "페스티벌", "예술", "연예인", "식품", "야외활동", "취미", "스타트업", "스마트폰", "트렌드", "역사", "문화", "인터넷", "과학기술", "음식", "운동", "여성", "남성", "가족", "친구", "컴퓨터", "프로그래밍", "디자인", "코딩", "비즈니스", "투자", "주식", "부동산", "금융", "자금", "부모", "아이", "육아", "결혼", "연애", "이별", "건축", "인테리어", "가구", "요가", "명상", "사진", "카메라", "모바일앱", "자기계발", "공부", "어학", "영어", "일본어", "중국어", "외국어", "여행지", "호텔", "항공", "바다", "산", "호수", "자연", "동물", "생물학", "물리학", "화학", "수학", "심리학", "사회학", "국제정치", "연예계", "배우", "가수", "스포츠선수", "올림픽", "월드컵", "테크놀로지", "스마트홈", "로봇", "모바일게임", "스포츠영화", "호러영화", "코미디", "드라마", "로맨스", "범죄", "환경보호", "재활용", "기후변화", "정치인", "선거", "정책", "경제학", "금융시장", "투자전략", "예술가", "전시회", "미술", "문학", "문학작품", "사용자경험", "소프트웨어", "앱개발", "IT보안", "인공지능", "빅데이터", "로봇공학", "우주", "우주탐사", "로켓", "천체관측", "신기술", "인터넷오브락", "가상현실", "3D프린팅", "음악페스티벌", "컨서트", "음악가", "음악밴드", "힙합", "팝뮤직", "록뮤직", "클래식음악", "재즈", "블루스", "컨트리음악", "레게", "펑크록", "메탈", "전자음악", "발라드", "댄스음악", "컨템포러리댄스", "발레", "힙합댄스", "노래", "음악프로듀서", "음악비디오", "MTV", "그래미어워드", "오스카상", "종합격투기", "농구", "야구", "축구", "테니스", "골프", "수영", "스키", "스케이트보드", "사이클링", "레이싱", "육상", "체조", "무용", "탁구", "볼링", "롤러스케이트", "얼라이언스", "게임컨솔", "모바일게임", "온라인게임", "카드게임", "보드게임", "비디오게임", "게임개발", "게임캐릭터", "게임커뮤니티", "게임대회", "유명게임", "모델", "배우모델", "패션모델", "아름다움", "메이크업", "피부관리", "헤어스타일", "헤어컬러", "미용실", "스킨케어", "스파", "마사지", "에스테틱", "요가스튜디오", "요가매트", "피트니스클럽", "운동화", "운동복", "다이어트", "건강식품", "식단", "요리책", "요리조리", "디저트", "피자", "스시", "커피", "와인"]

    tag = """인기검색어, 트렌드, 최신뉴스, 뉴스, 인터넷트렌드, 소셜미디어, 인스타그램, 페이스북, 트위터, 유튜브, 틱톡, 영화, TV쇼, 음악, 연예뉴스, 스포츠, 게임, 과학, 건강, 여행, 패션, 경제, 요리, 운동, 다이어트, 비즈니스, 경제, 주식, 부동산, 투자, """
    r_no = random.sample(range(0,200),50)
    for i in r_no:
        if( i != len(r_no) - 1):
            tag = tag + arr[i] + ', '
        else:
            tag = tag + arr[i]
    return tag

#현재시간 중복 게시물 확인
def check_api_post():
    print('#check_api_post')
    result = False
    url = 'https://www.tistory.com/apis/post/list'
    params = { 'access_token': 'accToken',
                'output' : 'json',
                'blogName' : 'clud',
                'page': 1
    }
    res = requests.get(url, params=params)
    if res.status_code == 200:
        res_json = res.json()
        t1 = json.dumps(res_json)
        jsonObject = json.loads(t1)
        post_title = jsonObject.get("tistory").get("item").get("posts")
        for k in post_title:
            t2 = json.dumps(k)
            tempObject = json.loads(t2)
            categoryId = tempObject.get("categoryId")

            #인기검색어 카테고리ID 체크
            #IF문일때 딱 한번실행(최근값)
            if(categoryId == '1051139'): 
                ti = str(tempObject.get("title"))
                tempHour = ti[11:13]
                hour = date.strftime("%H")
                if(tempHour == hour):
                    result = True
                break
    else:
        res_json = res.json()
        print(res_json)
    return result

#실제 글쓰기
def get_api_test(title, content):
    print('#get_api_test')
    url = 'https://www.tistory.com/apis/post/write'
    data = { 'access_token': token,
                'output' : 'json',
                'blogName' : blog_id,
                'title': title,
                'content': content,
                'tag': random_tag(),
                'visibility': 3, #비공개 - 0, 보호 - 1, 공개 -3
                'category': 1051139, #인기검색어 - 1051139
                'acceptComment': 1, #댓글 비허용 - 0, 허용 -1
    }
    res = requests.post(url, data=data)
    if res.status_code == 200:
        res_json = res.json()
        print(res_json)
    else:
        res_json = res.json()
        print(res_json)

#######################################################################main#########################################################################
#최근게시물 확인, 중복일경우 종료
if(check_api_post()):
    print("이 시간대의 게시글이 이미 존재합니다.")
    sys.exit()
else:
    #인기검색어 가져오기
    imgUrl = []
    url = []
    word = []
    driver.get('인기검색어 사이트')
    #time.sleep(3)
    driver.implicitly_wait(3)

    #기본 옵션 설정
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    notices = soup.select('.rank-text')
    link = soup.select('.rank-layer')

    #인기검색어
    for tag in notices:
        word.append(tag.get_text())
        print(tag.get_text())

    #인기검색어 url
    for i in range(0,10):
        print(i)
        href = link[i].attrs['href']
        print(href)
        url.append(href)
        imgUrl.append(upload_test(href))

    #현재시간
    title = date.strftime("%Y-%m-%d %H시 인기검색어")

    #내용 만들기
    content = headCt
    content = content.replace('{{title}}',title)
    content = content.replace('{{no1}}',word[0])
    content = content.replace('{{no2}}',word[1])
    content = content.replace('{{no3}}',word[2])
    content = content.replace('{{no4}}',word[3])
    content = content.replace('{{no5}}',word[4])
    content = content.replace('{{no6}}',word[5])
    content = content.replace('{{no7}}',word[6])
    content = content.replace('{{no8}}',word[7])
    content = content.replace('{{no9}}',word[8])
    content = content.replace('{{no10}}',word[9])
    if len(imgUrl) == 10:
        for j in range(0,10):
            tempCt = """"""
            tempCt = baseCt.replace('{{tag}}',"tag" + str(int(j)+2))
            tempCt = tempCt.replace('{{imgUrl}}',imgUrl[j])
            tempCt = tempCt.replace('{{url}}',url[j])
            tempCt = tempCt.replace('{{content}}', str(int(j)+1) +'위.' +word[j])
            content += tempCt

    #글쓰기
    print(content)
    if len(imgUrl) == 10:
        get_api_test(title, content)
    