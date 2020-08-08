import numpy as np 
import matplotlib.pyplot as plt 


no_actions = 10

no_tasks = 2000
no_step = 1000
Q = np.zeros([no_tasks,no_step,no_actions])
R = np.zeros([no_tasks,no_step])
epsilon  = np.array([0,0.01,0.1])


for k in range(0,epsilon.shape[0]):
	for i in range(0,no_tasks):
		print i
		qa = np.random.normal(0,1,no_actions)
		N = np.zeros(no_actions)
		# q = np.zeros(no_actions)
		j = 0
		for j in range(0,no_step):
			e = np.random.uniform(0,1)
			if(e<epsilon[k] or j==0):
				a_index = np.random.randint(no_actions)
				r = qa[a_index]
				# print "yes", a_index, r,j
			else:
				r = np.max(Q[i,j-1])
				a_index = np.where(Q[i,j-1]==r)[0][0]
				r = qa[a_index]
				# print r, a_index, j

			N[a_index]+=1
			r = r + np.random.normal(0,1)
			# print R.shape, r.shape
			R[i,j] =  r
			N1 =  N[a_index]
			# print r.shape, N1
			Q[i,j] = Q[i,j-1]
			Q[i,j,a_index] = Q[i,j-1,a_index] + (1/N1)*(r-Q[i,j-1,a_index])
	# print R.shape
	R = np.sum(R,0)/R.shape[0]
	# print R.shape
	x = np.linspace(0,R.shape[0],R.shape[0])
	plt.plot(x,R,label='Epsilon = '+str(epsilon[k]))
	R = np.zeros([no_tasks,no_step])

plt.legend()
plt.grid()
plt.xlabel('Steps')
plt.ylabel('Reward')
plt.show()