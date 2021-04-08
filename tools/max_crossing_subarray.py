def max_crossing_subarray(a, low, mid, high):
    left_sum = -float("inf")
    current_sum = 0
    for i in range(mid, low-1, -1):
        current_sum += a[i]
        if current_sum > left_sum:
            left_sum = current_sum
            max_left = i
    right_sum = -float("inf")
    current_sum = 0
    for j in range(mid+1, high+1):
        current_sum += a[j]
        if current_sum > right_sum:
            right_sum = current_sum
            max_right = j
    return (max_left, max_right, left_sum+right_sum)
