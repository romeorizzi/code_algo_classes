#!/usr/bin/python

def num_parentheses(n_pairs):
  """
  ritorna il numero di formule ben formate (FBF) di n_pairs coppie di parentesi '(' e ')', dove n_pairs è il parametro in input
  """
  assert n_pairs >= 0
  if n_pairs == 0:
    return 1
#  if n_pairs == 1:
#    return 1
  risp = 0 
  for guess_res_size in range(n_pairs):
    risp += num_parentheses(n_pairs-guess_res_size-1) *num_parentheses(guess_res_size)
  return risp


def list_parentheses(n_pairs):
  """
  lista tutte formule ben formate (FBF) di n_pairs coppie di parentesi '(' e ')', dove n_pairs è il parametro in input
  """
  assert n_pairs >= 0
  if n_pairs == 0:
    yield ""
  else:
    for guess_res_size in range(n_pairs):
      for boss_choice in list_parentheses(n_pairs - guess_res_size - 1):
        for fairy_choice in list_parentheses(guess_res_size):
          #print(f"{guess_res_size=}, {boss_choice=}, {fairy_choice=}")
          yield f"({boss_choice}){fairy_choice}"


n_pairs = int(input("n_pairs="))
print(f"Ecco la lista delle {num_parentheses(n_pairs)=} FBS possibili:")
for fbf in list_parentheses(n_pairs):
  print(fbf)


  
def num_parentheses_ver2(ope,clo):
  """
  ritorna il numero di stringhe diverse, con <ope> caratteri '(' e <clo> caratteri ')', che siano suffissi di una qualche FBF.
  """
  #print(f"called num_parentheses_ver2({ope},{clo})")
  assert clo >= ope >= 0
  if ope == 0:
    return 1
  if ope == clo:
    return num_parentheses_ver2(ope-1,clo)
  return num_parentheses_ver2(ope-1,clo) + num_parentheses_ver2(ope,clo-1)

for n in range(10):
  assert num_parentheses_ver2(n,n) == num_parentheses(n)

"""
ESERCIZI SUGGERITI:
1. provate ad ottenere un algoritmo che lista tutte le FBF poggiando sulla struttura ricorsiva evidenziata in num_parentheses_ver2.
2. implementare rank e unrank secondo l'ordinamento determinato da list_parentheses
"""



