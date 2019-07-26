
# 1. 주간/주말 박스오피스 데이터


최근 50주간 데이터 중 주간 박스오피스 TOP10데이터 수집

* 조건
    1. 주간(월 ~ 일) `weekGb : “0” : 주간 (월~일)`
    2. 조회기간 총 50주, 기준일 2019년 7월 13일 `targetDt`
    3. 다양성 영화/상업 영화 모두 포함(default)
    4. 한국/외국 영화 모두 포함(default)
    5. 모든 상영지역 포함(default)


* 결과
    * `영화 대표코드 : movieCd`, `영화명 : movieNm`, `해당일 누적관객수 : audiAcc`
    * 해당일 누적 관객수는 중복시 최신 정보로 반영 **(이미 있는 데이터라면 그냥 넘어가기)**
    * 해당 결과 boxoffice.csv에 저장
    
* [소스코드](./01.py)



```python
# 20190713 주간 박스오피스 조회

import requests
import pprint
import datetime

key = '2c6010411226af12f598c9e149bfeca8'
weekGb = '0' # 주간
targetDt = '20190713'
api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={targetDt}'
response = requests.get(api_url).json()
pprint.pprint(response)
```

    {'boxOfficeResult': {'boxofficeType': '주말 박스오피스',
                         'showRange': '20190712~20190714',
                         'weeklyBoxOfficeList': [{'audiAcc': '6685136',
                                                  'audiChange': '-54.4',
                                                  'audiCnt': '1302522',
                                                  'audiInten': '-1555300',
                                                  'movieCd': '20196309',
                                                  'movieNm': '스파이더맨: 파 프롬 홈',
                                                  'openDt': '2019-07-02',
                                                  'rank': '1',
                                                  'rankInten': '0',
                                                  'rankOldAndNew': 'OLD',
                                                  'rnum': '1',
                                                  'salesAcc': '57709310340',
                                                  'salesAmt': '11554695230',
                                                  'salesChange': '-54.0',
                                                  'salesInten': '-13567929120',
                                                  'salesShare': '49.5',
                                                  'scrnCnt': '1708',
                                                  'showCnt': '25563'},
                                                 {'audiAcc': '10161231',
                                                  'audiChange': '3.2',
                                                  'audiCnt': '623546',
                                                  'audiInten': '19624',
                                                  'movieCd': '20183867',
                                                  'movieNm': '알라딘',
                                                  'openDt': '2019-05-23',
                                                  'rank': '2',
                                                  'rankInten': '0',
                                                  'rankOldAndNew': 'OLD',
                                                  'rnum': '2',
                                                  'salesAcc': '86703804479',
                                                  'salesAmt': '5477973020',
                                                  'salesChange': '5.0',
                                                  'salesInten': '260204110',
                                                  'salesShare': '23.5',
                                                  'scrnCnt': '975',
                                                  'showCnt': '9633'},
                                                 {'audiAcc': '3151060',
                                                  'audiChange': '-30.0',
                                                  'audiCnt': '243118',
                                                  'audiInten': '-104021',
                                                  'movieCd': '20184047',
                                                  'movieNm': '토이 스토리 4',
                                                  'openDt': '2019-06-20',
                                                  'rank': '3',
                                                  'rankInten': '0',
                                                  'rankOldAndNew': 'OLD',
                                                  'rnum': '3',
                                                  'salesAcc': '26720315850',
                                                  'salesAmt': '2062179210',
                                                  'salesChange': '-28.7',
                                                  'salesInten': '-831438970',
                                                  'salesShare': '8.8',
                                                  'scrnCnt': '784',
                                                  'showCnt': '4866'},
                                                 {'audiAcc': '220182',
                                                  'audiChange': '100.0',
                                                  'audiCnt': '118776',
                                                  'audiInten': '118776',
                                                  'movieCd': '20185353',
                                                  'movieNm': '기방도령',
                                                  'openDt': '2019-07-10',
                                                  'rank': '4',
                                                  'rankInten': '0',
                                                  'rankOldAndNew': 'NEW',
                                                  'rnum': '4',
                                                  'salesAcc': '1816098140',
                                                  'salesAmt': '1039472930',
                                                  'salesChange': '100.0',
                                                  'salesInten': '1039472930',
                                                  'salesShare': '4.5',
                                                  'scrnCnt': '603',
                                                  'showCnt': '5703'},
                                                 {'audiAcc': '101245',
                                                  'audiChange': '100.0',
                                                  'audiCnt': '93944',
                                                  'audiInten': '93944',
                                                  'movieCd': '20191601',
                                                  'movieNm': '극장판 엉덩이 탐정: 화려한 사건 '
                                                             '수첩',
                                                  'openDt': '2019-07-11',
                                                  'rank': '5',
                                                  'rankInten': '0',
                                                  'rankOldAndNew': 'NEW',
                                                  'rnum': '5',
                                                  'salesAcc': '811862520',
                                                  'salesAmt': '755074840',
                                                  'salesChange': '100.0',
                                                  'salesInten': '755074840',
                                                  'salesShare': '3.2',
                                                  'scrnCnt': '561',
                                                  'showCnt': '2570'},
                                                 {'audiAcc': '106756',
                                                  'audiChange': '100.0',
                                                  'audiCnt': '74145',
                                                  'audiInten': '74145',
                                                  'movieCd': '20185986',
                                                  'movieNm': '진범',
                                                  'openDt': '2019-07-10',
                                                  'rank': '6',
                                                  'rankInten': '0',
                                                  'rankOldAndNew': 'NEW',
                                                  'rnum': '6',
                                                  'salesAcc': '922196600',
                                                  'salesAmt': '661013300',
                                                  'salesChange': '100.0',
                                                  'salesInten': '661013300',
                                                  'salesShare': '2.8',
                                                  'scrnCnt': '224',
                                                  'showCnt': '2438'},
                                                 {'audiAcc': '9919835',
                                                  'audiChange': '-28.5',
                                                  'audiCnt': '64267',
                                                  'audiInten': '-25611',
                                                  'movieCd': '20183782',
                                                  'movieNm': '기생충',
                                                  'openDt': '2019-05-30',
                                                  'rank': '7',
                                                  'rankInten': '-3',
                                                  'rankOldAndNew': 'OLD',
                                                  'rnum': '7',
                                                  'salesAcc': '84601476725',
                                                  'salesAmt': '506735120',
                                                  'salesChange': '-36.2',
                                                  'salesInten': '-287949640',
                                                  'salesShare': '2.2',
                                                  'scrnCnt': '360',
                                                  'showCnt': '1680'},
                                                 {'audiAcc': '45707',
                                                  'audiChange': '5948.0',
                                                  'audiCnt': '31752',
                                                  'audiInten': '31227',
                                                  'movieCd': '20192151',
                                                  'movieNm': '미드소마',
                                                  'openDt': '2019-07-11',
                                                  'rank': '8',
                                                  'rankInten': '21',
                                                  'rankOldAndNew': 'OLD',
                                                  'rnum': '8',
                                                  'salesAcc': '427369480',
                                                  'salesAmt': '304193910',
                                                  'salesChange': '5990.6',
                                                  'salesInten': '299199410',
                                                  'salesShare': '1.3',
                                                  'scrnCnt': '375',
                                                  'showCnt': '1867'},
                                                 {'audiAcc': '459037',
                                                  'audiChange': '-42.1',
                                                  'audiCnt': '30789',
                                                  'audiInten': '-22397',
                                                  'movieCd': '20199951',
                                                  'movieNm': '애나벨 집으로',
                                                  'openDt': '2019-06-26',
                                                  'rank': '9',
                                                  'rankInten': '-3',
                                                  'rankOldAndNew': 'OLD',
                                                  'rnum': '9',
                                                  'salesAcc': '3809833030',
                                                  'salesAmt': '259004140',
                                                  'salesChange': '-40.1',
                                                  'salesInten': '-173465580',
                                                  'salesShare': '1.1',
                                                  'scrnCnt': '154',
                                                  'showCnt': '813'},
                                                 {'audiAcc': '913066',
                                                  'audiChange': '-69.6',
                                                  'audiCnt': '20052',
                                                  'audiInten': '-45900',
                                                  'movieCd': '20196655',
                                                  'movieNm': '존 윅 3: 파라벨룸',
                                                  'openDt': '2019-06-26',
                                                  'rank': '10',
                                                  'rankInten': '-5',
                                                  'rankOldAndNew': 'OLD',
                                                  'rnum': '10',
                                                  'salesAcc': '7802546702',
                                                  'salesAmt': '182696180',
                                                  'salesChange': '-69.3',
                                                  'salesInten': '-412456620',
                                                  'salesShare': '0.8',
                                                  'scrnCnt': '187',
                                                  'showCnt': '691'}],
                         'yearWeekTime': '201928'}}



