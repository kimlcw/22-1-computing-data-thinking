name = input("학생 이름을 입력하세요. :")
kor_score = int(input("국어 점수를 입력하세요. :"))
math_score = int(input("수학 점수를 입력하세요. :"))
eng_score = int(input("영어 점수를 입력하세요. :"))
com_score = int(input("컴퓨터 점수를 입력하세요. :"))

ave = (kor_score + math_score + eng_score + com_score)/4
print("%s의 평균 점수는 %.6f입니다."%(name, ave))
print("%s의 평균 점수는 %d입니다."%(name, ave))
print("%s의 평균 점수는 %.2f입니다."%(name, ave))
