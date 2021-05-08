# pymongo 사용을 위한 기본 코드
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta
# dbsparta라고 하는 db이름으로 접속할 거라는 뜻, 그걸 이제 db로 잡는 것이다.(해당 이름 db가 없으면 만들어 진다.)

# 코딩 시작

# 저장 - 예시
doc = {'name': 'jane', 'age': 21}
db.users.insert_one(doc)
# 여기서 users는 collection이라고 해서 비슷한 애들끼리 모은거라고 생각하면 된다.
# db안에 users라는 컬렉션에 작업한다는 뜻


# 한 개 찾기 - 예시
user = db.users.find_one({'name': 'bobby'}, {'_id': False})
print(user)
print(user['age'])


# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
same_ages = list(db.users.find({'age': 21}, {'_id': False}))
# 처음 나오는 중괄호는 조건이라 만약 조건 없이 모든 데이터를 가지고 오고 싶으면 빈 중괄호로 넣으면 된다.
same_ages = list(db.users.find({}, {'_id': False}))
print(same_ages)
# 이렇게 하면 리스트 안에 있는 딕셔너리 형태로 나온다.
for person in same_ages:
print(person)


# 바꾸기 - 예시
db.users.update_one({'name': 'bobby'}, {'$set': {'age': 19}})
# name이 boby인 애를 찾아서 age를 19로 바꿔라
db.users.update_many({'name': 'bobby'}, {'$set': {'age': 19}})
# 이름이 바비인 애를 모두 찾아서 바꿔라 // 잘 쓰진 않는다. 위험해서


# 지우기 - 예시
db.users.delete_one({'name': 'bobby'})
db.users.delete_many({'name': 'bobby'})
