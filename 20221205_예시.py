# 10 파이썬 이진탐색 예시

mylist = []
idnum = int(input("몇 개의 숫자를 입력하시겠습니까? "))

for i in range (idnum) :
    num = int(input("숫자를 입력하세요. : "))
    mylist.append(num)

# 버블, 선택, 삽입

mylist.sort()

# 삽입
#for k in range (0, idnum):
#    temp = mylist[k]
#    j = k-1
#    while (j >= 0 and mylist[j] > temp):
#        mylist[j+1] = mylist[j]
#        j = j-1
#    mylist[j+1]=temp

print("초기데이터 : ", mylist)

target = int(input("찾고자 하는 숫자를 입력하세요. : "))
left = 0
right = len(mylist) - 1

while (left <= right) :
    mid = (left + right) // 2
    if (mylist[mid] > target):
        right = mid-1
    elif(mylist[mid] < target):
        left = mid+1
    else:
        break

if (mylist[mid] == target):
    print("찾고자 하는 수는 %d번째 인덱스 위치에  있습니다."%(mid))
else:
    print("찾고자 하는 수가 없습니다.")
