# 22/11/14
# 버블정
# 실습

def A_ham(input_num, my_num):
    for i in range(input_num-1, 0, -1):
        for j in range(0, i, 1):
            if(my_num[j]>my_num[j+1]):
                my_num[j], my_num[j+1] = my_num[j+1], my_num[j]
        print("%d회전 : %s"%(input_num-i, my_num))

def B_ham(input_num, my_num):
    for i in range(input_num-1, 0, -1):
        for j in range(0, i, 1):
            if(my_num[j]<my_num[j+1]):
                my_num[j], my_num[j+1] = my_num[j+1], my_num[j]
        print("%d회전 : %s"%(input_num-i, my_num))




my_num = []

input_num = int(input("몇 개의 숫자를 입력하시겠습니까? "))

for i in range(0, input_num, 1):
     temp_num = int(input("숫자를 입력하세요. : "))
     my_num.append(temp_num)

print("정렬 전 데이터 : ", my_num)
my_type = input("정렬방식을 입력하세요. A(오름차순) 또는 D(내림차순) : ")

if(my_type == 'A' or my_type == 'a'):
    A_ham(input_num, my_num)
elif(my_type == 'D' or my_type == 'd'):
    B_ham(input_num, my_num)
else:
    print("정렬방법을 다시 선택하세요.")


print("정렬 후 데이터 : ", my_num)
