from datetime import datetime
import matplotlib.pyplot as plt
import math
import numpy as np
import sys


def theory(x,y):
    x_n = x
    x_nlogn = x * np.log(x)

    print('-------------------')

    X = np.array(x_n)
    y = np.array(y)
    X = np.reshape(X, (X.shape[0],1))
    coefficients, residualsA, rank, singular_values = np.linalg.lstsq(X, y, rcond=-1)
    k1A = coefficients
    print("Coefficients:", k1A)
    print("Residuals O(n):", residualsA)

    X = np.array([x_nlogn]).T
    y = np.array(y)
    X = np.reshape(X, (X.shape[0],1))
    coefficients, residualsB, rank, singular_values = np.linalg.lstsq(X, y, rcond=-1)
    k1B = coefficients
    print("Coefficients:", k1B)
    print("Residuals O(n log n):", residualsB)

    print('-------------------')

    if residualsA[0] < residualsB[0]:
        oname = 'O(n)'
        yy = k1A[0] * x_n
    else:
        oname = 'O(n log n)'
        yy = k1B[0] * x_nlogn

    return yy, oname

print(  )

fn = 'res.txt'

f = open(fn, 'rt')
lines = f.readlines()

x = []
y1 = []
y2 = []
for line in lines:
    parts = line.split(',')
    if len(parts) != 3:
        break

    x.append(int(parts[0]))
    y1.append(float(parts[1]))
    y2.append(float(parts[2]))

x = np.array(x)
y1 = np.array(y1)
y2 = np.array(y2)

print(x)
print(y1)
print(y2)

y1t, y1name = theory(x, y1)
y2t, y2name = theory(x, y2)

plt.figure(figsize=(15, 10))

plt.plot(x, y1, 'b', label='Intro Sort')
plt.plot(x, y2, 'r', label='Stat Sort')

plt.plot(x, y1t, 'b-.', label='Intro Sort ' + y1name)
plt.plot(x, y2t, 'r-.', label='Stat Sort ' + y2name)

plt.xlabel('vector size')
plt.ylabel('time')

plt.legend()
plt.savefig('fig_perf_' + sys.argv[1] + '.png')
plt.close()

