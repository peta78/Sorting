from datetime import datetime
import math
import matplotlib.pyplot as plt

fn = 'log_uniform.csv'

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

difs1 = []
difs2 = []
difs3 = []
win1 = 0
win2 = 0
win3 = 0
for i in range(1,len(x)):
    for j in range(i+1,len(x)):
        real = y2[j]/y2[i]
        on = (x[j])/(x[i])
        onlogn = (x[j]*math.log(x[j]))/(x[i]*math.log(x[i]))
        onloglogn = (x[j]*math.log(math.log(x[j])))/(x[i]*math.log(math.log(x[i])))

        difs1.append(abs(real-on))
        difs2.append(abs(real-onlogn))
        difs3.append(abs(real-onloglogn))

        if abs(real-on)<abs(real-onlogn) and abs(real-on)<abs(real-onloglogn):
            win1 += 1
        elif abs(real-onlogn)<abs(real-onloglogn):
            win2 += 1
        else:
            win3 += 1

print(win1,win2,win3)
print(sum(difs1)/len(difs1),sum(difs2)/len(difs2),sum(difs3)/len(difs3))
plt.hist(difs1,bins=30, color='r', histtype='step', density=True, label='O(n)')
plt.hist(difs2,bins=30, color='g', histtype='step', density=True, label='O(n log n)')
plt.hist(difs3,bins=30, color='b', histtype='step', density=True, label='O(n log log n)')
plt.legend()
plt.show()