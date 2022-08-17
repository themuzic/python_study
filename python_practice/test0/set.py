# set : 집합. 중복안됨, 순서 없음

java = {"유재석", "김태호", "정형돈"}
python = set(["유재석","하하","노홍철"])

# 두 set의 교집합(중복값) 출력하기
print(java & python)
print(java.intersection(python))

# 두 set의 합집합(중복값은 한번만 나옴)
print(java | python)
print(java.union(python))
