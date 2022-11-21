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
#assending
for k in range(0, len(data)-1, 1):
    min = k
    for j in range(k+1, n, 1):
        if (data[j] < data[min]):
            min = j
        data[min], data[k] = data[k], data[min]
    print("%d회전 :  %s"%(k+1, data))
    
print("정렬 후 데이터 : ", data)
