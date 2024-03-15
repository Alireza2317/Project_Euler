from math import factorial

def combination(n: int, k: int) -> int:
    result = factorial(n) // (factorial(n-k)*factorial(k))
    return result
      

n: int = 20
answer: int = combination(n*2, n)
print(answer)
