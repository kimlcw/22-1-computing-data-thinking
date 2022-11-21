# 8. 정렬기법 [선택, 삽입]
# [ 예시 ]

# 선택 정렬
data = []
n = int(input("몇 개의 숫자를 입력하시겠습니까? "))

for i in range(n):
    num = int(input("숫자를 입력하세요. : "))
    data.append(num)
print("정렬 전 데이터 : ", data)
# 5 4 3 2 1

# n = len(data)
for k in range(0, len(data)-1, 1):
    min = data[k]
    for j in range(k+1, n, 1):
        if (data[j] < min):
            min = data[j]
        data[j] = data[k]
        data[k] = min
    print("%d회전 :  %s"%(k+1, data))
    
print("정렬 후 데이터 : ", data)
