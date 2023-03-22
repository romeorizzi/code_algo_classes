#!/usr/bin/python


def num_piastrellature2xn(n):
  """
  ritorna il numero di piastrellature di un bagno 2xn, dove n è il parametro in input
  """
  #print(f"called num_piastrellature2xn({n})")
  assert n >= 0
  if n == 0:
    return 1
  if n == 1:
    return 2
  risp = num_piastrellature2xn(n-2)
  for guess in range(1,n+1):
    risp += 2*num_piastrellature2xn(n-guess)
  return risp

n = int(input("n="))
print(f"Le piastrellature possibili sono: {num_piastrellature2xn(n)}")

# SECONDA VERSIONE (CON ESERCITO DI API, BOMBI E VESPE):

def num_piastrellature2xn_ver2(n):
  """
  ritorna il numero di piastrellature di un bagno 2xn, dove n è il parametro in input
  """
  #print(f"called num_piastrellature2xn_ver2({n})")
  assert n >= 0
  if n == 0:
    return 1
  if n == 1:
    return 2
  return num_piastrellature2xn_ver2(n-1) + num_piastrellature2xn_sbec1(n) + num_piastrellature2xn_sbec2(n) 

def num_piastrellature2xn_sbec2(n):
  """
  ritorna il numero di piastrellature di un bagno 2xn cui è stata rimossa una cella d'angolo e la sua adiacente sulla stessa riga (bagno 2-sbecchettato)
  """
  #print(f"called num_piastrellature2xn_sbec2({n})")
  assert n >= 2
  return num_piastrellature2xn_ver2(n-2) + num_piastrellature2xn_sbec1(n-1)

def num_piastrellature2xn_sbec1(n):
  """
  ritorna il numero di piastrellature di un bagno 2xn cui è stata rimossa una cella d'angolo (bagno sbecchettato)
  """
  #print(f"called num_piastrellature2xn_sbec1({n})")
  assert n >= 1
  if n == 1:
    return 1
  return num_piastrellature2xn_ver2(n-1) + num_piastrellature2xn_sbec1(n-1)


for n in range(10):
  assert num_piastrellature2xn_ver2(n) == num_piastrellature2xn(n)


