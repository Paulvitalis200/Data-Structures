import random

names = ["James", "Alicia", "Frost", "John", "Grace", "Wambui"]

my_dict = {customer:random.randint(1, 100) for customer in names}

days = ["Sunday", "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
temp_C = [30.5,32.6,31.8,33.4,29.8,30.2,29.9]

dates = {day:temp for (day, temp) in zip(days, temp_C)}

customer_10 = {customer:discount for(customer, discount) in my_dict.items() if discount < 40}
print(dates)
print(dates.items())
print(my_dict)
print(customer_10)