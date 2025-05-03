# Бинарный поиск

arr = [8, 1, 3, 45, 12, 34, 2, 0 ]
arr = sorted(arr)
print(arr)

value = 8
def binary_search(arr, value):
    left, right = 0, len(arr)-1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == value:
            return mid
        elif arr[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1
# a = binary_search(arr, value)
# print(a)
print(binary_search(arr, value))