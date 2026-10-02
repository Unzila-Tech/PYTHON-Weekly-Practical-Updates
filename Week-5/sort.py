import numpy as np
arr = np.array([[1,2,3],
                [5,4,3],
                [3,1,7]])

case1=arr[:,arr[1].argsort()]
case2=arr[arr[:,1].argsort()]
print("second Row sort")
print(case1)
print("second Column sort")
print(case2)
