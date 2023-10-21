from copy import deepcopy

import numpy as np


def candidate_cells_for_digit(arr):
    candidates = {}
    for digit in range(1, 10):
        candidates[digit] = {
            (smr, smc): blanks(smr, smc, arr, digit)
            for smr in range(3) for smc in range(3)
            if blanks(smr, smc, arr, digit)
        }
    return candidates


def blanks(smr, smc, arr, digit):
    return [
        (r, c)
        for r in range(smr * 3, smr * 3 + 3)
        for c in range(smc * 3, smc * 3 + 3)
        if not (
                arr[r, c]
                or
                digit_present_in_submat(arr, digit, smc, smr)
                or digit in arr[r, :]
                or digit in arr[:, c]
        )
    ]


def digit_present_in_submat(arr, digit, smc, smr):
    return digit in arr[smr * 3: smr * 3 + 3, smc * 3: smc * 3 + 3]


def smrow_and_smcol(smr, smc):
    sm_row = row_neighbors(smr, smc)
    sm_col = col_neighbors(smr, smc)
    return list(set(sm_row + sm_col))


def col_neighbors(smr, smc):
    sm_col = [(j, smc) for j in range(3) if j != smr]
    return sm_col


def row_neighbors(smr, smc):
    sm_row = [(smr, i) for i in range(3) if i != smc]
    return sm_row


def update_with_candidate_cells_for_digit_method(arr, candidates):
    for digit in range(1, 10):
        to_be_popped = []
        for (smr, smc), cells in candidates[digit].items():
            cells_copy = deepcopy(cells)
            v_and_h_submats = smrow_and_smcol(smr, smc)
            cells_r, cells_c = [], []
            for (can_sm_r, can_sm_c) in v_and_h_submats:
                candidate_submat = arr[can_sm_r * 3:can_sm_r * 3 + 3, can_sm_c * 3:can_sm_c * 3 + 3]
                if digit in candidate_submat:
                    d_sm_r, d_sm_c = np.where(candidate_submat == digit)
                    d_sm_r, d_sm_c = d_sm_r[0], d_sm_c[0]
                    d_r, d_c = can_sm_r * 3 + d_sm_r, can_sm_c * 3 + d_sm_c
                    if can_sm_r == smr:
                        row_cells_to_remove = [cell for cell in cells_copy if cell[0] == d_r]
                        for cell in row_cells_to_remove:
                            cells_copy.remove(cell)

                    if can_sm_c == smc:
                        col_cells_to_remove = [cell for cell in cells_copy if cell[1] == d_c]
                        for cell in col_cells_to_remove:
                            cells_copy.remove(cell)

            candidates[digit][(smr, smc)] = cells_copy

            if len(cells_copy) == 1:
                cell_row_index = cells_copy[0][0]
                cell_column_index = cells_copy[0][1]

                arr[cell_row_index, cell_column_index] = digit
                to_be_popped.append((smr, smc))

        for (smr, smc) in to_be_popped:
            candidates[digit].pop((smr, smc))
