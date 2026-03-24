# Comparação entre Métodos de Mitigação de Viés em Modelos de Aprendizagem de Máquina

**Alexcolman Apunike¹, Vinícius Sakamoto², Ricardo Ricci Lopes³**

Faculdade de Tecnologia de FATEC Ribeirão Preto (FATEC) — Ribeirão Preto, SP – Brasil

---

## Resumo

Modelos preditivos estão sujeitos a vieses presentes em todas as etapas do processo de aprendizagem, desde a coleta de dados, pelos algoritmos usados para treinar o modelo, até a validação feita por um ser humano. Devido ao crescente uso e presença de tais modelos, desde recomendações de vídeos até seleção de crédito para financiamento, assim, faz-se necessário métodos para identificar e mitigar tais vieses, tal necessidade resultou na insurgência de um novo campo de estudo, AI Fairness. O presente trabalho visa realizar um estudo comparativo entre métodos de mitigação de viés aplicados individualmente, também, comparando o impacto combinando os métodos.

**Palavras-chave:** Análise preditiva, algoritmos discriminatórios, aprendizagem de máquina, AI Fairness 360.

**Keywords:** Predictive analytics, discriminatory algorithms, machine learning, AI Fairness 360.

---

## 1. Introdução

O uso de sistemas inteligentes não é algo inédito, sendo utilizados há décadas para apoiar operadores de usinas elétricas (WONG, 1990), em trabalhos relacionados a contabilidade (O'LEARY; O'KEEFE, 1997), entre outras aplicações como detecção de fraudes, recomendações, etc. Tendo em vista que a qualidade de aprendizado de máquinas está sujeito a qualidade dos dados (HU, 2025), assim, um modelo que é treinado sobre um dataset enviesado resultará em respostas enviesadas, de tal maneira, tais sistemas podem acarretar em decisões errôneas e injustas. Por exemplo, Lambrecht e Tucker (2019) relatam sobre algoritmos que consideravam jovens mulheres como um grupo caro para entrega de propagandas sobre profissões nas áreas de ciências, tecnologia, engenharia e matemática (STEM fields); também, outro exemplo é o sistema Correctional Offender Management Profiling for Alternative Sanctions (COMPAS), sistema que avalia o risco de a pessoa ser reincidente em algum delito, que possui maiores taxas de falsos positivos para pessoas negras (MEHRABI et al, 2021).

Assim, métodos para mitigar vieses tornam-se uma necessidade, porém, a compreensão de que para mitigar tais vieses basta tratar o dataset é reducionista por não compreender que em alguns casos, especialmente casos envolvendo grupos sociais desfavorecidos, para identificar um viés deve-se ir além de tratamentos estatísticos, necessitando um olhar político, social, econômico, ecológico, etc., de forma que o problema de viés em aprendizado de máquinas não é normativamente distinto (HU, 2025). Essa compreensão, de que não é normativamente distinto, torna-se evidente quando compreende-se que vieses estão presentes em todas as etapas do processo de aprendizagem (MAVROGIORGOS et al, 2024), desde a coleta, ao processamento, até a análise dos resultados. Isso, pois a fonte de viés é a própria realidade e sociedade, sendo os dados apenas reflexos da sociedade (HU, 2025). De tal forma, a compreensão sobre viés é invariavelmente multidisciplinar e complexa, havendo definições ligeiramente diferentes entre os campos, porém, em vias gerais, é compreendido como um desvio sistemático da verdade (BUETER, 2022), especificamente na área de Fairness em aprendizado de máquina um viés pode ser compreendido como um modelo cujo resultados favorecem ou discriminam sistematicamente determinados grupos baseados em atributos sensíveis (MEHRABI et al, 2021).

Mesmo que vieses estejam presentes em todas as etapas do ciclo de vida de aprendizado de máquinas, os métodos de mitigação utilizados em AI Fairness se ocupam, majoritariamente, nas etapas adjacentes ao processamento. De tal forma, não cabe a tais métodos mitigar vieses decorrentes das etapas de coleta e de análise. Conforme posto por Mehrabi et al (2021) em sua revisão, os métodos podem ser categorizados em 3: pré-processamento, em processamento e pós-processamento. O primeiro método tenta remover os vieses transformando e modificando os dados de treinamento. Técnicas em processamento tentam remover viés durante o treinamento do modelo, alterando funções objetivo ou novas restrições aos modelos. O último método é utilizado quando os algoritmos usados para treinamento são tratados como caixa preta, sendo efetuado a mitigação após o treinamento fazendo uso de um conjunto de validação.

