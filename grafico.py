import numpy as np
import matplotlib.pyplot as plt

# Dados experimentais (exemplo)
# Substitua esses valores pelos dados obtidos no seu experimento
h_alcool = np.array([10,20,30,40])  
densi_alcool = np.array([0.141, 0.285, 0.431, 0.573]) 

# Plotando o gráfico
plt.figure(figsize=(8, 6))
plt.plot(h_alcool, densi_alcool, 'o-', label='Dados experimentais')

# Ajuste linear pelo Método dos Mínimos Quadrados
coef = np.polyfit(h_alcool, densi_alcool, 1)
ajuste_linear = np.polyval(coef, h_alcool)

# Adicionando a linha de ajuste
plt.plot(h_alcool, ajuste_linear, '--', color='red', label=f'Ajuste Linear: y = {coef[0]:.4f}x + {coef[1]:.4f}')

for i in range(len(h_alcool)):
    plt.text(h_alcool[i], densi_alcool[i], f'({h_alcool[i]}, {densi_alcool[i]:.2f})',
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
