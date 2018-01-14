import numpy as np
import time

a = np.random.rand(1000000)
b = np.random.rand(1000000)

tic = time.clock()
c = np.dot(a, b)
toc = time.clock()

print(c)
# print("Tic: " + str(tic))
# print("Toc: " + str(toc))
print("Vectorized version: " + str(1e3*(toc-tic)) + " ms.")

tic2 = time.clock()
d = 0
for i in range(1000000):
    d += a[i] * b[i]
toc2 = time.clock()
print(d)
print("For loop: " + str(1e3*(toc2-tic2)) + " ms.")

print("Vectorized version was " + str((toc2-tic2)/(toc-tic)) + " times faster.")
