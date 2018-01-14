import numpy as np
import time
import math

n = 1000000
v = np.random.rand(n)

u = np.zeros((n, 1))
tic = time.clock()
for i in range(n):
    u[i] = math.exp(v[i])
toc = time.clock()
print("For loop exponentiation: " + str(1e3*(toc-tic)) + " ms.")

tic2 = time.clock()
u = np.exp(v)
toc2 = time.clock()
print("Vectorized exponentiation: " + str(1e3*(toc2-tic2)) + " ms.")

print("Vectorized version was " + str((toc-tic)/(toc2-tic2)) + " times faster.")

