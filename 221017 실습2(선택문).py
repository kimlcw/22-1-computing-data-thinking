# 영화관 입장료 계산하는 프로그램
# 성인 입장료는 13,000원이며, 청소년은 11,000원으로 계산합니다.
# 청소년은 7세 이상 ~ 18세 이하로 제한
# 7세 미만은 입장료를 받지 않습니다.
# 성인 관람 인원수와 청소년 관람 인원수, 취학 전 아동의 관람 인원수를 물어본 다음

sum = 0
adult = int(input("성인 인원수를 입력해주세요 : "))
youth = int(input("청소년 인원수를 입력해주세요 : "))
kids = int(input("취학 전 어린이의 인원수를 입력해주세요 : "))

if adult > 0:
    sum = adult * 13000
    print("성인 %d명"%(adult), end=" ")
if youth > 0:
    sum = sum + youth * 11000
    print("청소년 %d명"%youth, end=" ")
if kids > 0:
    sum = sum + (kids * 0)
    print("취학 전 어린이 %d명"%kids, end=" ")

print("요금 총합은 %d원입니다."%(sum))
