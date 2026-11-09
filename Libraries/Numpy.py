#Numpy that is numerical data
import numpy as np

#Arange()   End point is not display
n2 = np.arange(24)
print(n2)

n3 = np.arange(1,24,2)
print(n3)

#ones()
n4 = np.ones(4) # Data type is float
print(n4)
print(type(n4))

n5 = np.ones((3,4),dtype=int)
print(n5)
print(n5.dtype)
print(n5.ndim)

#Zeros
n6 = np.zeros(4)
print(n6)
print(n6.dtype)

n7 = np.zeros((3,4),dtype=int)
print(n7)
print(n7.dtype)
print(n7.ndim)

#linspace() it'll display end point
n8 = np.linspace(10,20)
print(n8)     #default num = 5 so it sample start to end into 50

n9 = np.linspace(10,20,num=5)
print(n9)

n10 = np.linspace(10,20,num=5, endpoint=False)
print(n10)

#reshape()

n11 = np.arange(1,13)
print(n11)
print("Dimension is ",n11.ndim)

n12 = np.reshape(n11,(3,4),order='F')   #order - false means it'll arrange the data in column wise
print(n12)

#ravel() - convert the 2D array in 1D
n13 = np.ravel(n12)
print(n13)

#Transpose()
n14 = np.arange(6).reshape((2,3))
print(n14)
print("After Transpose: ")
n15 = np.transpose(n14)
print(n15)

