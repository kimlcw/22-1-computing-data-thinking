# 11 이진 탐색 [실습]

def quick_sort(array, start, end):

    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while (left <= right) :
        while (left <= end and array[left] <= array[pivot]):
            left = left + 1
        while (right > start and array[right] >= array[pivot]) :
            right = right - 1
        if left > right :
            array[right], array[pivot] = array[pivot], array[right]
        else :
            array[right], array[left] = array[left], array[right]

    print(array)
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

array = [7, 2, 9, 4, 3, 5, 6, 1]

quick_sort(array, 0, len(array)-1)
print("최종정렬", array)



