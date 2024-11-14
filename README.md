# Análise Experimental com Ajuste Linear de Dados

Este repositório contém um código em Python para a análise de dados experimentais com visualização em gráfico e ajuste linear utilizando o Método dos Mínimos Quadrados. A aplicação visa facilitar a visualização e o ajuste de dados experimentais, fornecendo uma interpretação gráfica para uma relação linear entre duas variáveis.

## Descrição do Código

O código faz o seguinte:

1. **Entrada dos Dados Experimentais**: Os dados experimentais são definidos nas variáveis `eixo_X` e `eixo_Y`. Neste exemplo, `eixo_X` representa valores de posição (em cm) e `eixo_Y` representa o tempo médio (em segundos) correspondente. Esses valores podem ser substituídos pelos dados reais do seu experimento.
   
2. **Plotagem do Gráfico**:
   - O gráfico é criado com a biblioteca `matplotlib`.
   - Os pontos experimentais são exibidos com marcadores circulares conectados por uma linha (`'o-'`), facilitando a visualização dos dados.
   
3. **Ajuste Linear (Método dos Mínimos Quadrados)**:
   - Um ajuste linear é realizado com o uso da função `np.polyfit`, gerando uma linha que representa a tendência dos dados.
   - A linha de ajuste é adicionada ao gráfico e exibida em vermelho tracejado (`'--'`), com a equação do ajuste linear formatada diretamente no gráfico.

4. **Anotação dos Dados**:
   - Cada ponto de dados é anotado diretamente no gráfico para facilitar a identificação dos valores individuais.

5. **Configurações Gráficas**:
   - O gráfico é configurado com título, rótulos para os eixos, grade e legenda para uma visualização mais compreensiva.

## Como Usar

1. Substitua os valores de `eixo_X` e `eixo_Y` pelos dados reais do seu experimento.
2. Execute o script. O gráfico exibirá os dados experimentais e o ajuste linear, além de anotar cada ponto para facilitar a interpretação.

## Requisitos

- Python 3.x
- Bibliotecas `numpy` e `matplotlib`

Para instalar as dependências, execute:
```bash
pip install numpy matplotlib
