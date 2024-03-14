#https://youtu.be/UARBitWTIwQ?list=PLlvFEn0NKwXI6m_qufpwM3R7rOSGMFtdK&t=1778
import numpy as np
import time
import sys
a = np.array([1,2,3])
print(a)
print(a[0])
print(a[2])
print('='*30)
b = range(1000)
print(sys.getsizeof(5)*len(b))
print('@'*30)
c = np.arange(1000)
print(c.size*c.itemsize)
#https://youtu.be/UARBitWTIwQ?list=PLlvFEn0NKwXI6m_qufpwM3R7rOSGMFtdK&t=1901
print('#'*30)
size = 100000
l1 = range(size)
l2 = range(size)
A1 = np.arange(size)
A2 = np.arange(size)

start = time.time()
result=[(x + y)for x, y in zip(l1, l2)] 
result=[(x + y)for x, y in zip(l1, l2)]
print(result)
print('python list took:',(time.time() - start)*1000)
print('*'*40)
start = time.time()
result=A1+A2
print('numpy array took:',(time.time() - start)*1000)
# output numpy array took: 4.44483757019043
print('#'*40)
a = np.array([[1,2],[3,4],[5,6]])
print(a)#we have 3 different objects:
#[[1 2]
#  [3 4]
#  [5 6]]
z = a.ndim
print(z)#output: 2
#we have 2 dimensions array
print('-'*40)
w = a.itemsize
print(w)#output:8
print('3'*40)
r = a.shape
print(r)#output:(3, 2)=(3 objects, 2 elements)

a1 = np.array([[1,2],[3,4],[5,6]],dtype=np.float64)
print(a1)#output:[[1. 2.]
#  [3. 4.]
#  [5. 6.]]
print('7'*50)
r1 = a.itemsize
print(r1)#output:8 we see the size is doubled
#https://youtu.be/UARBitWTIwQ?list=PLlvFEn0NKwXI6m_qufpwM3R7rOSGMFtdK&t=2404


