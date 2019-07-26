import requests
from decouple import config
import pprint
import csv

movies = [] # 결과 저장할 리스트

# 네이버 API 설정
client_id = config('NAVER_CLIENT_ID')
client_secret = config('NAVER_CLIENT_SECRET')

# 헤더 설정
headers = {
    'X-Naver-Client-Id': client_id,
    'X-Naver-Client-Secret': client_secret
}

# 요청 api_url
api_url = 'https://openapi.naver.com/v1/search/movie.json'

# movie.csv 파일에서 query: 영화명(국문), 영화 대표코드 가져오기
with open('movie.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        query = row.get('영화명(국문)')
        movieCd = row.get('영화 대표코드')

        # 요청
        response = requests.get(f'{api_url}?query={query}', headers=headers).json()

        # 필요한 정보 영화 대표코드, 링크, 이미지 평점 저장하기
        # 썸네일 이미지 url 없으면 None 처리
        image = response.get('items')[0].get('image') if response.get('items')[0].get('image') else None
        temp = {
        'movieCd': movieCd,
        'link': response.get('items')[0].get('link'),
        'image': image,
        'userRating': response.get('items')[0].get('userRating')
        }
        movies.append(temp)

# 결과 movie_naver.csv에 저장하기
with open('movie_naver.csv', 'w', encoding='utf-8') as f:
    fieldnames = ['movieCd', 'link', 'image', 'userRating']
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()
    for movie in movies:
        csv_writer.writerow(movie)
