# 1. 영화 제목 '매트리스'의 평점 가지고 오기
# 2. '매트리스'와 같은 평점의 영화 제목 가지고 오기
# 3. '매트리스' 영화 평점을 0으로 만들기

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# 코딩 시작

# 1번 문제
matrix = db.movies.find_one({'title': '매트릭스'}, {'_id': False})
print(matrix['star'])

# 2번 문제
same_stars = list(db.movies.find({'star': "9.39"}, {'_id': False}))
for movie_title in same_stars:
    print(movie_title['title'])

# 3번 문제
db.movies.update_one({'title': '매트릭스'}, {'$set': {'star': '0'}})
# 여기서 다른 영화들의 star가 문자열로 저장되어 있음으로 관리의 용의성을 위해 숫자 0 말고 문자열 0으로 저장해주는게 좋다.
