# movie_image.py

import requests
import csv

# url, 영화 대표코드 저장할 리스트
image_list = []

# movie_naver.csv에서 url, 영화 대표코드 가져오기
with open('movie_naver.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        url = row.get('image') if row.get('image') else None
        movieCd = row.get('movieCd')
        image_list.append((url, movieCd))

for url, movieCd in image_list:    
    #만약 url이 None이면 요청하지 않음
    # 이미지 파일 파이너리 형태로 저장
    if url:
        # 요청 -> 파일 저장
        # wb : 바이너리 파일을 쓰겠다.
        with open('./images/' + movieCd + '.jpg', 'wb') as f:
            response = requests.get(url)
            f.write(response.content)

