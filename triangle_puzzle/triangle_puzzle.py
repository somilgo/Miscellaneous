import matplotlib.pyplot as plt 
import numpy as np
import math
import random

random.seed()
def midpoint(a, b):
	return [(a[0]+b[0])/2,(a[1]+b[1])/2]

def distance(a, b):
	return math.sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2)

plt.ylim(-1, 1)
plt.xlim(-1, 1)

x = [-.75, .75, 0]
y = [-.75, -.75, (math.sqrt(27)/4)-.75]
points = zip(x,y)


currentPoint = [1e9,1e9]
check = True
while (check):
	currentPoint = [random.random()*2-1, random.random()*2-1]
	for i in points:
		if distance(currentPoint, i) > (math.sqrt(27)/4):
			check = True
			break
		else:
			check = False
xpoints = []
ypoints = []
for i in range(100000):
	xpoints.append(currentPoint[0])
	ypoints.append(currentPoint[1])
	ind = random.randint(0,2)
	currentPoint = midpoint(currentPoint,points[ind])
	if i % 100 == 0:
		print "You're on iteration " + str(i)

plt.scatter(xpoints, ypoints, color='b', s=10, alpha=0.5)
plt.scatter(x, y, color='r', s=100, alpha=0.5)
plt.show()