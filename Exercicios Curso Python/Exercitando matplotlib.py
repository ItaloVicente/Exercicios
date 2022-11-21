import numpy as np
import matplotlib.pyplot as plt
P=[[4,5,6,7,8],[7,9,8,10,9]]
plt.scatter(P[0], P[1])
tam_P=len(P[0])
Xm=0
Ym=0
a=0
b=0
soma_prod_y_x=0
soma_da_dif_de_x_ao_quadrado=0
for i in range(tam_P):
   Xm=Xm+P[0][i]
   Ym=Ym+P[1][i]
Xm=Xm/tam_P
Ym=Ym/tam_P
for i in range(tam_P):
   soma_prod_y_x=soma_prod_y_x+(P[1][i]-Ym)*(P[0][i]-Xm)
   soma_da_dif_de_x_ao_quadrado=soma_da_dif_de_x_ao_quadrado+((P[0][i]-Xm)**2)
a=soma_prod_y_x/soma_da_dif_de_x_ao_quadrado
b=Ym - a*Xm
x_central_primeiro=min(P[0])
x_central_extremo=max(P[0])
y_central_primeiro=a*x_central_primeiro+b
y_central_extermo=a*x_central_extremo+b
x_reta_centro=np.linspace(x_central_primeiro,x_central_extremo,10)
y_reta_central=np.linspace(y_central_primeiro,y_central_extermo, 10)
plt.plot(x_reta_centro,y_reta_central, 'r')
plt.title("Figura da Questão 1")
plt.ylabel("y")
plt.xlabel("x")
plt.show()