O presente trabalho visa comparar o impacto de diferentes métodos de mitigação de viés em pré-processamento da ferramenta proprietária da IBM AI Fairness 360, serão utilizados datasets com diferentes características para analisar o impacto desses métodos, sendo Random Forests o modelo base para treinamento.

---

## 2. Fundamentação Teórica

### 2.1. Viés

Como supracitado, a definição do conceito de viés diverge entre diferentes áreas, porém, mais precisamente, em equidade de aprendizado de máquina, viés pode ser identificado quando não há independência entre atributos sensíveis (S) e a predição (Y), de tal forma que um atributo sensível influencie na probabilidade de predição de um resultado. Essa independência é mensurada através de métricas de equidade.

### 2.2. Fairness

Assim como o conceito de viés é difícil de ser definido, o conceito de equidade (Fairness) também resvala em diferentes definições entre as distintas áreas do conhecimento. De maneira geral, equidade pode ser compreendida como a ausência de viés em aprendizado de máquinas.

### 2.3. Métricas de avaliação

A capacidade de generalização de um modelo é avaliada através de métricas que estão associadas com as taxas com que o modelo acerta ou erra. Essas métricas são particulares ao tipo de variável a ser avaliada, se contínua ou discreta, consequentemente, modelos de regressão e classificação, respectivamente.

#### 2.3.1. Métricas de classificação

Os modelos de classificação, especialmente os de classificação binária, são avaliados a partir da matriz de confusão, da qual se originam as métricas de classificação, mais especificamente as métricas de limiares.

A matriz de confusão compreende-se em colunas que representam as classes reais e as linhas as previstas. Assim, tem-se uma distribuição entre classificações cujas previsões representam a realidade, verdadeiras (TP e TN), e previsões equivocadas, falsas (FP e FN).

|  | Classe real positiva | Classe real negativa |
|---|---|---|
| **Classe prevista positiva** | Verdadeiro positivo (TP) | Falso positivo (FP) |
| **Classe prevista negativa** | Falso negativo (FN) | Verdadeiro negativo (TN) |

Operando sobre essas distribuições obtém-se métricas de limiares para avaliação de modelos classificatórios. As métricas devem ser avaliadas em conjunto e com o devido contexto, isso pois cada métrica avalia um aspecto do modelo, por exemplo, situações como a previsão de alguma doença exige uma maior sensibilidade à uma maior acurácia, tendo que falsos negativos são mais críticos que falsos positivos.

Além das métricas de limiares é comum o uso de métricas de ranqueamento, sendo as mais comuns as curvas de precisão-sensibilidade (PR) e a de característica de operação do receptor (ROC), ambas descrevem o desempenho do classificador se baseando sobre diversos limiares de decisão. A primeira avalia a compensação que o modelo apresenta entre precisão e sensibilidade sendo uma métrica mais conservadora ao considerar a compensação entre o quanto o modelo prevê como correto e o quanto acerta corretamente, o que demonstra a eficácia do modelo em identificar uma classe como positiva como correta em relação com a prevista erroneamente como positiva. Já a curva ROC descreve a compensação entre a taxa de falsos positivos e a sensibilidade, o quanto o modelo acerta corretamente para as classes positivas e o quanto erra para as classes verdadeiramente negativas, o que possibilita avaliar a capacidade de distinção entre as classes pelo modelo.

Através da representação gráfica é possível visualizar tal compensação, observando os extremos tem-se que na curva ROC o ideal reside na ordenada, quando a taxa de verdadeiros positivos é máxima e a taxa de falsos positivos é mínima enquanto que o diametralmente oposto indica que o modelo alerta incondicionalmente positivos. Através da curva PR identifica-se que o ideal reside sobre o ponto (1, 1) no qual o modelo é capaz de prever corretamente as classes positivas, porém o comportamento típico da curva é decrescente, de forma que quanto maior a sensibilidade menor a precisão, isso porque ao ajustar o modelo para ser mais leniente com o limiar de decisão (maior sensibilidade) o modelo acusará mais facilmente uma classe como positiva com menos rigor, se o modelo for mais rigoroso há menos falsos positivos, porém, haverá mais falsos negativos.

**Principais métricas para avaliação de modelos classificatórios:**

