# 8. 정렬기법 [선택, 삽입]
# [ 실습 ]

# 삽입 정렬
data = []
n = int(input("몇 개의 숫자를 입력하시겠습니까? "))

for i in range(n):
    num = int(input("숫자를 입력하세요. : "))
    data.append(num)
print("정렬 전 데이터 : ", data)

updown = input("정렬방식을 선택하세요.\nA(오름차순) 또는 D(내림차순) : ")

if (updown == 'A' or updown == 'a'):
    for k in range(1, len(data), 1):
        temp = data[k]
        j = k-1
        while (j >= 0 and data[j] > temp): # 정렬된 data[j]가 temp보다 크면 temp를 그 앞에 꽂아야 함.
            data[j+1] = data[j] # while문 1회차에 data[j+1] (data[k], temp) 는 덮힘.
            j = j-1
            # 뒤로 한 칸씩 밀어주는 코드
        data[j+1] = temp
        # j가 -1일 때는 0에,
        # 0 이상일 때에는 
        # 덮힌 data[j+1] 넣기
        print("%d회전 : %s"%(k, data))

elif(updown == 'D' or updown == 'd'):
    for k in range(1, len(data), 1):
        temp = data[k]
        j = k-1
        while (j >= 0 and data[j] < temp): # 정렬된 data[j]가 temp보다 작으면 temp를 그 앞에 꽂아야 함.
            data[j+1] = data[j] # while문 1회차에 data[j+1] (data[k], temp) 는 덮힘.
            j = j-1
            # 뒤로 한 칸씩 밀어주는 코드
        data[j+1] = temp
        # j가 -1일 때는 0에,
        # 0 이상일 때에는 
        # 덮힌 data[j+1] 넣기
        print("%d회전 : %s"%(k, data))
    
else:
    print("정렬방법을 다시 선택하세요.")
    
print("정렬 후 데이터 : ", data)
