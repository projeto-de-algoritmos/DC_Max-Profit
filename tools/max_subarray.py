from tools import max_crossing_subarray


def max_subarray(a, low, high):
    if low == high:  # base case
        return (low, high, a[low])
    else:
        mid = (low+high)//2
        left_low, left_high, left_sum = max_subarray(a, low, mid)
        right_low, right_high, right_sum = max_subarray(a, mid+1, high)
        cross_low, cross_high, cross_sum = max_crossing_subarray.max_crossing_subarray(
            a, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)
