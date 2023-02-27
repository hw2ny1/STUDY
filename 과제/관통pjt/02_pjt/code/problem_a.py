import requests

URL = 'https://api.themoviedb.org/3/movie/popular?api_key=b2a30c85b9a410c42cfb9f2f541fd4d4'


def popular_count():
# requests 사용 예시 1
    response = requests.get(URL).json()
    #print(response.get('results'))
    print(response)
    datas = response.get('results')

    return len(datas)



 


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
