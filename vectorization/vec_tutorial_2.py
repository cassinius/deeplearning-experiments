import numpy as np
import time
import math

its = int(1e1)
n = int(1e6)
v = np.random.rand(n)

u = np.zeros((n, 1))

tic1 = time.process_time()
for it in range(its):
    for i in range(n):
        u[i] = math.exp(v[i])
toc1 = time.process_time()
time1 = toc1-tic1
print("For loop exponentiation: " + str(1e3*time1/its) + " ms.")

tic2 = time.process_time()
for it in range(its):
    u = np.exp(v)
toc2 = time.process_time()
time2 = toc2-tic2
print("Vectorized exponentiation: " + str(1e3*time2/its) + " ms.")

print("Vectorized version was %.2f times faster." % (time1/time2))
