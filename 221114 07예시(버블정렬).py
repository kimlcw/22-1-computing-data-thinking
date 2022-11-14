# 22/11/14
# 버블정렬
# 예시

# (9, 0, -1) 9, 8, 7, ... 1 (9번 반복)
def bubble_sort(data):
    for i in range(len(data)-1, 0, -1):
        for j in range(0, i, 1):
            if(data[j]>data[j+1]):
                data[j], data[j+1] = data[j+1], data[j]
        print("%d회전 : %s"%(len(data)-i, data))


data = [6, 3, 0, 8, 2, 7, 4, 5, 1, 9] # 10갱
print("정렬 전 데이터 :", data)
bubble_sort(data)
print("정렬 후 데이터 :", data)
