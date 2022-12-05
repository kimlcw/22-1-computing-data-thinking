# 10 파이썬 이진탐색 실습 - 함수로 구현하기
def binary_search(dxlist, dxnum):
    left = 0
    right = len(dxlist) -1

    while (left <=right):
        mid = (left+right)//2

        if (dxlist[mid] == dxnum):
            return 1
        elif (dxnum > dxlist[mid]):
            left = mid + 1
        else:
            right = mid - 1

    return -1
        


students = [2022100, 2022101, 2022121, 2022130, 2022151, 2022160, 2022171]
num = int(input("출석 여부를 알고 싶은 응시번호 입력:"))
attend = binary_search(students, num)

if (attend == 1):
    print("출석한 학생입니다. 답안지를 다시 찾아보세요")
else:
    print("출석하지 않은 학생입니다.")
