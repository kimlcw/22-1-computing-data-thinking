
# 파이썬에는 모듈이 있음. 그 중 하나가 turtle()
import turtle
turtle.shape("turtle")
turtle.pensize(5)


######### 삼각형 : 이동 후 120도 회전 * 3회 #########
turtle.forward(100) # 거리
turtle.left(120) # 각도

turtle.forward(100) # 거리
turtle.left(120) # 각도

turtle.forward(100) # 거리
turtle.left(120) # 각도
#########################################

######### 사각형 : 이동 후 90도 회전 * 4회 #########
turtle.clear()
turtle.forward(100)
turtle.left(90)

turtle.forward(100)
turtle.left(90)

turtle.forward(100)
turtle.left(90)

turtle.forward(100)
turtle.left(90)
#########################################

######### 원 : 이동 후 1도 회전 * 360회 or circle 함수 #########
turtle.clear()

# turtle.circle(100)
#turtle.circle(100, 360, 4) 360를 4번 꺾어서 도달
turtle.circle(100, 360, 360)

# turtle.forward(1) # 거리
# turtle.left(1) # 각도
#########################################
