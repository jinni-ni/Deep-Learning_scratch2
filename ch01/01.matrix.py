import numpy as np
import matplotlib.pylab as plt

x = np.array([1,2,3])
x.__class__

print(x.shape)
#dimension
print(x.ndim)

W = np.array([[1,2,3],[4,5,6]])
print(W.shape)
print(W.ndim)


W = np.array([[1,2,3],[4,5,6]])
X = np.array([[0,1,2],[3,4,5]])
print(W+X)

print("========")
print(W*X)

A = np.array([[1,2],[3,4]])
print(A*10)

# 내적
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.dot(a,b))

# 곱
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print(np.matmul(A,B))



def sigmoid(x):
    return 1/(1 + np.exp(-x))

x = np.random.randn(10,2)
W1 = np.random.randn(2,4)
b1 = np.random.randn(4)
W2 = np.random.randn(4,3)
b2 = np.random.randn(3)

# h(10,4)
h = np.matmul(x,W1) + b1
print(h.shape)
a = sigmoid(h)
print("a==============")
print(a)
s = np.matmul(a,W2) + b2
print(s)
