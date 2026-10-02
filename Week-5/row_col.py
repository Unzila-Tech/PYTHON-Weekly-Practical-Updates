import numpy as np
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])
# odd Row even col
new_arr = arr[::2, 1::2]

print(new_arr)
