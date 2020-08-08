import numpy as np

#### The states and actions are represented as follows: good-0, bad-1, stay-0, move-1 #######

r = np.zeros([2])
pr = np.zeros([2,2,2])
v = np.zeros([2])
pi = np.zeros([2])
gama = 0.5
epsilon = 1e-20

r[0] = 3
r[1] = -1

v[0] = 0.
v[1] = 0.

pr[0][0][0] = 0.5
pr[0][1][0] = 1 - pr[0][0][0]
pr[0][1][1] = 1.
pr[1][1][0] = 1.
pr[1][0][1] = 1.


t=1
i = 0
while(t==1):
	v_good_old = v[0]
	v_bad_old = v[1]
	v[0] = np.max(((pr[0][0][0]*(r[0]+gama*v[0])+pr[0][1][0]*(r[1]+gama*v[1])),pr[0][1][1]*(r[1]+gama*v[1])))
	v[1] = np.max((pr[1][1][0]*(r[1]+gama*v[1]),pr[1][0][1]*(r[0]+gama*v[0])))
	err_good = np.absolute(v[0]-v_good_old)
	err_bad = np.absolute(v[1] - v_bad_old)
	delta = np.max((err_good,err_bad))
	if(delta<epsilon):
		t = 0

pi[0] = np.argmax(((pr[0][0][0]*(r[0]+gama*v[0])+pr[0][1][0]*(r[1]+gama*v[1])),pr[0][1][1]*(r[1]+gama*v[1])))
print "Value at good = ",v[0]
if(pi[0]==0):
	print "When at good, the policy says to stay"
else:
	print "When at good, the policy says to move"
pi[1] = np.argmax((pr[1][1][0]*(r[1]+gama*v[1]),pr[1][0][1]*(r[0]+gama*v[0])))
print "Value at bad = ",v[1]
if(pi[1]==0):
	print "When at bad, the policy says to stay"
else:
	print "When at bad, the policy says to move"