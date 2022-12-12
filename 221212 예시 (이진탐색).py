# 11 이진 탐색 [예시]
##############################################
def binary_search(list, item):
    left = 0
    right = len(list) -1
    ###########################################
    while (left <= right) :
        mid = (left + right) // 2
        if (item == list[mid]) :
            return mid  # 예비번호 알림용
            # break문으로는 while문만 빠져나갈 수 있기 때문에
            # return 처리함.
        elif (item > list[mid]) :
            left = mid + 1
        else :
            right = mid - 1
    ###########################################
    return -1
##############################################
students = [100, 101, 121, 130, 151, 160, 171, 186, 190, 200] # 합격자
wating_students = [102, 122, 135, 163, 180] # 예비합격자

num = int(input("수험 번호를 입력하세요\n입력: "))
result = binary_search(students, num)
wating_result = binary_search(wating_students, num)

if (result != -1) :
    print("수험번호 %d님은 합격하셨습니다." %(num))
elif (wating_result != -1) :
    print("수험번호 %d님은 합격하진 못했지만 예비번호 %d입니다." %(num, wating_result+1))
else :
    print("수험번호 %d님은 불합격이고 예비번호가 없습니다. " %(num))








