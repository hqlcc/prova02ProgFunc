
#📊 Prova Parcial II - Programação Funcional
Disciplina: Programação Funcional
Professor: Prof. Dr. Antonio Marcos Selmini
Aluno: Henrique S. Lecce

##💻 Descrição
Este repositório contém as soluções dos três exercícios propostos na Prova Parcial II. Os problemas abordam conceitos de paralelismo com ProcessPoolExecutor, manipulação de listas e cálculos matemáticos intensivos, simulando cenários reais das áreas de meio ambiente, agronomia e biotecnologia.

##🧪 Exercícios
###✅ 1. Análise de Períodos de Calor Extremo
Simula séries temporais de temperaturas em diferentes regiões do país. Para cada região, identifica o maior número de dias consecutivos com temperatura superior a 40°C. A análise é realizada de forma paralela.

####📂 Arquivo: onda_calor.py

####💡 Técnicas: random, ProcessPoolExecutor, listas

####🧠 Conceito: Paralelismo em análise climática

###✅ 2. Cálculo de Caminhos de Drones em Plantações
Calcula o número de rotas distintas que um drone pode seguir em uma plantação representada por uma grade m x n, movendo-se apenas para a direita ou para baixo. Executado em paralelo para diversas plantações.

####📂 Arquivo: caminhos_drones.py

####📐 Entrada: Lista de tamanhos de grids

####💡 Técnicas: Programação dinâmica, combinatória, math.comb, ProcessPoolExecutor

###✅ 3. Logaritmo de Fatoriais para Simulações Genéticas
Calcula log10(n!) para grandes valores de n, otimizando a memória com soma de logaritmos. Executado de forma paralela.

####📂 Arquivo: log_fatorial.py

####🔢 Entrada: [5000, 10000, 15000, 20000]

####💡 Técnicas: math.log10, ProcessPoolExecutor, precisão numérica

###📄 Licença
Este projeto é destinado unicamente para fins acadêmicos.