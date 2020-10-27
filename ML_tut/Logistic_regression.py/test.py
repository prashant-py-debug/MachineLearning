import numpy as np

my_list = [2,3,4,5]
a = np.array(my_list)
b = np.array([1,2,3,4])
print(b.shape)
c = np.sum(b - a)
print(c)
