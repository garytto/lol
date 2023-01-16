import requests
from pprint import pprint


def search_movie(title):
    pass
    Main_URL = 'https://api.themoviedb.org/3'
    path = '/movie'
    params = {
    'api_key' : '838453ac1f4808293cf5656a23fa667a',
    'language' : 'ko-KR',
    'region' : 'KR'
    }
    response = requests.get(Main_URL+path, params=params).json()
    name = response["results"][title]
    
    return name

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id 반환
    검색한 결과 영화가 없다면 None을 반환
    """
    print(search_movie('기생충'))
    # 496243
    print(search_movie('그래비티'))
    # 959101
    print(search_movie('검색할 수 없는 영화'))
    # None
