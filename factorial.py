

def trial(n):
    count = 0
    i = 1

    while (n//(5**i) != 0):
        count += n//(5**i)
        i += 1

    return count


print(trial(40))
