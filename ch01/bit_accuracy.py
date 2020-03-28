import numpy as np

a = np.random.randn(3)
print(a.dtype) #float64

b = np.random.randn(3).astype(np.float32)
print(b.dtype) #float32

c = np.random.randn(3).astype('f')
print(c.dtype) #float32

