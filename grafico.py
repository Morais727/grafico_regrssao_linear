import numpy as np
import matplotlib.pyplot as plt

# Dados experimentais (exemplo)
# Substitua esses valores pelos dados obtidos no seu experimento
eixo_X = np.array([10,20,30,40])  
eixo_Y = np.array([0.141, 0.285, 0.431, 0.573]) 

# Plotando o gráfico
plt.figure(figsize=(8, 6))
plt.plot(eixo_X, eixo_Y, 'o-', label='Dados experimentais')

# Ajuste linear pelo Método dos Mínimos Quadrados
coef = np.polyfit(eixo_X, eixo_Y, 1)
ajuste_linear = np.polyval(coef, eixo_X)

# Adicionando a linha de ajuste
plt.plot(eixo_X, ajuste_linear, '--', color='red', label=f'Ajuste Linear: y = {coef[0]:.4f}x + {coef[1]:.4f}')

for i in range(len(eixo_X)):
    plt.text(eixo_X[i], eixo_Y[i], f'({eixo_X[i]}, {eixo_Y[i]:.2f})',
    ha='left',
    bbox=dict(facecolor='blue', alpha=0.2))

# Configurando o gráfico
plt.title("Deslocamento x Tempo")
plt.xlabel("Posição (cm)")
plt.ylabel("Tempo médio (s)")
plt.legend()
plt.grid(True)

# Exibindo o gráfico
plt.show()