```python
# 20190713부터 50주 동안의 주간 박스오피스 조회
import requests
import csv
import datetime

key = '2c6010411226af12f598c9e149bfeca8'
weekGb = '0' # 주간
movies = {} # 50 주간 영화 저장할 딕셔너리

# 2019년 7월 13일을 기준으로 week주 전 날짜(dt)를 반환해주는 함수
def target_date(week):
    dt = datetime.datetime(2019, 7, 13) - datetime.timedelta(weeks=week)
    return dt.strftime('%Y%m%d')
```


```python
# 1주 전 날짜
target_date(1)
```


    '20190706'




```python
# 주간 리스트 받아오기 for문 시작
for week in range(49, -1, -1): # 49주전부터 0주전(현재 2019.07.13)까지 50주 동안
    # targetDT 받아오는 함수 호출
    targetDt = target_date(week)
    api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={targetDt}&weekGb={weekGb}'
    response = requests.get(api_url).json()
    
    # 반복문 실행하여 영화 대표코드, 영화 이름, 누적관객수를 변수에 저장함
    for movie_info in response.get('boxOfficeResult').get('weeklyBoxOfficeList'):
        movieCd = movie_info.get('movieCd')
        movieNm = movie_info.get('movieNm')
        audiAcc = movie_info.get('audiAcc')
        # 키(영화 대표코드), 값(영화 정보 - 영화 대표코드, 영화명, 누적관객수) 형태의 딕셔너리를 리스트 안에 삽입
        movies[movieCd] = {'movieCd': movieCd, 'movieNm': movieNm, 'audiAcc': audiAcc}
```


