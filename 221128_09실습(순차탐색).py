def serch_list(data, h_data, name):
    for i in range(len(data)):
        if (data[i] == name):
            result = data_height[i]
            return result;
    return '이름이 없습니다. 다시 입력하세요.'
            
data = ['미선', '지연', '성식', '민석', '지민', '소현', '정국']
data_height = [150, 165, 170, 177, 168, 158, 163]

print(data)

while(1):
    name = input('학생 이름 입력(stop : end) :' )
    if name == 'end':
        break
    else :
        print(serch_list(data, data_height, name))


