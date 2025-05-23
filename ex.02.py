
from concurrent.futures import ProcessPoolExecutor
from typing import Tuple, List

def coeficienteBi(n: int, k: int) -> int:
    
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    if k > n - k:
        k = n - k
    resultado = 1
    for i in range(1, k + 1):
        resultado = resultado * (n - k + i) // i
    return resultado

def calcularCaminho(grade: Tuple[int, int]) -> Tuple[Tuple[int, int], int]:
    
    m, n = grade
    caminhos = coeficienteBi(m + n - 2, m - 1)
    return (m, n), caminhos

def main():
    
    grades: List[Tuple[int, int]] = []

    qtd = int(input("Quantas grades deseja processar? "))

    for i in range(qtd):
        
        print(f"\nInforme os dados da grade {i+1}:")
        m = int(input("  Número de linhas (m): "))
        n = int(input("  Número de colunas (n): "))
        grades.append((m, n))

    resultados = []
    with ProcessPoolExecutor() as executor:
        for resultado in executor.map(calcularCaminho, grades):
            resultados.append(resultado)

    print("Grade (m x n) | Caminhos Distintos")
    print("-" * 40)
    for (m, n), caminhos in resultados:
        print(f"{m} x {n} | {caminhos}")

if __name__ == "__main__":
    main()
