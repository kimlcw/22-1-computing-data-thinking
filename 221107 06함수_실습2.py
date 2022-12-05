# 06 함수
# [실습2]

# 올라가는 함수
def up(n, t):
    for floor in range(n, t+1, 1):
        print("현재 층은 %d입니다."%(floor))
    print("%d층에 도착하였습니다. 안녕히 가세요."%(target))


# 내려가는 함수
def down(n, t):
    for floor in range(n, t-1, -1):
        print("현재 층은 %d입니다."%(floor))
    print("%d층에 도착하였습니다. 안녕히 가세요."%(target))


######################### input ############################
while 1 :
    target = int(input("가고자 하는 층 입력 : "))
    now = int(input("현재 위치 입력 : "))

    if((target == now) or (target>6) or (target <1) or (now>6) or (now<1)):
        print("다른 층(1~6)을 눌러주세요.\n")
    else:
        break

###########################################################
if(target>now):
    up(now, target)
elif(target<now):
    down(now, target)



