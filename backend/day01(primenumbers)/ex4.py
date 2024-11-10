def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

array = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", array)
bubble_sort(array)
print("Sorted array:", array)
# Original array: [64, 34, 25, 12, 22, 11, 90]
# Sorted array: [11, 12, 22, 25, 34, 64, 90]
