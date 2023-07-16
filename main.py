def find_smallest_subarray_size(arr):
    n = len(arr)
    if n < 2:
        return 0
    min_val = min(arr)
    max_val = max(arr)
    min_index = -1
    max_index = -1
    min_max_diff = float('inf')
    for i in range(n):
        if arr[i] == min_val:
            min_index = i
            if max_index != -1:
                min_max_diff = min(min_max_diff, abs(max_index - min_index) + 1)
        if arr[i] == max_val:
            max_index = i
            if min_index != -1:
                min_max_diff = min(min_max_diff, abs(max_index - min_index) + 1)
    return min_max_diff
arr = [1, 3, 2]
result = find_smallest_subarray_size(arr)
print("Size of the smallest subarray:", result)

arr = [2, 6, 1, 6, 9]
result = find_smallest_subarray_size(arr)
print("Size of the smallest subarray:", result)
