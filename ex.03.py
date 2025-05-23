
import math
from concurrent.futures import ProcessPoolExecutor

def logFatorial(n):
    
    logSoma = sum(math.log10(k) for k in range(1, n + 1))
    return (n, logSoma)

def main():

    numeros = [5000, 10000, 15000, 20000]

    with ProcessPoolExecutor() as executor:
        resultados = list(executor.map(logFatorial, numeros))

    print("n | log10(n!)")
    print("-" * 28)
    for n, log in sorted(resultados):
        print(f"{n} | {log:.4f}")

if __name__ == "__main__":
    main()
