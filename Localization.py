import numpy as np
p=np.array([0.2,0.2,0.2,0.2,0.2])
pHit = 0.6
pMiss = 0.2
m=np.array([0.6,0.6,0.2,0.2,0.2])
#Enter code here
p = p * m
p = p/p.sum()
# print p

p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i]/s
    return q

# for i in range(len(measurements)):
#     p = sense(p,measurements[i])
#     print p
p=[0, 1, 0, 0, 0]
def move(p, U):
    q = []
    for i in range(len(p)):
        # step = (i-U)%len(p)
        # q.append(p[step])
        U = U % len(p)
        q = p[-U:] + p[:-U]
    return q

print move(p, -1)