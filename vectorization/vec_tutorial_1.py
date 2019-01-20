import numpy as np
import time

its = int(1e1)

a = np.random.rand(int(1e6))
b = np.random.rand(int(1e6))

tic1 = time.clock()
for it in range(its):
    c = np.dot(a, b)
toc1 = time.clock()
time1 = toc1-tic1

print(c)
print("Vectorized version: " + str(1e3*time1/its) + " ms.")

tic2 = time.clock()
d = 0
for it in range(its):
    for i in range(int(1e6)):
        d += a[i] * b[i]
toc2 = time.clock()
time2 = toc2-toc1

print(d)
print("For loop: " + str(1e3*time2/its) + " ms.")

print("Vectorized version was %.2f times faster." % (time2/time1))
