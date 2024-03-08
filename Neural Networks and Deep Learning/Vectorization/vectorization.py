import numpy as np

# For example, lets take this example of calories from 4 different food:
#                      Apples  Beef  Eggs  Potatoes
#  Carb                56.0    0.0   4.4    68.0
# Protein               1.2   104.0  52.0    8.0
# Fat                   1.8   135.0  99.0    0.9

# Lets calculate the % of calories for Carb, Protein, Fat 
# For each of those food WITHOUT using an explicit for-loop
# By implementing Vectorization:

A = np.array([[56.0, 0.0, 4.4, 68.0],
            [1.2, 104.0, 52.0, 8.0],
            [1.8, 135.0, 99.0, 0.9]])

# That is our array with the above data, it dimensions are: (3,4)

cal = A.sum(axis=0)

percentage = 100*A/cal.reshape(1,4)

print(percentage)
