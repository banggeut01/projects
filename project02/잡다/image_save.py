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