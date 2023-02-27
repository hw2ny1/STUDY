import requests
from pprint import pprint


def credits(title):

    result = []
    cast_list = []

    URL = f'https://api.themoviedb.org/3/search/movie?api_key=b2a30c85b9a410c42cfb9f2f541fd4d4&query={title}'
    response = requests.get(URL).json()
    results = response.get('results')

    if len(results) > 0:
       id = results[0].get("id")

       URL = f"https://api.themoviedb.org/3/movie/{id}/credits?api_key=b2a30c85b9a410c42cfb9f2f541fd4d4&language=ko"
       response = requests.get(URL).json()
       #print(response) 


       casts = response.get('cast')

       for cast in casts:
        #print(cast.get("name"))
        cast_list.append(cast.get("name"))

       print(cast_list)

       result['cast'] = cast_list

       return result
    else :
        return None
    '''

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
    '''


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
