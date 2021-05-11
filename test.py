
def binary_search(array,num):
    """
	this is a test py
    """
    if not array:
        return -1
    mid = 0
    left = 0
    right = len(array)-1

    while left < right:
        print(left,right)
        mid = (right+left)//2
        print(mid)
        if array[mid] == num:
            return mid
        elif array[mid] < num:
            left = mid + 1
        else:
            right = mid

    return -1

ans = binary_search([1,2,3,4,5,6,7,8],10)
print(ans)
