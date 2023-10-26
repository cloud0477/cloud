# -*- coding: euc-kr -*-
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import time
from bs4 import BeautifulSoup
import datetime as dt
import random
import requests
import json
from dateutil.relativedelta import relativedelta
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

#공통변수
blog_id = ''
token = ''
location = '서울'

#크롬 연결
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options = option)
driver.get('청약홈페이지')
driver.implicitly_wait(3)

#오늘 날짜
date = dt.datetime.now()

#json 파일읽기
file_path = "E:/dev/python/blog_byPython/real/crolling/arr_seoul.json"
def json_read():
    data = {}
    with open(file_path, 'r', encoding='UTF8') as file:
        data = json.load(file)
    return data

#기본 옵션 설정
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

#검색 옵션 설정
dropdown = Select(driver.find_element(By.XPATH,'//*[@id="cate02"]'))  #정렬기준 드롭다운
dropdown.select_by_value(location)
driver.implicitly_wait(3)

#올해1월
january = date.strftime("%Y01")
dropdown = Select(driver.find_element(By.XPATH,'//*[@id="start_year"]'))  
dropdown.select_by_value(january)
driver.implicitly_wait(3)

#오늘기준 한달후
now = date + relativedelta(months=1)
now = now.strftime("%Y%m")
dropdown = Select(driver.find_element(By.XPATH,'//*[@id="end_year"]'))  
dropdown.select_by_value(now)
driver.implicitly_wait(3)

#조회
driver.find_element(By.XPATH,'//*[@id="pbSearchForm"]/div[2]/button').click()
driver.implicitly_wait(3)

#랜덤 태그 붙이기
def random_tag():
    #200개
    arr = ["부동산 시장", "아파트 검색", "분양 공고", "아파트 계약", "아파트 인테리어 디자인", "아파트 입주 일정", "아파트 관리비", "아파트 가구 구매", "아파트 시세 예측", "아파트 리모델링", "아파트 입주 심사", "아파트 모델 하우스 투어", "아파트 유지보수 비용", "아파트 리스", "아파트 임대", "아파트 중개", "아파트 거래", "아파트 구입", "아파트 판매", "아파트 대출", "아파트 중개업체", "아파트 전용면적", "아파트 건설사", "아파트 개발", "아파트 분양사", "아파트 신청", "아파트 입주 신청", "아파트 분양신청", "아파트 시세 변동", "아파트 홈스테이징", "아파트 시설", "아파트 가격대", "아파트 시티뷰", "아파트 공사 현황", "아파트 세금", "아파트 경매", "아파트 경기도", "아파트 부산", "아파트 서울", "아파트 대전", "아파트 경남", "아파트 경북", "아파트 전세", "아파트 월세", "아파트 전세금", "아파트 월세계약", "아파트 보증금", "아파트 공인중개사", "아파트 입주자격", "아파트 청약통장", "아파트 대출한도", "아파트 단기임대", "아파트 재건축", "아파트 재개발", "아파트 주차장", "아파트 공간활용", "아파트 친환경", "아파트 에너지효율", "아파트 안전", "아파트 보안 시스템", "아파트 공동주택", "아파트 분리수거", "아파트 생활편의시설", "아파트 주민모임", "아파트 홈오더", "아파트 동물 반려", "아파트 자동화 시스템", "아파트 스마트홈", "아파트 소음 대책", "아파트 화재 대비", "아파트 환기 시스템", "아파트 엘리베이터", "아파트 수영장", "아파트 체육시설", "아파트 놀이터", "아파트 공원", "아파트 쇼핑몰", "아파트 카페", "아파트 레스토랑", "아파트 헬스장", "아파트 교육시설", "아파트 유치원", "아파트 초등학교", "아파트 중학교", "아파트 고등학교", "아파트 대학교", "아파트 도서관", "아파트 의료시설", "아파트 병원", "아파트 약국", "아파트 편의점", "아파트 주변 상가", "아파트 교통편", "아파트 버스정류장", "아파트 지하철역", "아파트 고속도로", "아파트 공항", "아파트 주차 시설", "아파트 주거환경", "아파트 주거 만족도"]

    tag = """아파트 분양 정보, 아파트 분양, 서울, 경기, 아파트, 부동산, 청약,"""
    r_no = random.sample(range(0,100),50)
    for i in r_no:
        if( i != len(r_no) - 1):
            tag = tag + arr[i] + ', '
        else:
            tag = tag + arr[i]
    return tag

#테이블 만들기
def get_table():
    time.sleep(1)
    header = "<tr><td>지역</td><td>주택구분</td><td>분양/임대</td><td>주택명</td><td>시공사</td><td>문의처</td><td>모집공고일</td><td>청약기간</td><td>당첨자발표</td></tr>"
    inner = ""

    paging = len(driver.find_element(By.ID,'paging').find_elements(By.TAG_NAME,'a'))
    tableCnt = len(driver.find_element(By.TAG_NAME,'tbody').find_elements(By.TAG_NAME,'tr'))

    data = json_read()
    for k in range(1,paging+1):
        #다음 페이지 조회
        driver.execute_script('fn_link_page(' + str(k) +');return false;')

        try:
            for i in range(1,tableCnt+1):
                    td = ""
                    for j in range(1,10):
                        item = driver.find_element(By.XPATH,'//*[@id="subContent"]/div[4]/table/tbody/tr[' + str(i) + ']/td[' + str(j) + ']').text
                        if j != 4:
                            td = td + "<td>" +  item + "</td>"
                        else:
                            #링크달기
                            try:
                                td = td + "<td><a href='" +  data[item] + "'>" + item + "</a></td>"
                            except:
                                td = td + "<td>" +  item + "</td>"
                        driver.implicitly_wait(3)
                    inner = inner + "<tr>" + td + "</tr>"
        except:
            continue
    table = '<table data-ke-align="alignLeft" data-ke-style="style12"><tbody>' + header + inner + '<table><tbody>'
    return table

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
                'category': 1057621,
                'acceptComment': 1, #댓글 비허용 - 0, 허용 -1
    }
    res = requests.post(url, data=data)
    if res.status_code == 200:
        res_json = res.json()
        print(res_json)
    else:
        res_json = res.json()
        print(res_json)
#-------------------------------------------------------------main-------------------------------------------------------------

today = date.strftime("%Y년 %m월 %d일 ")
title = '[' + location + '] ' + today + ' 기준 아파트 분양 정보'
content = '<h2 data-ke-size="size26">[' + location +  '] ' + today + ' 기준 아파트 분양 정보</h2><ul style="list-style-type: disc;" data-ke-list-type="disc"><li>국민, 민영 모두 포함한 분양 정보입니다.</li><li>이 글은 청약 홈의 글을 참고한 표입니다.</li><li>청약 제한 여부 확인은 청약 홈에서 확인 바랍니다.</li></ul>'
table = get_table()
print('table : ' + table)
#글쓰기
get_api_test(title, content + table)


