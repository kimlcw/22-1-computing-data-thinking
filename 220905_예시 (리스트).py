
# week1) 예시문제
aa = [15, 30, 10, 20]
print('현재 리스트 : ', aa)

aa.append(40)
print('append(40) 후의 리스트 : ', aa)

print('pop()으로 추출한 값 : ', aa.pop()) # 스택(프링글스 구조)
print('pop() 후의 리스트 : ', aa)

aa.sort()
print('sort() 후의 리스트 : ', aa)

aa.reverse()
print('reverse() 후의 리스트 : ', aa)

print('20 값의 위치 : ', aa.index(20))

aa.insert(2, 222)
print('insert(2, 222) 후의 리스트 : ', aa)

aa.remove(222)
print('remove(222) 후의 리스트 : ', aa)

aa.extend([77, 88, 77])
print('extend([77, 88, 77]) 후의 리스트 : ', aa)

print('77 값의  개수 : ', aa.count(77))

