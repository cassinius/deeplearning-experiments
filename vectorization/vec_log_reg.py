import numpy as np
import time
import math
import sys

# Nr. Training samples
m = 300

# Amount of features (100x100 pixel images)
n = 10000

# Simulated training samples
x = np.random.rand(m, n, 1)
print("X shape: " + str(x.shape))
y = np.random.randint(2, size=m)

# print(x.shape)
# print(y)

# Weight vector & bias
w = np.ones((n, 1))
# print("Weight shape: " + str(w.shape))
b = 0

# derivative vector & bias
dw = np.zeros((n, 1))
db = 0

# Overall Cost
J = 0

for i in range(0, m):
    # print("x[i] shape: " + str(x[i].shape))
    z_i = np.dot(np.transpose(w), x[i]) + b
    print("z_i: " + str(z_i))
    # print(z_i.shape)
    a_i = 1 / (1 + np.exp(-z_i))
    print("a_i: " + str(a_i))

    a_i = sys.float_info.min if a_i == 0 else a_i
    a_i_sub = 1 - a_i
    a_i_sub = sys.float_info.min if a_i_sub == 0 else a_i_sub

    J -= y[i] * math.log(a_i) + (1 - y[i]) * math.log(a_i_sub)
    dz_i = a_i * (1 - a_i)
    dw += x[i] * dz_i
    db += dz_i

J /= m
dw /= m
db /= m

print("Total cost: " + str(J))
print("Final gradient: " + str(dw))
print("Final bias: " + str(db))
