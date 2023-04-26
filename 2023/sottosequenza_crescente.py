input_seq = [-1, 45, 23, 41, 32, 55, 22, 13, 57, 39, 77, 16, 15, 44, 18, 63, 54, 43, 38, 56, 38, 29, 41, 19, 73, 55, 86]

def num_feasible_solutions(pos_first = 1, pos_last_taken = 0):
    """ritorna il numero di sottosequenze cresenti di input_seq[pos_first:] con tutti gli elementi presi >= input_seq[pos_last_taken:]"""
    if len(input_seq[pos_first:]) == 0:
        return 1
    num_dont_take_first = num_feasible_solutions(pos_first + 1, pos_last_taken)
    if input_seq[pos_first] > input_seq[pos_last_taken]:
        num_take_first = num_feasible_solutions(pos_first + 1, pos_first)
    else:
        num_take_first = 0
    return num_dont_take_first + num_take_first

print(num_feasible_solutions())


def opt_val_of_feasible_solutions(pos_first = 1, pos_last_taken = 0):
    """ritorna la massima lunghezza di una sottosequenza cresente di input_seq[pos_first:], che abbia tutti gli elementi presi >= input_seq[pos_last_taken:]"""
    if len(input_seq[pos_first:]) == 0:
        return 0
    val_dont_take_first = opt_val_of_feasible_solutions(pos_first + 1, pos_last_taken)
    if input_seq[pos_first] > input_seq[pos_last_taken]:
        val_take_first = 1 + opt_val_of_feasible_solutions(pos_first + 1, pos_first)
    else:
        val_take_first = 0
    return max(val_dont_take_first, val_take_first)

print(opt_val_of_feasible_solutions())