def remove_dups(input_arr):

    l = 1
    for i in range(1, len(input_arr)):
        if input_arr[i] != input_arr[i-1]:
            input_arr[l] = input_arr[i]
            l += 1

    return l