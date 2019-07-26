# 영화인 상세 정보
from decouple import config
import requests
import pprint
import csv

key = config('KEY')
# 영화인 상세정보 딕셔너리가 들어갈 리스트
people_infos = [] 
api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json?key={key}'
# print(api_url)

with open('movie.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    # row는 한 영화의 상세정보를 담고 있음
    for row in reader:
        temp = {}
        # 만약 peopleCd == None 이면 다음 row로 넘어감
        if not row.get('peopleNm'):
            continue
        # url 요청해서 값 받아오기
        response = requests.get(api_url + '&peopleNm=' + row.get('peopleNm')).json()
        # pprint.pprint(response)
        # 만약 검색 결과가 없으면 넘어감
        if not response.get('peopleListResult').get('peopleList'):
            continue
        for people in response.get('peopleListResult').get('peopleList'):
            # 영화 감독 이름이 일치하고, repRoleNm이 감독일 때 영화인 정보를 저장하고 반복문 종료
            if people.get('peopleNm') == row.get('peopleNm') and people.get('repRoleNm') == '감독':
                # print(row.get('peopleNm'))
                peopleCd = people.get('peopleCd')
                peopleNm = people.get('peopleNm')
                repRoleNm = people.get('repRoleNm')
                filmoNames = people.get('filmoNames')
                temp = {
                    'peopleCd': peopleCd,
                    'peopleNm': peopleNm,
                    'repRoleNm': repRoleNm,
                    'filmoNames': filmoNames
                }
                people_infos.append(temp)
                # print(people_infos)
                break


# director.csv에 저장하기
with open('director.csv', 'w', encoding='utf-8') as f:
    # 헤더와 딕셔너리 키 값을 맞춰줘야함.
    fieldnames = ['peopleCd', 'peopleNm', 'repRoleNm', 'filmoNames'] 
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()
    for people_info in people_infos:
        csv_writer.writerow(people_info)