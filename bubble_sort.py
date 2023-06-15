def bubble(unsorted_list):
    is_sorted = False
    indexing_length = len(unsorted_list) - 1

    while not is_sorted:
        is_sorted = True
        for i in range(0, indexing_length):
            if unsorted_list[i] > unsorted_list[i+1]:
                unsorted_list[i], unsorted_list[i +
                                                1] = unsorted_list[i+1], unsorted_list[i]
                is_sorted = False

    return unsorted_list


print(bubble([48, 30, 4, 29, 199, 39, 43, 91, 19]))
