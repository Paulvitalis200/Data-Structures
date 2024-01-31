import numpy as np


one_dimensional_array = np.array([1.2,2.4,3.5,4.7,5.6,6.1,7.9,8.9])

two_dimensional_array = np.array([[2,3], [4,5], [4,9], [1,7]])
zeros_array = np.zeros(5)
ones_array =  np.ones(3)

sequence_of_integers = np.arange(5, 12)

random_integers_between_50_and_100 = np.random.randint(low=50, high=101, size=(6,))
children = np.random.randint(low=0, high=101, size=(6,))
random_floats_between_0_and_1 = np.random.random((6,))
random_floats_between_2_and_3 = random_floats_between_0_and_1 + 2.0
random_integers_between_150_and_300 = random_integers_between_50_and_100 * 3
features = np.arange(6, 21)
label = features * 3 + 4
noise =  np.random.random((2,3))

# print(sequence_of_integers)

# print(one_dimensional_array)
# print(two_dimensional_array)
# print(zeros_array)
# print(ones_array)
print(random_integers_between_50_and_100)
print(children)
# print(random_floats_between_0_and_1) 
# print(random_floats_between_2_and_3)
# print(random_integers_between_150_and_300)
# print(features)
# print(label)
# print(noise)