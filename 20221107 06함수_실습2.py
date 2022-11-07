# 06 함수
# [실습2] 

def gofl(ob, my):
    print("현재 층은 %d층입니다."%myfl)
    if(ob>my):
           
        my++
        
    elif(ob<my):
        my--

obfl = int(input("가고자 하는 층 입력 : "))
myfl = int(input("현재 위치 입력 : "))


print("현재 층은 %d층입니다."%myfl)