```python
import pprint
pprint.pprint(movies)
```

    {'19880001': {'audiAcc': '142372', 'movieCd': '19880001', 'movieNm': '이웃집 토토로'},
     '19990220': {'audiAcc': '49958', 'movieCd': '19990220', 'movieNm': '노팅 힐'},
     '20010291': {'audiAcc': '259733',
                  'movieCd': '20010291',
                  'movieNm': '해리포터와 마법사의 돌'},
     '20020222': {'audiAcc': '79301',
                  'movieCd': '20020222',
                  'movieNm': '해리포터와 비밀의 방'},
     '20060347': {'audiAcc': '482408',
                  'movieCd': '20060347',
                  'movieNm': '판의 미로 - 오필리아와 세 개의 열쇠'},
    
    ... (생략)



```python
# boxoffice.csv 결과 파일 저장
with open('boxoffice.csv', 'w', encoding='utf-8') as f:
    fieldnames = ['movieCd', 'movieNm', 'audiAcc'] # 헤더와 딕셔너리 키 값을 맞춰줘야함.
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()
    for movie in movies.values():
        csv_writer.writerow(movie)
```


```python
# 결과 파일 확인
with open('boxoffice.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
```

    OrderedDict([('movieCd', '20186202'), ('movieNm', '신과함께-인과 연'), ('audiAcc', '12264813')])
    OrderedDict([('movieCd', '20181181'), ('movieNm', '미션 임파서블: 폴아웃'), ('audiAcc', '6567099')])
    OrderedDict([('movieCd', '20183361'), ('movieNm', '인크레더블 2'), ('audiAcc', '2998015')])
    OrderedDict([('movieCd', '20186501'), ('movieNm', '극장판 헬로카봇 : 백악기 시대'), ('audiAcc', '854230')])
    OrderedDict([('movieCd', '20185242'), ('movieNm', '신비아파트: 금빛 도깨비와 비밀의 동굴'), ('audiAcc', '667879')])
    
    ... (생략)

```
boxoffice.csv
186개의 영화 정보
1위는 극한직업, 16,243,231명
```



# 2. 영화 상세정보


01에서 수집한 영화 대표코드 활용해 상세 정보 수집.
향후 영화 정보로 활용될 것.

* 결과
    * 저장할 내용
        1.  `영화 대표코드` : movieCd
        2. `영화명(국문)` : movieNm
        3. `영화명(영문)` : movieNmEn	
        4. `영화명(원문)` : movieNmOg
        5. `관람등급` : watchGradeNm
        6. `개봉연도` : openDt
        7. `상영시간` : showTm
        8. `장르` : genreNm
        9. `감독명` : peopleNm
    
* 해당 결과 movie.csv에 저장
  
* [소스코드](./02.py)


```python
# 영화 상세정보

import requests
# import pprint
import csv

movie_infos = [] # 영화 상세정보 딕셔너리가 들어갈 리스트
key = '2c6010411226af12f598c9e149bfeca8'
api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={key}&movieCd='
```


```python
# csv 열기
with open('boxoffice.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        temp = {}
        # url로 요청하고 값 받아오기, movieCd 영화 대표코드를 이용해 영화 상세정보 검색
        response = requests.get(api_url + row.get('movieCd')).json()
        response = response.get('movieInfoResult').get('movieInfo')
        watchGradeNm = response.get('audits')[0].get('watchGradeNm') if response.get('audits') else None
        genreNm = response.get('genres')[0].get('genreNm') if response.get('genres') else None
        peopleNm = response.get('directors')[0].get('peopleNm') if response.get('directors') else None
        # 한 영화의 상세 정보 딕셔너리
        temp = {
            'movieCd': response.get('movieCd'),
            'movieNm': response.get('movieNm'),
            'movieNmEn': response.get('movieNmEn'),
            'movieNmOg': response.get('movieNmOg'),
            'watchGradeNm': watchGradeNm,
            'openDt': response.get('openDt'),
            'showTm': response.get('showTm'),
            'genreNm': genreNm,
            'peopleNm': peopleNm
        }
        movie_infos.append(temp)
```


```python
import pprint
pprint.pprint(response)
```

    {'actors': [{'cast': '',
                 'castEn': '',
                 'peopleNm': '플로렌스 퓨',
                 'peopleNmEn': 'Florence Pugh'},
                {'cast': '',
                 'castEn': '',
                 'peopleNm': '잭 레이너',
                 'peopleNmEn': 'Jack Reynor'},
                {'cast': '',
                 'castEn': '',
                 'peopleNm': '윌 폴터',
                 'peopleNmEn': 'Will Poulter'},
                {'cast': '',
                 'castEn': '',
                 'peopleNm': '윌리엄 잭슨 하퍼',
                 'peopleNmEn': 'William Jackson Harper'}],
     'audits': [{'auditNo': '2019-MF01288', 'watchGradeNm': '청소년관람불가'}],
     'companys': [{'companyCd': '20122837',
                   'companyNm': '(주)팝엔터테인먼트',
                   'companyNmEn': 'Pop Entertainment',
                   'companyPartNm': '배급사'},
                  {'companyCd': '20061718',
                   'companyNm': '찬란',
                   'companyNmEn': 'Challan Film',
                   'companyPartNm': '수입사'},
                  {'companyCd': '20122837',
                   'companyNm': '(주)팝엔터테인먼트',
                   'companyNmEn': 'Pop Entertainment',
                   'companyPartNm': '제공'},
                  {'companyCd': '20111472',
                   'companyNm': '(주)51k',
                   'companyNmEn': '',
                   'companyPartNm': '공동제공'}],
     'directors': [{'peopleNm': '아리 애스터', 'peopleNmEn': 'Ari Aster'}],
     'genres': [{'genreNm': '공포(호러)'}],
     'movieCd': '20192151',
     'movieNm': '미드소마',
     'movieNmEn': 'Midsommar',
     'movieNmOg': '',
     'nations': [{'nationNm': '미국'}],
     'openDt': '20190711',
     'prdtStatNm': '개봉',
     'prdtYear': '2019',
     'showTm': '147',
     'showTypes': [{'showTypeGroupNm': '2D', 'showTypeNm': '디지털'}],
     'staffs': [],
     'typeNm': '장편'}

01.py와 다르게 반복문을 이용하지 않는다.
`response`에는 한 영화의 상세정보를 담고 있다.
필요한 영화 대표코드, 영화명, 영화명(영문), 영화명(원문), 관람등급, 개봉연도, 상영시간, 장르, 감독명만 뽑아 딕셔너리(`temp`)로 저장한 후 `movie_infos` 리스트에 삽입한다.


```python
# 영화 상세정보 movie.csv에 저장
with open('movie.csv', 'w', encoding='utf-8') as f:
    # 헤더와 딕셔너리 키 값을 맞춰줘야함.
    fieldnames = ['movieCd', 'movieNm', 'movieNmEn', 'movieNmOg', 'watchGradeNm', 'openDt', 'showTm', 'genreNm', 'peopleNm'] 
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()
    for movie in movie_infos:
        csv_writer.writerow(movie)
```


```python
# 결과 파일 확인
with open('movie.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        pprint.pprint(row)
```

    OrderedDict([('movieCd', '20186202'),
                 ('movieNm', '신과함께-인과 연'),
                 ('movieNmEn', 'Along with the Gods: The Last 49 Days'),
                 ('movieNmOg', ''),
                 ('watchGradeNm', '12세이상관람가'),
                 ('openDt', '20180801'),
                 ('showTm', '141'),
                 ('genreNm', '판타지'),
                 ('peopleNm', '김용화')])
    
    ... (생략)

```
movie.csv
186개의 영화 상세정보
```



# 3. 영화인 상세정보

02에서 수집한 영화 감독정보를 활용해 상세 정보 수집.
향후 감독 정보로 활용될 예정.


* 요청 조건
    * 요청 변수 : key(필수), `영화인명 : peopleNm`으로 조회
    * peopleNm None 일수도
    
    
    
* 결과
    * 영화인별로 `영화인 코드 : peopleCd`, `영화인명 : peopleNm`, `분야 : repRoleNm`, `필모리스트 : filmoNames` 저장
    * **director.csv에 저장**
    (만약 검색 결과 없으면 저장하지 않기)
    
* [소스코드](./03.py)


```python
# 영화인 상세 정보

import requests
import pprint
import csv

# 영화인 상세정보 딕셔너리가 들어갈 리스트
people_infos = [] 
key = '2c6010411226af12f598c9e149bfeca8'
api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json?key={key}'
```

`api_url`은 `key`만 들어가게 한다.
반복문을 돌리면서 영화인명(`peopleNm`)으로 조회할 수 있게 한다.


```python
with open('movie.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    # row는 한 영화의 상세정보를 담고 있음
    for row in reader:
        temp = {}
        # 만약 peopleCd == None 이면 다음 row로 넘어감
        if not row.get('peopleNm'):
            continue
        # url 요청해서 값 받아오기. 영화인명으로 검색한다.
        response = requests.get(api_url + '&peopleNm=' + row.get('peopleNm')).json()
        pprint.pprint(response)
        # 만약 검색 결과가 없으면 다음 row로 넘어감
        if not response.get('peopleListResult').get('peopleList'):
            continue
        for people in response.get('peopleListResult').get('peopleList'):
            # 영화 감독 이름이 일치하고, repRoleNm이 감독일 때 영화인 상세정보를 저장하고 반복문 종료
            if people.get('peopleNm') == row.get('peopleNm') and people.get('repRoleNm') == '감독':
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
                break
```

    # pprint.pprint(response) 결과
    
    {'peopleListResult': {'peopleList': [{'filmoNames': '마약왕',
                                          'peopleCd': '20320378',
                                          'peopleNm': '김지운',
                                          'peopleNmEn': '',
                                          'repRoleNm': '케이블맨'},
                                         {'filmoNames': '오목소녀|죄 많은 '
                                                        '소녀|메소드|여자들|아이들...',
                                          'peopleCd': '20165512',
                                          'peopleNm': '김지운',
                                          'peopleNmEn': '',
                                          'repRoleNm': '홍보/마케팅 진행'},
                                         {'filmoNames': '안시성',
                                          'peopleCd': '20314900',
                                          'peopleNm': '김지운',
                                          'peopleNmEn': '',
                                          'repRoleNm': '촬영팀'},
                                         {'filmoNames': '인랑|밀정|라스트 스탠드|악마를 보았다|악마를 '
                                                        '보았다 감독판|좋은 놈, 나쁜 놈, 이상한 놈 '
                                                        '|좋은 놈, 나쁜 놈, 이상한 '
                                                        '놈(칸버전)|감독들, 김기영을 말하다|달콤한 '
                                                        '인생|장화, 홍련|쓰리|쓰리 '
                                                        '메모리즈|반칙왕|커밍 아웃|조용한 가족|더 '
                                                        '엑스|사랑의 가위바위보|선물|사랑의 '
                                                        '힘|제13회 미쟝센 단편영화제 김지운 단편 '
                                                        '특별전1|제13회 미쟝센 단편영화제 김지운 '
                                                        '단편 특별전2|제13회 미쟝센 단편영화제 '
                                                        '김지운 감독 마스터클래스|인류멸망 보고서|인류 '
                                                        "멸망 보고서 '천상의 피조물' ",
                                          'peopleCd': '10005852',
                                          'peopleNm': '김지운',
                                          'peopleNmEn': 'KIM Jee-woon',
                                          'repRoleNm': '감독'},
                                         {'filmoNames': '동네사람들|협상|꾼|조작된 도시|협녀, 칼의 '
                                                        '기억|경성학교: 사라진 소녀들|더 테너 리리코 '
                                                        '스핀토|피끓는 청춘|관상|사랑해! '
                                                        '진영아|베를린|내가 살인범이다|코리아|로맨틱 '
                                                        '헤븐|평양성|꿈은 이루어진다|미인도|서울이 '
                                                        '보이냐',
                                          'peopleCd': '20131144',
                                          'peopleNm': '김지완',
                                          'peopleNmEn': 'KIM Ji-wan',
                                          'repRoleNm': '소품'},
                                         {'filmoNames': '채비',
                                          'peopleCd': '20300250',
                                          'peopleNm': '김지운',
                                          'peopleNmEn': '',
                                          'repRoleNm': '촬영장비'},
                                         {'filmoNames': '특별시민',
                                          'peopleCd': '20295715',
                                          'peopleNm': '김지운',
                                          'peopleNmEn': '',
                                          'repRoleNm': '조명팀'},
                                         {'filmoNames': '항로-제주,조선,오사카',
                                          'peopleCd': '20209026',
                                          'peopleNm': '김지운',
                                          'peopleNmEn': 'KIM Ji-woon',
                                          'repRoleNm': ''},
                                         {'filmoNames': '간첩|달팽이의 별|체포왕|헬로우 '
                                                        '고스트|하녀|하모니|사랑',
                                          'peopleCd': '20165511',
                                          'peopleNm': '김지운',
                                          'peopleNmEn': '',
                                          'repRoleNm': '홍보/마케팅 진행'},
                                         {'filmoNames': '커플즈',
                                          'peopleCd': '20165514',
                                          'peopleNm': '김지운',
                                          'peopleNmEn': '',
                                          'repRoleNm': '배우'}],
                          'source': '영화진흥위원회',
                          'totCnt': 13}}
    
    ... (생략)



```python
# director.csv에 저장하기
with open('director.csv', 'w', encoding='utf-8') as f:
    # 헤더와 딕셔너리 키 값을 맞춰줘야함.
    fieldnames = ['peopleCd', 'peopleNm', 'repRoleNm', 'filmoNames'] 
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()
    for people_info in people_infos:
        csv_writer.writerow(people_info)
```


```python
# 결과 파일 확인
with open('director.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        pprint.pprint(row)
```

    OrderedDict([('peopleCd', '20115572'),
                 ('peopleNm', '김용화'),
                 ('repRoleNm', '감독'),
                 ('filmoNames', '저격자 ')])
    OrderedDict([('peopleCd', '10077515'),
                 ('peopleNm', '크리스토퍼 맥쿼리'),
                 ('repRoleNm', '감독'),
                 ('filmoNames',
                  '미션 임파서블: 폴아웃|미션 임파서블: 로그네이션|잭 리처|웨이 오브 더 건|유주얼 서스펙트')])

```
director.csv
166개의 영화인 상세정보
```

