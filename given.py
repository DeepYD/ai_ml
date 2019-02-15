import numpy as np
import matplotlib.pyplot as plt
len=10

A=np.array([2,-3])
B=np.array([-2,1])

U=np.array([-3,7/3])
V=np.array([4,-7/3])
lam_1=np.linspace(0,1,len)

x_AB=np.zeros((2,len))
x_UV=np.zeros((2,len))
for i in range(len):
	temp1=A+lam_1[i]*(B-A)
	x_AB[:,i]=temp1.T
	temp11=U+lam_1[i]*(V-U)
	x_UV[:,i]=temp11.T

plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_UV[0,:],x_UV[1,:],label='$UV$')

plt.plot(A[0],A[1],'o')
plt.text(A[0]*1.1,A[1]*1.1,'A')
plt.plot(B[0],B[1],'o')
plt.text(B[0]*1.1,B[1]*1.1,'B')
plt.plot(U[0],U[1],'o')
plt.text(U[0]*1.1,U[1]*1.1,'U')
plt.plot(V[0],V[1],'o')
plt.text(V[0]*1.1,V[1]*1.1,'V')
plt.xlabel('$x$')
plt.xlabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.show()
