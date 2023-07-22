def high_and_low(numbers):
    numbers_list = numbers.split(" ")
    for i in range(len(numbers_list)):
        numbers_list[i] = int(numbers_list[i])
    output_str = str(max(numbers_list))  + " " + str(min(numbers_list))
    print(numbers_list)
    return output_str

print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))

