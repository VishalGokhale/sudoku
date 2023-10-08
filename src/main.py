from copy import deepcopy

import numpy as np
import pandas as pd

from candidate_cells_for_digit import candidate_cells_for_digit, update_with_candidate_cells_for_digit_method, \
    row_neighbors
from candidate_digits_for_cell import update_with_candidate_digits_for_cell_method
from helper import read_input
from linear_alignment import remove_candidates_impacted_by_linear_alignment


def update_arr(arr, candidates):
    for digit in range(1, 10):
        for _, cells in candidates[digit].items():
            if len(cells) == 1:
                cell = cells[0]
                arr[cell[0], cell[1]] = digit


def remove_candidates_by_rows_columns(candidates, arr):
    for digit in range(1, 10):
        for (smr, smc), cells in candidates[digit].items():
            if digit == 3 and smr == 0 and smc == 2:
                print(f"{arr[8, 1]=}")
            for c in cells:
                # row_coord = c[0]
                other_cells_in_same_row = [x for x in cells if x[0] == c[0] and x[1] != c[1]]
                if not other_cells_in_same_row:
                    r_neighs = row_neighbors(smr, smc)
                    candidate_cells_neigh_sub_mat_in_same_row = []
                    for neigh in r_neighs:
                        if neigh in candidates[digit] and candidates[digit][neigh]:
                            candidate_cells_neigh_sub_mat_in_same_row += [x for x in candidates[digit][neigh] if
                                                                          x[0] == c[0]]
                    if candidate_cells_neigh_sub_mat_in_same_row:
                        continue
                    arr[c[0], c[1]] = digit


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
        remove_candidates_by_rows_columns(candidates, arr)

        if np.array_equal(arr_copy, arr):
            print(f"{iterations = } completed\n\nNo updates compared to previous state, exiting...")
            break
        iterations += 1
        candidates = candidate_cells_for_digit(arr)

    arr = np.where(arr == None, '', arr)
    output_df = pd.DataFrame(arr)
    print(output_df)
    # output_df.to_excel(r'output_int2.xlsx')
    # print(f"==========\n{arr}\n==============")
