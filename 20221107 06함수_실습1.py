# 06 함수
# [실습1] 
def fac(my):
    if(my == 0):
        return 1
    return my * fac(my-1)

num = int(input("숫자를 입력하세요 : "))

fact = fac(num)
print("%d!의 값은 %d입니다."%(num, fac(num)))
