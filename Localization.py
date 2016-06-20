import numpy as np
p=np.array([0.2,0.2,0.2,0.2,0.2])
pHit = 0.6
pMiss = 0.2
m=np.array([0.6,0.6,0.2,0.2,0.2])
#Enter code here
p = p * m
p = p/p.sum()
print p
print "--------------------------------"
p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
motions = [1,1]
Z = 'red'
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i]/s
    return q

for i in range(len(measurements)):
    p = sense(p,measurements[i])
    print p
print "--------------------------------"

p=[0, 1, 0, 0, 0]
def move(p, U):
    q = []
    for i in range(len(p)):
        s = pExact * p[(i-U)%len(p)] + pOvershoot * p[(i-U-1)%len(p)] + pUndershoot * p[(i-U+1)%len(p)]
        q.append(s)
    return q

for i in range(1000):
    p = move(p, 1)
print p
print "--------------------------------"

for i in range(len(measurements)):
    p = sense(p,measurements[i])
    p = move(p,motions[i])
print p
print "--------------------------------"