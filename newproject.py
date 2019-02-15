import numpy as np
import matplotlib.pyplot as plt
len=10

A=np.array([2,-3])
B=np.array([-2,1])

P=np.array([-1,11/3])
Q=np.array([4,1/3])
U=np.array([-3,7/3])
V=np.array([4,-7/3])

def dir_vec():
	return np.matmul(np.linalg.inv(omat),N)
	
N=np.array([2,3])
omat=np.array([[0,1],[-1,0]])
print (dir_vec())

for k in range(0,1):
	C=np.array([k,(9-2*k)/3])
	for k in range(1,2):
		D=np.array([k,(9-2*k)/3])
		for k in range(2,3):
			E=np.array([k,(9-2*k)/3])
			for k in range(3,4):
				F=np.array([k,(9-2*k)/3])
				lam_1=np.linspace(0,1,len)

				x_AB=np.zeros((2,len))
				x_UV=np.zeros((2,len))
				x_PQ=np.zeros((2,len))
				x_BC=np.zeros((2,len))
				x_BD=np.zeros((2,len))
				x_BE=np.zeros((2,len))
				x_BF=np.zeros((2,len))
				x_CA=np.zeros((2,len))
				x_DA=np.zeros((2,len))
				x_EA=np.zeros((2,len))
				x_FA=np.zeros((2,len))
				for i in range(len):
		
					temp1=A+lam_1[i]*(B-A)
					x_AB[:,i]=temp1.T
					temp2=B+lam_1[i]*(C-B)
					x_BC[:,i]=temp2.T
					temp3=C+lam_1[i]*(A-C)
					x_CA[:,i]=temp3.T
					temp4=D+lam_1[i]*(A-D)
					x_DA[:,i]=temp4.T
					temp5=E+lam_1[i]*(A-E)
					x_EA[:,i]=temp5.T
					temp6=F+lam_1[i]*(A-F)
					x_FA[:,i]=temp6.T
					temp7=B+lam_1[i]*(D-B)
					x_BD[:,i]=temp7.T
					temp8=B+lam_1[i]*(E-B)
					x_BE[:,i]=temp8.T
					temp9=B+lam_1[i]*(F-B)
					x_BF[:,i]=temp9.T
					temp10=P+lam_1[i]*(Q-P)
					x_PQ[:,i]=temp10.T
					temp11=U+lam_1[i]*(V-U)
					x_UV[:,i]=temp11.T
					
			
		
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_BD[0,:],x_BD[1,:],label='$BD$')
plt.plot(x_BE[0,:],x_BE[1,:],label='$BE$')
plt.plot(x_BF[0,:],x_BF[1,:],label='$BF$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_DA[0,:],x_DA[1,:],label='$DA$')
plt.plot(x_EA[0,:],x_EA[1,:],label='$EA$')
plt.plot(x_FA[0,:],x_FA[1,:],label='$FA$')
plt.plot(x_PQ[0,:],x_PQ[1,:],label='$PQ$')
plt.plot(x_UV[0,:],x_UV[1,:],label='$UV$')

plt.plot(A[0],A[1],'o')
plt.text(A[0]*1.1,A[1]*1.1,'A')
plt.plot(B[0],B[1],'o')
plt.text(B[0]*1.1,B[1]*1.1,'B')
plt.plot(C[0],C[1],'o')
plt.text(C[0]*1.1,C[1]*1.1,'C')
plt.plot(D[0],D[1],'o')
plt.text(D[0]*1.1,D[1]*1.1,'D')
plt.plot(E[0],E[1],'o')
plt.text(E[0]*1.1,E[1]*1.1,'E')
plt.plot(F[0],F[1],'o')
plt.text(F[0]*1.1,F[1]*1.1,'F')
plt.plot(P[0],P[1],'o')
plt.text(P[0]*1.1,P[1]*1.1,'P')
plt.plot(Q[0],Q[1],'o')
plt.text(Q[0]*1.1,Q[1]*1.1,'Q')
plt.plot(U[0],U[1],'o')
plt.text(U[0]*1.1,U[1]*1.1,'U')
plt.plot(V[0],V[1],'o')
plt.text(V[0]*1.1,V[1]*1.1,'V')

plt.xlabel('$x$')
plt.xlabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.show()



