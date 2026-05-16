
Usar one hot encode (OHE) para treinamento, as categorias possuem baixa cardinalidade
e o modelo tende a lidar melhor com variáveis binárias ao invés de ordinais.

Checar o impacto de algumas variáveis sobre o modelo
    - male
    - fulltime
    - fam_inc

# FAZENDO

    - EDA
        ( matriz de correlação para identificar variáveis categoricas redundantes )
        ( matriz de correlação para identificar variáveis continuas redundantes )


# MONOGRAFIA PRINCIPAL

    [x] INTRODUÇÃO
        [x] justificar a mitigação de viés
            [x] histórico sobre uso de sistemas inteligentes
            [x] impacto econômico e social
        [x] viés
            [x] definição do conceito geral
            [x] definição do conceito específico
            [x] como o viés se origina
        [x] métodos de mitigação
            [x] o que são
            [x] como são categorizados
        [x] resumir projeto
            [x] o que será realizado

    [ ] FUNDAMENTAÇÃO TEÓRICA
        [ ] viés
            [ ] definir matematicamente (?)
            [ ] tipos de viés presentes 
            [ ] como o viés se manifesta nas etapas
        [ ] fairness
            [ ] definir atributos sensíveis
            [ ] definir fairness
        [ ] métricas padrões
            [ ] accuracy
        [ ] fairness Metrics
        [ ] Random Forests
        [ ] pré-processamento
            [ ] reweighting
            [ ] disparate Impact Remover
            [ ] learning Fair Representations
            [ ] optimized Preprocessing

    [ ] METODOLOGIA
        [ ] materiais e dependências utilizadas
        [ ] pipeline

    [ ] RESULTADOS E DISCUSSÃO
        [ ] EDA dos datasets
        [ ] métricas padrões
        [ ] fairness metrics

    [ ] CONCLUSÃO


# MONOGRAFIA SECUNDÁRIO
    [ ] VERIFICAR FORMATAÇÃO E ELEMENTOS OBRIGATÓRIOS (CAPA, SUMÁRIO, ETC.)


# EXPERIMENTO
    [ ] Encontrar datasets com características diferentes
        [ ] classes desbanlanceadas (poucas amostras p/ uma classe)
        [ ] representation bias (sub representação de um grupo)
        [ ] dataset com alta dimensionalidade
        [ ] dataset com baixa dimensionalidade
    [ ] EDA
        [ ] frequência relativa dos grupos (representation analysis)
        [ ] frequência relativa da variável alvo e do grupo (disparidade entre grupos, disparate impact, parity difference)
        [ ] matriz de correlação (proxy analysis)
        [ ] frequência de valores nulos e vazios
        [ ] variância de variáveis por grupo
    [ ] Pipeline
        [ ] ETL
        [ ] pré processamento
        [ ] treinar modelos
        [ ] cuspir métricas e gráficos




# TODO
   CLEAN DATA
       - REMOVE REDUNDANT VARIABLES
       - REMOVE COLINEAR VARIABLES
       - CHECK PROTECTED ATTRIBUTES DISTRIBUTION
       - TRANSFORM CATEGORIES INTO BINARY CATEGORIES

   MODULES 
       - ETL
       - METRICS
       - CHARTS
       - RF
       - RW+RF

   GLOBAL VARIABLES
