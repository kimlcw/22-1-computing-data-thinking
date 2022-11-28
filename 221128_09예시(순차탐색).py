def serch_list(data, num):
    for i in range(len(data)):
        print('%d와 %d번째 값 %d 비교'%(num, i, data[i]))
        if (data[i] == num):
            print('같습니다.')
            break
        else:
            print('다릅니다.')

data = [53, 27, 90, 16 ,76, 31, 40, 55, 19, 25]

print(data)
num = int(input('찾고자 하는 수를 입력하세요.: '))
serch_list(data, num)

