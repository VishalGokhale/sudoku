from copy import deepcopy

import numpy as np
import pandas as pd

from candidate_cells_for_digit import candidate_cells_for_digit, update_with_candidate_cells_for_digit_method
from candidate_digits_for_cell import update_with_candidate_digits_for_cell_method
from helper import read_input
from linear_alignment import remove_candidates_impacted_by_linear_alignment
from stage3 import remove_candidates_by_rows, remove_candidates_by_cols


def update_arr(arr, candidates):
    for digit in range(1, 10):
        for _, cells in candidates[digit].items():
            if len(cells) == 1:
                cell = cells[0]
                arr[cell[0], cell[1]] = digit


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
        remove_candidates_impacted_by_linear_alignment(candidates)
        update_arr(arr, candidates)
        candidates = candidate_cells_for_digit(arr)
        remove_candidates_by_rows(candidates, arr)
        candidates = candidate_cells_for_digit(arr)
        remove_candidates_by_cols(candidates, arr)


        if np.array_equal(arr_copy, arr):
            print(f"{iterations = } completed\n\nNo updates compared to previous state, exiting...")
            break
        iterations += 1
        candidates = candidate_cells_for_digit(arr)

    arr = np.where(arr == None, '', arr)
    output_df = pd.DataFrame(arr)
    print(output_df)
    output_df.to_excel(r'output_very hard-partial.xlsx')
    # print(f"==========\n{arr}\n==============")
