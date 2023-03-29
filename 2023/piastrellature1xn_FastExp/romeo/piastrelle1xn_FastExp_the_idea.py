#!/usr/bin/python

"""
Consider:
V(n) = [Fib(n+1), Fib(n)]', for n==0,...

Then:
V(n+1) = [Fib(n+2), Fib(n+1)]'
       = [Fib(n+1)+Fib(n), Fib(n+1)]
       = M * [Fib(n+1), Fib(n)]'
       = M * V(n), for n=0,...
where
M = [ [1,1], [1,0] ]

Base case: V(0) = [Fib(1), Fib(0)]' = [1, 1]'
Recursive computation involved:
V(n) = M * V(n-1) = M^2 * V(n-2) = ... = M^n * V(0)
Final Answer: V(n-1)[0] = (M^(n-1) * V(0))[0] = (M^(n-1) * [1, 1]')[0] = M^(n-1)[0][0] + M^(n-1)[0][1], for every n >= 2
An equivalent but simpler form for the final answer: M^n[0][0], for every n >= 1 

The true problem is hence how to compute M^{n-1} the fastest possible, which leads us to fast matrix exponentiation.
"""
M = [ [1,1], [1,0] ]


def num_piastrellature(N):
  assert N >= 0
  if N <= 1:
    return 1
  M_to_power_of_N = fastMatPow(M,N)
  return M_to_power_of_N[0][0]

def slowMatPow(M,N):
  """just for fast prototyping and checking"""
  assert N >= 1
  assert len(M) == len(M[0]) # M should be a square matrix
  if N==1:
    return M
  else:
    return matMult(M,slowMatPow(M,N-1))

def matMult(A,B):
  m = len(A)
  n = len(A[0])
  assert n == len(B)
  p = len(B[0])
  C = [ [None] * n for _ in range(p)]
  for i in range(n):
    for j in range(p):
      C[i][j] = sum([A[i][q]*B[q][j] for q in range(n)])
  return C


def fastMatPow(M,N):
  """TO DO: implement fast matrix exponentiation, that is, the idea here below"""
  return slowMatPow(M,N) # just for fast prototyping and checking

N = int(input("n="))
print(f"Le piastrellature di un bagno 1x{N} sono {num_piastrellature(N)}.")


"""
IDEA ALLA BASE DI FAST EXPONENTIATION:
assumiamo per partire che l'esponente N, sia una potenza di 2, ossia N=2^n:

M^1 = M
M^2 = M^1 * M^1
M^4 = M^2 * M^2
M^8 = M^4 * M^4
...
M^N = M^(N/2) * M^(N/2)

Quindi solo n=log N fasi di cui il costo è per altro:

O(1) + O(2) + O(4) + ... + O(N/2) + O(N) = O(N)

Consideriamo ora il caso generale in cui N non è una potenza di 2. Tuttavia, sarà una somma di potenze di due, giusto?

Ad esempio N = 72

N_0 = 0    36
N_1 = 0    18
N_2 = 0     9
N_3 = 1     4
N_4 = 0     2
N_5 = 0     1
N_6 = 1

72 =  1*2^6 + 1*2^3 = 64 + 8


M^72 come calcolarlo?

M^1 -> M^2 -> M^4 -> M^8 -> M^16 -> M^32 -> M^64
                      *                       *

M^(72) = M(64 + 8) = M^(64) * M(8)
osservazione:
1. al più n=log N prodotti per calcolare M^72 sfruttanto le M^(2^bit)
2. dal punto di vista asintotico il costo dell'ultimo e più costoso prodotto domina tutti gli altri (serie geometrica)
"""

