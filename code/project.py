import numpy as np
import matplotlib.pyplot as plt

n1=np.array([2,1])
n2=np.array([1,-1])
p=np.array([3,1])
N=np.vstack((n1,n2))
I=np.matmul(np.linalg.inv(N),p)
print(I)

A=np.array([1,-1])
R=np.linalg.norm(A-I)
print(R)

def dir_vec():
	return np.matmul(np.linalg.inv(omat),P)

P=I-A
omat=np.array([[0,1],[-1,0]])
print (dir_vec())
#here dir_vec() is used for direction of AB

B=np.array([-3,0])

len=10

lam_1=np.linspace(0,1,len)

x_AB=np.zeros((2,len))
x_IA=np.zeros((2,len))

for i in range(len):
	temp1=A+lam_1[i]*(B-A)
	x_AB[:,i]=temp1.T
	temp2=I+lam_1[i]*(A-I)
	x_IA[:,i]=temp2.T
	
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_IA[0,:],x_IA[1,:],label='$IA$')

plt.plot(A[0],A[1],'o')
plt.text(A[0]*1.1,A[1]*1.1,'A')
plt.plot(B[0],B[1],'o')
plt.text(B[0]*1.1,B[1]*1.1,'B')
plt.plot(I[0],I[1],'o')
plt.text(I[0]*1.1,I[1]*1.1,'I')

t=np.linspace(0,2*np.pi,100)
x=R*np.cos(t)+(4/3)
y=R*np.sin(t)+(1/3)
plt.axis('equal')
plt.plot(x,y)
plt.xlabel('$x$')
plt.xlabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.show()
plt.show()