| Métrica | Fórmula | Descrição |
|---|---|---|
| Acurácia | \(\frac{TP + TN}{TP + FP + TN + FN}\) | Taxa de previsões corretas sobre todas as instâncias. |
| Precisão | \(\frac{TP}{TP + FP}\) | Taxa de acerto de classes prevista como positiva. |
| Recall / Sensibilidade | \(\frac{TP}{TP + FN}\) | Taxa de acerto de classes verdadeiramente positivas. |
| Especificidade | \(\frac{TN}{FP + TN}\) | Taxa de acerto de classes verdadeiramente negativas. |
| Taxa de falsos positivos | \(\frac{FP}{FP + TN}\) | Taxa de erro de classes verdadeiramente negativas. |
| F1-Score | \(\frac{2}{recall^{-1} + precisão^{-1}}\) | Média harmônica entre recall e precisão. |

#### 2.3.2. Métricas de regressão

Embora o presente trabalho foque em problemas de classificação, é relevante notar que modelos de regressão — que buscam prever valores numéricos contínuos — demandam métricas distintas. Enquanto a classificação avalia a correção de rótulos, a regressão mensura a magnitude do erro por meio de métricas como o Erro Médio Absoluto (MAE), que indica a distância média entre a previsão e o valor real, e o Erro Quadrático Médio (MSE), que penaliza severamente desvios maiores (outliers). Tais métricas são fundamentais em contextos estatísticos de previsão de valores, mas diferem das métricas de classificação por não operarem sobre uma matriz de confusão ou limiares de decisão discretos.

**Principais métricas para modelos de regressão:**

