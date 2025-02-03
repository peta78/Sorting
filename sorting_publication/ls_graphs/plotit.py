from datetime import datetime
import math
import numpy as np
import sys
import matplotlib.pyplot as plt

def compute_res_a0_a1(x,y):
    coefs = 0
    res = 0
    
    A = []
    B = []
    for i in range(len(x)):
        A.append([x[i]])
        B.append([y[i]])
        
    A = np.array(A)
    B = np.array(B)
    At = np.transpose(A)
    X = np.matmul(np.linalg.inv(np.matmul(At,A)),np.matmul(At,B))
    
    yhat = np.matmul(A,X)
    res = yhat-B
    res = np.matmul(np.transpose(res), res)
    
    return yhat, res

def theory(x,y):
    x_n = x
    x_nlogn = x * np.log(x)
    x_nloglogn = x * np.log(np.log(x))

    print('-------------------')

    X = np.array(x_n)
    y = np.array(y)
    yA, residualsA = compute_res_a0_a1(X,y)
    print("Residuals O(n):", residualsA)
    
    X = np.array(x_nlogn)
    y = np.array(y)
    yB, residualsB = compute_res_a0_a1(X,y)
    print("Residuals O(n log n):", residualsB)

    X = np.array(x_nloglogn)
    y = np.array(y)
    yC, residualsC = compute_res_a0_a1(X,y)
    print("Residuals O(n log log n):", residualsC)

    print('-------------------')

    if residualsA < residualsB and residualsA < residualsC:
        return yA, 'O(n)'
    elif residualsB < residualsC:
        return yB, 'O(n log n)'
    else:
        return yC, 'O(n log log n)'


print(  )

fn = 'log_' + sys.argv[1] + '.csv'

f = open(fn, 'rt')
lines = f.readlines()

x = []
y1 = []
y2 = []
for line in lines:
    parts = line.split(',')
    if len(parts) != 7:
        break

    s1 = datetime.strptime(parts[3], "%Y-%m-%d %H:%M:%S.%f")
    s2 = datetime.strptime(parts[4], "%Y-%m-%d %H:%M:%S.%f")
    s3 = datetime.strptime(parts[5], "%Y-%m-%d %H:%M:%S.%f")

    x.append(float(parts[2]))
    y1.append(float((s2-s1).total_seconds()))
    y2.append(float((s3-s2).total_seconds()))

x = np.array(x)
y1 = np.array(y1)
y2 = np.array(y2)

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