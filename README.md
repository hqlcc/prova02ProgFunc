
# 📊 Prova Parcial II - Programação Funcional

**Disciplina**: Programação Funcional  
**Professor**: Prof. Dr. Antonio Marcos Selmini 
**Aluno**: Henrique S. Lecce

## 💻 Descrição

Este repositório contém as soluções dos três exercícios propostos na **Prova Parcial II**. Os problemas abordam conceitos de paralelismo com `ProcessPoolExecutor`, manipulação de listas e cálculos matemáticos intensivos, simulando cenários reais das áreas de meio ambiente, agronomia e biotecnologia.

---

## 🧪 Exercícios

### ✅ 1. Análise de Períodos de Calor Extremo

Simula séries temporais de temperaturas em diferentes regiões do país. Para cada região, identifica o maior número de dias consecutivos com temperatura superior a 40°C. A análise é realizada em paralelo.

---

### ✅ 2. Cálculo de Caminhos de Drones em Plantações

Calcula o número de rotas distintas que um drone pode seguir em uma plantação representada por uma grade `m x n`, movendo-se apenas para a direita ou para baixo. Executado em paralelo para diversas plantações.

---

### ✅ 3. Logaritmo de Fatoriais para Simulações Genéticas

Calcula `log10(n!)` para grandes valores de `n`, utilizando soma de logaritmos para evitar estouro de memória. Os cálculos são feitos em paralelo.

---

## ⚙️ Requisitos

- Python 3.10+
- Nenhuma biblioteca externa além da standard library

---

## 🚀 Execução

Cada exercício possui um arquivo `.py` separado. Execute com:

```bash
python3 ex.01.py
python3 ex.02.py
python3 ex.03.py
