
# 실습 1 - 1

name = input("이름을 입력하세요: ")
add = input("주소를 입력하세요: ")
hobby = input("취미를 입력하세요: ")

print("안녕! %s님 반갑습니다!"%(name))
print("%s님은 %s에 사시는군요."%(name, add))
print("%s님은 %s를 좋아하는군요!\n"%(name, hobby))

# 파이썬도 서식문자 이용해서 출력할 수 있음.
# 근데 뒤에 쉼표로 구분 안함
# % 또 씀


# 실습 1 - 2

rad = 10
pi = 3.141592

print("반지름이 %d인 원의 넓이: %.2f" %(rad, rad * rad * pi))

rad += 10
print("반지름이 %d인 원의 넓이: %.2f" %(rad, rad * rad * pi))

rad += 10
print("반지름이 %d인 원의 넓이: %.2f" %(rad, rad * rad * pi))

rad += 10
print("반지름이 %d인 원의 넓이: %.2f" %(rad, rad * rad * pi))

rad += 10
print("반지름이 %d인 원의 넓이: %.2f" %(rad, rad * rad * pi))
