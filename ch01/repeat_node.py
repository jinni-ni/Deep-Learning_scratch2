import numpy as np

D, N = 8, 7
x = np.random.randn(1, D)
print(x)
# 순전파
y = np.repeat(x, N, axis=0)
print("----y-----")
print(y)

print("backpropagateion")
dy = np.random.randn(N, D)
print(dy)

print(np.sum(dy[:][0]))
#역전파
dx = np.sum(dy, axis=0, keepdims=True)
print("-------dx---------")
print(dx)

# sum 노드
D,N = 8,7
x = np.random.randn(N, D)
y = np.sum(x, axis=0, keepdims=True)

dy = np.random.randn(1,D)
dx = np.repeat(dy, N, axis=0)
