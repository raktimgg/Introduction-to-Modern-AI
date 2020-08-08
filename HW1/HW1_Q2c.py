import numpy as np

###### The states and actions are repersented as follows: low-0, high-1, search-0, wait-1, recharge-2 ########

r = np.zeros([4])
v = np.zeros([2])
pr = np.zeros([2,2,3])
gama = 0.5
epsilon = 1e-50

r[0] = 2
r[1] = 1
r[2] = 0
r[3] = -3

pr[1][1][0] = 0.3
pr[1][0][0] = 1 - pr[1][1][0]
pr[1][1][1] = 1
pr[0][0][0] = 0.2
pr[0][1][0] = 1 - pr[0][1][0]
pr[0][0][1] = 1
pr[0][1][2] = 1

v[1] = 0
v[0] = 0


t=1
while(t==1):
	v_high_old = v[1]
	v_low_old = v[0]
	v[1] = np.max(((pr[1][1][0]*(r[0]+gama*v[1])+pr[1][0][0]*(r[0]+gama*v[0])),pr[1][1][1]*(r[1]+gama*v[1])))
	v[0] = np.max(((pr[0][0][0]*(r[0]+gama*v[0])+pr[0][1][0]*(r[3]+gama*v[1])),pr[0][0][1]*(r[1]+gama*v[0]),pr[0][1][2]*(r[2]+gama*v[1])))
	err_good = np.absolute(v[1]-v_high_old)
	err_bad = np.absolute(v[0] - v_low_old)
	delta = np.max((err_good,err_bad))
	if(delta<epsilon):
		t = 0


pi_high = np.argmax(((pr[1][1][0]*(r[0]+gama*v[1])+pr[1][0][0]*(r[0]+gama*v[0])),pr[1][1][1]*(r[1]+gama*v[1])))
pi_low = np.argmax(((pr[0][0][0]*(r[0]+gama*v[0])+pr[0][1][0]*(r[3]+gama*v[1])),pr[0][0][1]*(r[1]+gama*v[0]),pr[0][1][2]*(r[2]+gama*v[1])))
print "Value at high = ",v[1]
if(pi_high==0):
	print "When at high, the policy says to search"
else:
	print "When at high, the policy says to wait"
print "Value at low = ",v[0]
if(pi_low==0):
	print "When at low, the policy says to search"
if(pi_low==1):
	print "When at low, the policy says to wait"
else:
	print "When at low, the policy says to recharge"
