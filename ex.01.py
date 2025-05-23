
import threading
from typing import List, Tuple

def maiorPeriodo(temperaturas: List[int]) -> int:
    
    maxPeriodo = 0
    periodo = 0
    for temp in temperaturas:
        
        if temp > 40:
            periodo += 1
            maxPeriodo = max(maxPeriodo, periodo)
        else:
            periodo = 0
    return maxPeriodo

def analiseRegiao(regiao: str, temperaturas: List[int], resultados: List[Tuple[str, int]]):
    
    periodo = maiorPeriodo(temperaturas)
    resultados.append((regiao, periodo))

def main():
    
    regioes = {
        
        "Norte":        [38, 41, 42, 39, 44, 45, 46, 30, 41],
        "Sul":          [35, 42, 43, 44, 30, 32, 45, 46, 47, 48, 39],
        "Sudeste":      [39, 41, 40, 40, 42, 43, 30, 29],
        "Centro-Oeste": [30, 31, 32, 45, 46, 47, 48, 49, 29],
        "Nordeste":     [44, 45, 46, 47, 48, 49, 40, 30, 29, 41, 42]
    }

    threads = []
    resultados = []

    for regiao, temperaturas in regioes.items():
        
        t = threading.Thread(target=analiseRegiao, args=(regiao, temperaturas, resultados))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Região | Maior período de calor ( Temp > 40°C)")
    print("-" * 50)
    for regiao, periodo in resultados:
        print(f"{regiao} | {periodo} dias")

if __name__ == "__main__":
    main()
