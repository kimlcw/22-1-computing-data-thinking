dic = {}
dic['커피음료'] = '7'
dic['펜'] = '1'
dic['종이컵'] = '2'
dic['우유'] = '3'
dic['콜라'] = '4'
dic['책'] = '5'

answer = input('재고 수량을 알고 싶은 물건의 이름 : ')
print(answer, '의 재고 수량은 ',  dic[answer], '입니다')
