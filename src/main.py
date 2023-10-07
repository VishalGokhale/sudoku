from candidate_cells_for_digit import candidate_cells_for_digit
from candidate_digits_for_cell import update_with_candidate_digits_for_cell_method
from helper import read_input

if __name__ == '__main__':
    arr = read_input()
    candidates = candidate_cells_for_digit(arr)
    print(candidates)

    # for digit in range(1,10):
    #     for (smr,smc) in candidates[digit]:

    iterations = 0
    while iterations < 2:
        iterations += 1
        update_with_candidate_digits_for_cell_method(arr)

    # print(arr)
