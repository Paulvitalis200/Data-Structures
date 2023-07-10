persons = ['Chris', 'Amber', 'David', 'El-dorado', 'Brad', 'Folake']
sortedPersons = sorted(persons)

print(sortedPersons)

numbers = (14, 3, 1, 4, 2, 9, 8, 10, 13, 12)
sortedNumbers = sorted(numbers)

print(sortedNumbers)

my_dict = {'num6': 6, 'num3': 3, 'num2': 2, 'num4': 4, 'num1': 1, 'num5': 5}

sortedDict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)

print(dict(sortedDict))
