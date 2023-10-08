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
    # submats = [(r, c) for r in range(3) for c in range(3)]
    for digit in range(1, 10):
        # print(f"\n\n=======  {digit}  =======\n")
        to_be_popped = []
        for (smr, smc), cells in candidates[digit].items():
            # print(f"submat: {(smr, smc)}    -->    candidate_{cells=}")
            cells_copy = deepcopy(cells)
            # cells_copy = []
            v_and_h_submats = smrow_and_smcol(smr, smc)
            # print(f"{smr, smc} --> {v_and_h_submats}")
            cells_r, cells_c = [], []
            for (can_sm_r, can_sm_c) in v_and_h_submats:
                candidate_submat = arr[can_sm_r * 3:can_sm_r * 3 + 3, can_sm_c * 3:can_sm_c * 3 + 3]
                # print(f'{(can_sm_r,can_sm_c)=} --> {candidate_submat=}')
                if digit in candidate_submat:
                    d_sm_r, d_sm_c = np.where(candidate_submat == digit)
                    d_sm_r, d_sm_c = d_sm_r[0], d_sm_c[0]
                    d_r, d_c = can_sm_r * 3 + d_sm_r, can_sm_c * 3 + d_sm_c
                    if can_sm_r == smr:
                        row_cells_to_remove = [cell for cell in cells_copy if cell[0] == d_r]
                        # print(f"{(can_sm_r, can_sm_c)=} --> {row_cells_to_remove=}")
                        for cell in row_cells_to_remove:
                            cells_copy.remove(cell)

                        # cells_r.append(row_cells_to_remove)

                    if can_sm_c == smc:
                        col_cells_to_remove = [cell for cell in cells_copy if cell[1] == d_c]
                        # print(f"{(can_sm_r, can_sm_c)=} --> {col_cells_to_remove=}")
                        for cell in col_cells_to_remove:
                            cells_copy.remove(cell)
                        # cells_c.append(col_cells_to_remove)
            # cells_r_copy = [cell for r in cells_r for cell in r]
            # cells_c_copy = [cell for c in cells_c for cell in c]
            # print(f"before {digit=} {(smr, smc)=} {cells_r_copy=}")
            # print(f"before {cells_r=} ::: {cells_c_copy=}")

            # cells_copy = list(set(cells_r_copy).intersection(set(cells_c_copy)))
            # print(f"after {cells_copy=}")

            candidates[digit][(smr, smc)] = cells_copy

            if len(cells_copy) == 1:
                cell_row_index = cells_copy[0][0]
                cell_column_index = cells_copy[0][1]

                arr[cell_row_index, cell_column_index] = digit
                to_be_popped.append((smr, smc))
                print(f"Updating {digit=} in {(smr, smc)=} at {(cell_row_index, cell_column_index)=}")

        for (smr, smc) in to_be_popped:
            candidates[digit].pop((smr, smc))

            # cells
