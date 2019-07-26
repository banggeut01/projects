
#  02 - 파이썬을 활용한 데이터 수집 II 


## 요구사항
1. 네이버 영화 검색 API - `movie_naver.py`

   project01에서 얻은 `movie.csv`의 `영화명(국문)`을 바탕으로 네이버 영화 검색 API를 통해 추가적 데이터 수집. 해당 데이터는 기준 평점 및 영화 썸네일로 활용될 것.

   * 요청
     * 필수 요청변수 query: `영화명(국문)`으로 요청
   * 응답
     * movie.csv파일의 `영진위 영화 대표코드`, link: `하이퍼텍스트 link`, image: `영화 썸네일 이미지 URL`, userRating: `유저 평점`
     * `영화 썸네일 이미지 URL`이 없으면 저장하지 않기.
     *  **movie_naver.csv**에 저장하기

   * [소스보기](./movie_naver.py)

```python
# movie_naver.py

# 01. API URL로 요청 후 응답 받아오기

import requests
from decouple import config
import pprint

# 네이버 API 설정
client_id = config('NAVER_CLIENT_ID')
client_secret = config('NAVER_CLIENT_SECRET')

# 헤더 설정
headers = {
    'X-Naver-Client-Id': client_id,
    'X-Naver-Client-Secret': client_secret
}

# 요청
api_url = 'https://openapi.naver.com/v1/search/movie.json'
# 실제 코드에서는 query를 movie.csv에서 받아와야한다.
query = '자전차왕 엄복동'

response = requests.get(f'{api_url}?query={query}', headers=headers).json()
pprint.pprint(response)
```

    {'display': 1,
     'items': [{'actor': '비|강소라|이범수|',
                'director': '김유성|',
                'image': 'https://ssl.pstatic.net/imgmovie/mdi/mit110/1590/159070_P13_114738.jpg',
                'link': 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=159070',
                'pubDate': '2018',
                'subtitle': 'Race to Freedom : Um Bok Dong',
                'title': '<b>자전차왕 엄복동</b>',
                'userRating': '3.84'}],
     'lastBuildDate': 'Fri, 26 Jul 2019 10:01:01 +0900',
     'start': 1,
     'total': 1}

`client_id`와`client_secret`처럼 노출되지 말아야하는 정보는 `.env `파일(환경변수 파일)을 통해 관리. 

`.env`는 `.gitignore`에 넣어주어 git이 접근하지 못하게 해야함.


```python
# 02. movie.csv에서 query에 넣어줄 영화명(국문) 가져오기

with open('movie.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        pprint.pprint(row)
        break
```

    OrderedDict([('영화 대표코드', '20196309'),
                 ('영화명(국문)', '스파이더맨: 파 프롬 홈'),
                 ('영화명(영문)', 'Spider-Man: Far From Home'),
                 ('영화명(원문)', ''),
                 ('관람등급', '12세이상관람가'),
                 ('개봉연도', '20190702'),
                 ('상영시간', '129'),
                 ('장르', '액션'),
                 ('감독', '존 왓츠')])

```python
# 영화명(국문)
row.get('영화명(국문)')
```


    '스파이더맨: 파 프롬 홈'




```python
# 03. link, image userRating 값 추출하기

response.get('items') # 리스트 안에 딕셔너리가 포함된 형태
```


    [{'title': '<b>자전차왕 엄복동</b>',
      'link': 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=159070',
      'image': 'https://ssl.pstatic.net/imgmovie/mdi/mit110/1590/159070_P13_114738.jpg',
      'subtitle': 'Race to Freedom : Um Bok Dong',
      'pubDate': '2018',
      'director': '김유성|',
      'actor': '비|강소라|이범수|',
      'userRating': '3.84'}]


```python
print(response.get('items')[0].get('link'))
print(response.get('items')[0].get('image'))
print(response.get('items')[0].get('userRating'))
```

    https://movie.naver.com/movie/bi/mi/basic.nhn?code=159070
    https://ssl.pstatic.net/imgmovie/mdi/mit110/1590/159070_P13_114738.jpg
    3.84



```python
# 04. movies 리스트에 영화 코드, 링크, 이미지, 평점 딕셔너리 형태로 삽입

movies = []

temp = {
    # movieCd 추가하기
    'link': response.get('items')[0].get('link'),
    'image': response.get('items')[0].get('image'),
    'userRating': response.get('items')[0].get('userRating')
}

movies.append(temp)
```


