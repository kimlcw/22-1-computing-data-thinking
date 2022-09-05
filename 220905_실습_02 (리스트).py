
# week1) 실전문제_02
items = {'커피음료':7, '펜':3, '종이컵':2, '우유':1, '콜라':4, '책':5 }
print("재고품목 : ", items.keys())

goods = input("재고 수량을 알고 싶은 품목 입력 : ")
print(goods, "의 재고 수량은", items[goods], "입니다.")
