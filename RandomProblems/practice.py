A = [-2, 1, 2, 4, 7, 11]
target = 5

# Time complexity: O(n^2)
# Space Complexity: O(1)
def two_sum(input, target_value):
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] + A[j] == target_value:
                print(A[i], A[j])
                return True
    return False

# Time complexity: O(n)
# Space complexity: O(n)
def two_sum_hash(input_list, target_value):
    hash_table = dict()
    for i in range(len(input_list)):
        if input_list[i] in hash_table:
            print(hash_table[input_list[i]], input_list[i])
            return True
        else:
            hash_table[target - input_list[i]] = input_list[i]
    return False

# Time complexity - O(n)
# Space complexity - O(1)
def two_sum_last(input_list, target_value):
    i = 0
    j = len(input_list) - 1
    while i <= j:
        if input_list[i] + input_list[j] == target_value:
            print(input_list[i], input_list[j])
            return True
        elif input_list[i] + input_list[j] < target_value:
            i += 1
        else:
            j -= 1
    return False

myo = two_sum_last(A, target)
print(myo)