# mongodb_prac

- localhost:27017 을 통해서 mongodb 연결 확인 가능

- robo 3t

  - 들어가서 따로 건들건 없고
  - create 눌러서 name 설정 해주기
  - robo 3t의 역할 :
    - mongoDB의 데이터 베이스를 볼 수 있게 해준다.

- DB
  - RDBMS(SQL)
    - 행/열의 생김새가 정해진 엑셀에 데이터를 저장하는 것과 유사하다.
    - 데이터 50만개가 적재된 상태에서, 갑자기 중간에 열을 하나 더하기는 어렵다.
    - 하지만, 정형화되어 있는 만큼, 데이터의 일관성이나, 분석에 용이할 수 있다.
    - ex) MS-SQL, My-SQL
  - No-SQL
    - 딕셔너리 형태로 데이터를 저장해두는 DB
    - 고로 데이터 하나 하나 마다 같은 값들을 가질 필요가 없다.
    - 자유로운 형태의 데이터 적재에 유리한 대신, 일관성 부족할 수 있다.
    - ex) MongoDB