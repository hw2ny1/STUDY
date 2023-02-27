import requests
from pprint import pprint


def recommendation(title):
    result = []

    URL = f'https://api.themoviedb.org/3/search/movie?api_key=b2a30c85b9a410c42cfb9f2f541fd4d4&query={title}'
 
    response = requests.get(URL).json()

    if len(response.get('results')) > 0:

        response = requests.get(URL).json()
        id = response.get('results')[0].get("id")
        

        URL = f'https://api.themoviedb.org/3/movie/{id}/recommendations?api_key=b2a30c85b9a410c42cfb9f2f541fd4d4'
        response = requests.get(URL).json()
        datas = response.get('results')



        for data in datas:
            result.append(data.get('title'))
        return result
    
    return None


        


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
