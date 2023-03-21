#!/usr/bin/python

def num_piastrellature(n):
  assert n >= 0
  if n <= 1:
    return 1
  return num_piastrellature(n - 1) + num_piastrellature(n - 2)


def rank_piastrellatura(n, p):
  "restituisce il rank della piastrellatura p di un bagno di dimensione n"
  assert n >= 0
  assert len(p)==3*n
  if n==0:
    assert p == ""
    return 0;
  if n==1:
    assert p == "[-]"
    return 0;
  if p[:3] == "[-]":
    return rank_piastrellatura(n-1, p[3:]);
  elif p[:6] == "[----]":
    return num_piastrellature(n-1)+rank_piastrellatura(n-2, p[6:]);
  else:
    assert(False)

def unrank_piastrellatura(n, rank, history=""):
  "restituisce la piastrellatura di rango rank tra le piastrellature di un bagno di dimensione n, prefissata da history"
  assert n >= 0
  assert rank < num_piastrellature(n);
  if n == 0:
    print(history)
  elif n == 1:
    #print(history+"[-]");
    unrank_piastrellatura(n - 1, rank, history + "[-]")
  elif rank < num_piastrellature(n-1):
     unrank_piastrellatura(n - 1, rank, history + "[-]")
  else:
     unrank_piastrellatura(n - 2, rank-num_piastrellature(n-1), history + "[----]")


def list_piastrellature(n, history=""):
 """
  stampa le piastrellature di un bagno di dimensione n, ciascuna prefissata dal contenuto di history
 """
 assert n >= 0
 if n == 0:
  print(history)
 elif n == 1:
  #print(history+"[-]");
  list_piastrellature(n - 1, history + "[-]")
 else:
  list_piastrellature(n - 1, history + "[-]")
  list_piastrellature(n - 2, history + "[----]")


n = int(input("n="))
print(f"Ecco la lista delle {num_piastrellature(n)} piastrellature possibili:")
list_piastrellature(n)

print(f'{rank_piastrellatura(1, "[-]")=}');
print(f'{rank_piastrellatura(2, "[----]")=}');
print(f'{rank_piastrellatura(2, "[-][-]")=}');
print(f'{rank_piastrellatura(3, "[-][----]")=}');
print(f'{rank_piastrellatura(3, "[----][-]")=}');

print(f"Riotteniamo ora la lista delle {num_piastrellature(n)} piastrellature possibili utilizzando unrank:")
for r in range(num_piastrellature(n)):
  unrank_piastrellatura(n, r);
  
