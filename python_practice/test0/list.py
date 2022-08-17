# site_name = "http://naver.com"
# site_name = site_name[site_name.find("/")+2:site_name.find(".")]
# # print(site_name)

# pw1 = site_name[0:3]
# pw2 = len(site_name)
# pw3 = site_name.count("e")
# print(f"{pw1}{pw2}{pw3}!")

# arr = (1,2,3)
# print(type(arr))
# tuple은 조작 불가. 조회만 가능

subway = ["유재석","노홍철","박명수","정준하"]
print(subway)

subway.append("하하")
print(subway)

subway.insert(1,"정형돈")
print(subway)

print(subway.index("노홍철"))
print(subway.pop()) # 뒤에서 한 요소를 꺼내고 꺼낸값을 반환
print(subway)

subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬(오름차순)
# subway.sort()
# print(subway)

# 반대로 정렬 : 실행하는 배열을 그대로 반대로만 뒤집는다.
subway.reverse()
print(subway)

# .clear() : 모두 지우기
# list는 자료형 타입 상관없이 아무거나 다 섞어서 삽입 가능

num_list = [1,2,3,4,5]

# list 끼리 합치는거 가능(확장)

# 첫번째 방벙
# subway.extend(num_list)
# print(subway)

# 두번째 방법
# print(subway + num_list)
