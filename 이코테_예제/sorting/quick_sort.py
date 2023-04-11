array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end :
        return 
    pivot = start
    left = start +1
    right = end 
    
    while left <= right :
        #print(array)
        #왼->오로 피봇보다 큰 값 찾기 
        while left <= end and array[left] <= array[pivot] :
            left += 1
        #오->왼으로 피봇보다 작은 값 찾기 
        while right >start and array[right] >= array[pivot]:
            right -= 1
        #엇갈린 경우 작은 값과 피봇 값 스와프
        if left > right :
            array[right],array[pivot] = array[pivot],array[right]
        #엇갈리지 않았다면 큰 값과 작은 값 스와프
        else :
            array[left],array[right] = array[right],array[left]

    #엇갈려서 while 탈출한 후에는 피봇 값이 right으로 이동. 그 값 기준으로 왼(작), 오(큰) 묶음 각각 퀵 정렬 수행
    quick_sort(array, start, right-1)   #왼(작 부분)
    quick_sort(array, right+1, end)     #오(큰 부분)

quick_sort(array,0,len(array)-1)
print(array)