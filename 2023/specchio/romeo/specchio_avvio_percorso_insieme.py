#!/usr/bin/python

string_in = list(map(int, input().strip().split()))
num_figli = string_in
print(f"{string_in=}")
print(f"{num_figli=}")
"""
voglio andare da:

4 2 0 3 0 0 1 0 0 0 0

a:

4 0 0 0 2 3 1 0 0 0 0

"""



lista_figli = []

"""
Step 1:

  voglio ora riempire la lista dei figli per ottenere:
lista_figli = [ [1, 8, 9, 10], [2, 3], [], [4, 5, 6], [], [], [7], [], [], [], [] ]

Step 2:
   la lista_figli offr euna rappresentazione dell'albero in input.
   Riusciamo a rovesciarlo?

Step 3:
   scrivere la codifica dell'albero rovesciato.
"""
 

"""
Step 1:
potrei partire con ...

for _ in string_in:
    ....

   ma sarebbe farsi del male!

anche quì è chiaro che un approccio ricorsivo paga.
"""

def riempi_lista_figli(pos_R = 0):
    pass  


"""
Step 2:

voglio andare da:
lista_figli = [ [1, 8, 9, 10], [2, 3], [], [4, 5, 6], [], [], [7], [], [], [], [] ]

a:

4 0 0 0 2 3 1 0 0 0 0
                                        0        1   2   3    4        5          6    7   8   9   10
lista_figli_albero_riflesso_A = [ [1, 2, 3, 4], [], [], [], [5, 10], [6 , 8, 9], [7], [], [], [], [] ]

lista_figli_albero_riflesso_B = [ [10, 9, 8, 1], [3, 2], [], [6, 5, 4], [], [], [7], [], [], [], [] ]

a:

4 0 0 0 2 3 1 0 0 0 0


"""

""" Step 3 (sotto ipotesi A): """


lista_figli_albero_riflesso_A = [ [1, 2, 3, 4], [], [], [], [5, 10], [6 , 8, 9], [7], [], [], [], [] ]

lista_figli_albero_riflesso_B = [ [10, 9, 8, 1], [3, 2], [], [6, 5, 4], [], [], [7], [], [], [], [] ]


def dfs_dichiara_anagrafe_A(adamo):
    num_figli_adamo = len(lista_figli_albero_riflesso_A[adamo])
    print(num_figli_adamo)
    for figlio in lista_figli_albero_riflesso_A[adamo]:
      dfs_dichiara_anagrafe_A(figlio)

dfs_dichiara_anagrafe_A(adamo = 0)

print()

def dfs_dichiara_anagrafe_B(adamo):
    num_figli_adamo = len(lista_figli_albero_riflesso_B[adamo])
    print(num_figli_adamo)
    for figlio in lista_figli_albero_riflesso_B[adamo]:
      dfs_dichiara_anagrafe_B(figlio)

dfs_dichiara_anagrafe_B(adamo = 0)


