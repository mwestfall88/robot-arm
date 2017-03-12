import numpy as np 
import matplotlib.pylab as plt
from numpy import pi

q1_deg = 0
q2_deg = 30
q3_deg = 20

q1 = q1_deg*np.pi/180
q2 = q2_deg*np.pi/180
q3 = q3_deg*np.pi/180

# For now, eliminating rotation at the base

#T10 = np.matrix([
#	[np.cos(q1), -np.sin(q1), 0, 0],
#	[np.sin(q1), np.cos(q1), 0, 0],
#	[0, 0, 1, 0],
#	[0, 0, 0, 1],
#	])

p21 = np.matrix([[0], [0], [40], [1]])
p32 = np.matrix([[0], [0], [160], [1]])
p43 = np.matrix([[0], [0], [160], [1]])

T10 = np.matrix([
	[1, 0, 0, 0],
	[0, 1, 0, 0],
	[0, 0, 1, 0],
	[0, 0, 0, 1],
	])

T21 = np.matrix([
	[np.cos(q2), 0, np.sin(q2), p21[0,0]],
	[0, 1, 0, p21[1,0]],
	[-np.sin(q2), 0, np.cos(q2), p21[2,0]],
	[0, 0, 0, p21[3,0]],
	])

T32 = np.matrix([
	[np.cos(q3), 0, np.sin(q3), p32[0,0]],
	[0, 1, 0, p32[1,0]],
	[-np.sin(q3), 0, np.cos(q3), p32[2,0]],
	[0, 0, 0, p32[3,0]],
	])

p40 = T10*T21 * T32 * p43


#Arm is always in the 0th reerence frame
numpts = 10

arm1 = T10*p21
arm1_x = [0,arm1[0,0]]
arm1_z = [0,arm1[2,0]]

arm2 = T10*T21*p32
arm2_x = [arm1[0,0],arm2[0,0]]
arm2_z = [arm1[2,0],arm2[2,0]]

arm3 = T10*T21*T32*p43
arm3_x = [arm2[0,0],arm3[0,0]]
arm3_z = [arm2[2,0],arm3[2,0]]

plt.plot(arm1_x,arm1_z, arm2_x,arm2_z, arm3_x, arm3_z)
plt.show()

print(p40)

# def create_line(xstart, ystart, xend, yend, numpts):
# 	m = (yend-ystart)/(xend-xstart)
# 	xarr = np.array(np.linspace(xstart, xend, numpts))
# 	yarr = m*xarr+ystart
# 	return xarr, yarr

# arm1_plt = create_line(0, 0, arm1[0,0], arm1[2, 0], numpts)
# print(arm1_plt)