| Métrica | Fórmula | Descrição |
|---|---|---|
| Erro Médio Absoluto (MAE) | \(\frac{\sum_{i=1}^{n} \|y_i - x_i\|}{n}\) | Distância média entre o valor previsto e o verdadeiro. Menos sensível a outliers. |
| Erro Quadrático Médio (MSE) | \(\frac{\sum_{i=1}^{n} (y_i - x_i)^2}{n}\) | Quadrado da distância média entre o valor previsto e o verdadeiro. Maior impacto de erros maiores. |
| Raiz do Erro Quadrático Médio (RMSE) | \(\sqrt{\frac{\sum_{i=1}^{n} (y_i - x_i)^2}{n}}\) | Raiz do MSE. Mesma unidade da variável alvo. |
| Coeficiente de Determinação (R²) | \(1 - \frac{\sum_{i=1}^{n} (y_i - x_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2}\) | Indica o quanto o modelo está ajustado com os valores reais. |

### 2.4. Métricas de equidade

\[P(Y = 1 \mid S = 0) = P(Y = 1 \mid S = 1)\]

Assim, para que um modelo seja justo as probabilidades de predição devem ser semelhantes entre os grupos.

- **Paridade Estatística (Equidade de Grupo)**
- **Predictive Parity (Outcome Test)**
- **False Positive Error Rate Balance (Predictive Equality)**
- **False Negative Error Rate Balance (Equal Opportunity)**
- **Equalized Odds**
- **Equalized Odds Difference**
- **Equal Opportunity Difference**
- **Disparate Impact**

### 2.5. Random Forests

O modelo base, Random Forest, é um classificador baseado em um conjunto de árvores de decisão que são treinadas com um subconjunto aleatório do dataset utilizando um subconjunto aleatório de atributos, sendo que cada árvore emite um voto para uma variável-alvo, sendo selecionado o voto majoritário (BREIMAN, 2001).

### 2.6. Métodos de mitigação em pré-processamento

Métodos em pré-processamento focam na qualidade dos dados.

#### 2.6.1. Reweighting

Reweighting é um método relativamente simples e não intrusivo no qual são aplicados pesos sobre as tuplas para tornar os atributos protegidos independentes estatisticamente da variável-alvo; um atributo protegido pode ser compreendido como qualquer característica inata ou adquirida cuja discriminação baseada sobre essas seja ilegal, como gênero e etnia, por exemplo (BAROCAS; HARDT; NARAYANAN, 2023). Conforme posto por Kamiran e Calders (2012), o peso é obtido através da proporção entre a probabilidade esperada, P_exp, e a observada, P_obs. Sendo a probabilidade dada pela frequência de tuplas contendo os atributos sensíveis no dataset, D. Assim:

\[P(S = b \wedge Class = +) := \frac{|\{X \in D \mid X(S) = b\}|}{|D|} \times \frac{|\{X \in D \mid X(Class) = +\}|}{|D|}\]

\[W(X) := \frac{P_{exp}(S = X(S) \wedge Class = X(Class))}{P_{obs}(S = X(S) \wedge Class = X(Class))}\]

#### 2.6.2. Disparate Impact Remover

*(Seção a ser desenvolvida)*

#### 2.6.3. Learning Fair Representations

*(Seção a ser desenvolvida)*

#### 2.6.4. Optimized Preprocessing

*(Seção a ser desenvolvida)*

---

## 3. Metodologia

A metodologia empregada neste trabalho é baseada sobre o modelo apresentado por Yip (2020) o qual descreve o ciclo de vida de aprendizado de máquinas em 7 etapas:

1. Coleta de dados
2. Preparação de dados
3. Seleção do modelo
4. Treinamento do modelo
5. Avaliação do modelo
6. Implantação do modelo
7. Monitoramento e manutenção

O presente estudo utilizará apenas as etapas 2 à 5, pois o intuito do trabalho é apenas avaliar o impacto dos métodos de mitigação sobre modelos de aprendizagem. Também, o dataset utilizado foi o Law School GPA, dataset canônico utilizado como referência para testar algoritmos de mitigação de viés. Como é um dataset de referência já embarcado com a ferramenta AI Fairness 360 não há coleta de dados.

### 3.1. Preparação de dados

*(Seção a ser desenvolvida)*

### 3.2. Seleção do modelo

*(Seção a ser desenvolvida)*

### 3.3. Treinamento do modelo

*(Seção a ser desenvolvida)*

### 3.4. Avaliação do modelo

*(Seção a ser desenvolvida)*

---

## 4. Resultados e Discussão

*(Seção a ser desenvolvida)*

---

## 5. Considerações Finais

*(Seção a ser desenvolvida)*

---

## Referências

1. WONG, Kit Po. Applications of artificial intelligence and expert systems in power engineering. *The Knowledge Engineering Review*, v. 5, n. 2, p. 127-140, 1990.
2. O'LEARY, Daniel E.; O'KEEFE, Robert M. The impact of artificial intelligence in accounting work: Expert systems use in auditing and tax. *AI & Society*, v. 11, n. 1, p. 36-47, 1997.
3. LAMBRECHT, Anja; TUCKER, Catherine. Algorithmic bias? An empirical study of apparent gender-based discrimination in the display of STEM career ads. *Management Science*, v. 65, n. 7, p. 2966-2981, 2019.
4. HU, Lily. What is new, and what is old, in fairness and machine learning. *ACM Journal on Responsible Computing*, 2025.
5. MAVROGIORGOS, Konstantinos et al. Bias in machine learning: A literature review. *Applied Sciences*, v. 14, n. 19, p. 8860, 2024.
6. MEHRABI, Ninareh et al. A survey on bias and fairness in machine learning. *ACM Computing Surveys (CSUR)*, v. 54, n. 6, p. 1-35, 2021.
7. BUETER, Anke. Bias as an epistemic notion. *Studies in History and Philosophy of Science*, v. 91, p. 307-315, 2022.
8. YIP, Wendy. Lifecycle of machine learning models. *Oracle*, Redwood Shores, 2020.
9. KAMIRAN, Faisal; CALDERS, Toon. Data preprocessing techniques for classification without discrimination. *Knowledge and Information Systems*, v. 33, n. 1, p. 1-33, 2012.
10. BAROCAS, Solon; HARDT, Moritz; NARAYANAN, Arvind. *Fairness and machine learning: Limitations and opportunities*. MIT Press, 2023.
11. BREIMAN, Leo. Random forests. *Machine Learning*, v. 45, n. 1, p. 5-32, 2001.
12. Law School Admissions Bar Passage Dataset. Disponível em: https://www.kaggle.com/datasets/danofer/law-school-admissions-bar-passage/data

### Possíveis referências adicionais

- RUBACK, L.; CARVALHO, D.; AVILA, S. Mitigando Vieses no Aprendizado de Máquina: Uma Análise Sociotécnica. *iSys-Brazilian Journal of Information Systems*, v. 15, n. 1, p. 23-1, 2022.
- BESSE, P.; DEL BARRIO, E.; GORDALIZA, P.; LOUBES, J. M.; RISSER, L. A survey of bias in machine learning through the prism of statistical parity. *The American Statistician*, v. 76, n. 2, p. 188-198, 2022.
- RAINIO, O.; TEUHO, J.; KLÉN, R. Evaluation metrics and statistical tests for machine learning. *Scientific Reports*, v. 14, 6086, 2024. https://doi.org/10.1038/s41598-024-56706-x
