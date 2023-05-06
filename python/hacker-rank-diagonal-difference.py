def diagonalDifference(arr):
    # Write your code here
    primary_sum = arr_sum(arr)
    
    arr_rev = arr[::-1]
    secondary_sum = arr_sum(arr_rev)

    diff_sum = abs(primary_sum - secondary_sum)
    return diff_sum


def arr_sum(ar):
    ar_sum = 0
    for i in range(len(ar)):
        ar_sum = ar_sum + arr[i][i]
    return ar_sum