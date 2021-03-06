# 집합(set)
# 중복안됨, 순서 없음
my_set={1,2,3,3,3}
print(my_set)

java = {"유재석","김태호","양세형"}
python=set(["유재석","박명수"])

# 교집합 (java와 python을 모두 할수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합(java를 할수 있거나 python도 할수 있는 개발자)
print(java | python)
print(java.union(python)) #합집합, but 순서보장 x

# 차집합(java는 할 수있지만 python은 할줄 모르는 개발자)
print(java-python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)  # 순서는 보장 x

# 김태호가 java를 까먹었다.
java.remove("김태호")
print(java)