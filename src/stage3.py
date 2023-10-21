from candidate_cells_for_digit import row_neighbors, col_neighbors


def remove_candidates_by_rows(candidates, arr):
    for digit in range(1, 10):
        for (smr, smc), cells in candidates[digit].items():
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


def remove_candidates_by_cols(candidates, arr):
    for digit in range(1, 10):
        for (smr, smc), cells in candidates[digit].items():
            for c in cells:
                # row_coord = c[0]
                other_cells_in_same_col = [x for x in cells if x[1] == c[1] and x[0] != c[0]]
                if not other_cells_in_same_col:
                    c_neighs = col_neighbors(smr, smc)
                    candidate_cells_neigh_sub_mat_in_same_col = []
                    for neigh in c_neighs:
                        if neigh in candidates[digit] and candidates[digit][neigh]:
                            candidate_cells_neigh_sub_mat_in_same_col += [x for x in candidates[digit][neigh] if
                                                                          x[1] == c[1]]
                    if candidate_cells_neigh_sub_mat_in_same_col:
                        continue
                    arr[c[0], c[1]] = digit
