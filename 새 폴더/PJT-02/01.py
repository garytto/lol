import requests

Main_URL = 'https://api.themoviedb.org/3'
path = '/movie/popular'
params = {
    'api_key' : '838453ac1f4808293cf5656a23fa667a',
    'language' : 'ko-KR',
    'region' : 'KR'
}



def popular_count():
    pass
    response = requests.get(Main_URL+path, params=params).json()
    data = response["results"]
    cnt = int(len(data))
    return cnt




# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
