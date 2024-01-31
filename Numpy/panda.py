import numpy as np
import pandas as pd

# Create and populate a 5x2 NumPy array.
my_data = np.array([[0, 3], [10, 7], [20, 9], [30, 14], [40, 15]])

# Create a Python list that holds the names of the two columns.
my_column_names = ['temperature', 'activity']

# Create a DataFrame.
my_dataframe = pd.DataFrame(data=my_data, columns=my_column_names)

# Create a new column named adjusted.
my_dataframe["adjusted"] = my_dataframe["activity"] + 2

# children = np.random.randint(low=0, high=101, size=(3,4))
children = np.random.randint(low=0, high=101, size=(3,4))

# Create a Python list that holds the names of the two columns.
child_column_names = ['Eleanor', 'Chidi', 'Tahani', 'Jason']

# Create a DataFrame.
children_dataframe = pd.DataFrame(data=children, columns=child_column_names)

children_dataframe['Janet']  = children_dataframe["Tahani"] +  children_dataframe['Jason']

print(children)
# print(child_column_names)
# print(children_dataframe)
# print(children_dataframe['Eleanor'][1], '\n')

# # Print the entire DataFrame
# print(my_dataframe)

# print("Rows #0, #1, and #2:")
# print(my_dataframe.head(3), '\n')

# print("Row #2:")
# print(my_dataframe.iloc[[2]], '\n')

# print("Rows #1, #2, and #3:")
# print(my_dataframe[1:4], '\n')

# print("Column 'temperature':")
# print(my_dataframe['temperature'])