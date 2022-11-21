import math
import matplotlib.pyplot as plt
velocidade = float(input("Digite a Velocidade que o objeto foi lancado (m/s): "))
angulo = float(input("Digite o angulo que o objeto foi lancado: "))
anguloEmRadiano = (angulo*3.14)/180
vx = velocidade*math.cos(anguloEmRadiano)
vy = velocidade*math.sin(anguloEmRadiano)
tempoTotal = (2*vy)/9.8
tempoSubida = vy/9.8
alcance = vx*tempoTotal
alcanteInt = int(alcance)
alturaMaxima = 0+vy*tempoSubida-((9.8*(tempoSubida**2))/2)
x=0
verificador = False
while verificador==False:
    if(x<=alcance):
        x=x+1
    else:
        verificador = True
for x in range (x):
    y = x*math.tan(anguloEmRadiano) - ((9.8*(x**2))/(2*(velocidade**2)*(math.cos(anguloEmRadiano)**2)))
    plt.scatter(x,y)
    plt.pause(0.0001)
print("==============================================")
print("Dados do Movimento: ")
print(f'Tempo = {tempoTotal}s')
print("==============================================")
print(alturaMaxima)
print(alcance)
      #Tempo Total, Alcance, Tempo de Subida
plt.show()
