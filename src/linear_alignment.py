from copy import deepcopy

from candidate_cells_for_digit import row_neighbors, col_neighbors


def remove_candidates_from_neighboring_submats(row_col_coord, candidates, remove_from, digit, row_or_col):
    for (smr, smc) in remove_from:
        if (smr, smc) in candidates[digit]:
            cells = deepcopy(candidates[digit][(smr, smc)])
            for c in cells:
                if c[row_or_col] == row_col_coord:
                    candidates[digit][(smr, smc)].remove(c)
                    # print(f"Removing for {digit} --> {c}")


def remove_candidates_impacted_by_linear_alignment(candidates):
    for digit in range(1, 10):
        # if digit == 9:
        #     print('9 case')
        for (smr, smc), cells in candidates[digit].items():
            if 1 < len(cells) <= 3:
                row_coords = [c[0] for c in cells]
                f_cell_row_copies = [row_coords[0] for _ in range(len(row_coords))]
                if f_cell_row_copies == row_coords:
                    remove_from = row_neighbors(smr, smc)
                    remove_candidates_from_neighboring_submats(row_coords[0], candidates, remove_from, digit, 0)

                col_coords = [c[1] for c in cells]
                f_cell_col_copies = [col_coords[1] for _ in range(len(col_coords))]
                if f_cell_col_copies == col_coords:
                    remove_from = col_neighbors(smr, smc)
                    remove_candidates_from_neighboring_submats(col_coords[0], candidates, remove_from, digit, 1)

            # print(f'{(smr, smc)=}')
