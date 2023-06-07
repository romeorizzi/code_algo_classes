

# Per ogni elemento dell'array:
# 1) guardo il bit meno significativo dell'indice i dell'elemento, chiamo la sua posizione l
# 2) L'i-esimo elemento del fenwick avra' la somma dei suoi 2**l elementi precedenti

def query(F, x):
    sol = 0
    while x > 0:
        sol += F[x]
        x -= x & -x
    return sol


# Per eseguire un update su un elemento di indice i:
# 1) Trovare tutti gli elementi del fenwick che contengono l'elemento i-esimo
# 2) Fare l'update di questi elementi

def update(F, x, val):
    while x < len(F):
        F[x] += val
        x += x & -x



