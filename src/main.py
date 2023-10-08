from copy import deepcopy

import numpy as np

from candidate_cells_for_digit import candidate_cells_for_digit, update_with_candidate_cells_for_digit_method
from candidate_digits_for_cell import update_with_candidate_digits_for_cell_method
from helper import read_input

if __name__ == '__main__':
    arr = read_input()
    # print(candidates)

    iterations = 0
    candidates = candidate_cells_for_digit(arr)
    while True:
        arr_copy = deepcopy(arr)
        print(f'<<<<<<<<< {iterations} >>>>>>>>> ')
        update_with_candidate_digits_for_cell_method(arr)
        candidates = candidate_cells_for_digit(arr)
        update_with_candidate_cells_for_digit_method(arr, candidates)

        if np.array_equal(arr_copy, arr):
            print(f"{iterations = } completed\n\nNo updates compared to previous state, exiting...")
            break
        iterations += 1
        candidates = candidate_cells_for_digit(arr)

    print(arr)
