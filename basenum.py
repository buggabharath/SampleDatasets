import numpy as np

a = np.array([(1,2,3,4,5), (6,7,8,9,0)])
b = np.arange(10)
print(a)
print(a.shape)
print(a.reshape(5,2))
print(a[:,0], a[:,1])
a[:]
a[0:]
a[0:1]
a[0:2]
b
b[:6]
b[:0]
print(a[0:2, 1:3])
a[0,3]
a[1,3]
a[1,4]
a[0:1]
c = a.reshape(5,2)
c
c[3,1]
c[0:3]
c[:,0]
c[:,1]