```python
# 05. 결과 movie_naver.csv에 저장하기

import csv

with open('movie_naver.csv', 'w', encoding='utf-8') as f:
    # 영화 대표 코드 'movieCd' 추가하기
    fieldnames = ['link', 'image', 'userRating']
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()
    for movie in movies:
        csv_writer.writerow(movie)
```


```python
# ------<결과 파일 확인하기>------

with open('movie_naver.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        pprint.pprint(row)
```

    OrderedDict([('link',
                  'https://movie.naver.com/movie/bi/mi/basic.nhn?code=159070'),
                 ('image',
                  'https://ssl.pstatic.net/imgmovie/mdi/mit110/1590/159070_P13_114738.jpg'),
                 ('userRating', '3.84')])


코드 완성 후 실제 `movie_naver.csv` 결과


```python
with open('movie_naver.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    count = 0
    for row in reader:
        pprint.pprint(row)
        count += 1
    print(f'movie_naver.csv {count}개의 행')
```

    OrderedDict([('movieCd', '20196309'),
                 ('link',
                  'https://movie.naver.com/movie/bi/mi/basic.nhn?code=173123'),
                 ('image',
                  'https://ssl.pstatic.net/imgmovie/mdi/mit110/1731/173123_P06_135928.jpg'),
                 ('userRating', '8.37')])
                 
    ... (생략)
    
    movie_naver.csv 186개의 행



## 요구사항

2. 영화 포스터 이미지 저장 -  `movie_image.py`

* `movie_naver.py`에서 받아온 이미지 url에 요청을 보내 실제 이미지 파일로 저장. 
* 향후 영화 포스터 이미지로 사용될 것
  * 요청
    * 영화 썸네일 이미지 URL
  * 응답
    * 응답 결과 파일로 저장하기. 반드시 `wb`옵션으로 저장하기.
    * 저장되는 파일명은 `images`폴더 내에 `영진위 영화 대표코드.jpg`    
  * [소스보기](./movie_image.py)   



```python
# 예시) 이미지 url로 요청 후 바이너리 파일로 저장하기 

import requests

# 인터넷 상의 이미지파일
url = 'https://ssl.pstatic.net/imgmovie/mdi/mit110/1590/159070_P13_114738.jpg'

# 요청 -> 파일 저장
# wb : 바이너리 파일을 쓰겠다.
with open('./images/test.jpg', 'wb') as f:
    response = requests.get(url)
    print(response.content)
    f.write(response.content) 
    # 텍스트형식(json, html, xml...)이 아닌 
    # 바이너리 형식을 받을 때는 .content
```

바이너리 파일로 쓰게 되면 아래와 같은 내용으로 저장된다.

    b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00d\x00d\x00\x00\xff\xec\x00\x11Ducky\x00\x01\x00\x04\x00\x00\x00\x1e\x00\x00\xff\xdb\x00C\x00\x08\x06\x06\x07\x06\x05\x08\x07\x07\x07\t\t\x08\n\x0c\x14\r\x0c\x0b\x0b\x0c\x19\x12\x13\x0f\x14\x1d\x1a\x1f\x1e\x1d\x1a\x1c\x1c $.\' ",#\x1c\x1c(7),01444\x1f\'9=82<.342\xff\xdb\x00C\x01\t\t\t\x0c\x0b\x0c\x18\r\r\x182!\x1c!22222222222222222222222222222222222222222222222222\xff\xc0\x00\x11\x08\x00\x9d\x00n\x03\x01"\x00\x02\x11\x01\x03\x11\x01\xff\xc4\x00\x1c\x00\x00\x02\x03\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x05\x03\x06\x07\x02\x01\x00\x08\xff\xc4\x00;\x10\x00\x02\x
    
    ... (생략)



```python
# movie_image.py
# movie_naver.csv에서 url(image), 영진위 영화 대표코드 받아오기

import requests
import csv

# url, 영화 대표코드(movieCd) 저장할 리스트
image_list = []

with open('movie_naver.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        url = row.get('image') if row.get('image') else None
        movieCd = row.get('movieCd')
        image_list.append((url, movieCd))
        break
    print(image_list)
    
for url, movieCd in image_list:
    #만약 url이 None이면 요청하지 않음
    # 이미지 파일 파이너리 형태로 저장
    if url:
        with open('./images/' + movieCd + '.jpg', 'wb') as f:
            response = requests.get(url)
            f.write(response.content)
```

    [('https://ssl.pstatic.net/imgmovie/mdi/mit110/1731/173123_P06_135928.jpg', '20196309')]


movie_image.py 실행 결과 ./images 디렉토리에는 186개의 영화 포스터 이미지 파일이 생성됨.

