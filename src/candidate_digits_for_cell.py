def update_with_candidate_digits_for_cell_method(arr):
    for i in range(9):
        for j in range(9):
            if arr[i, j]:
                continue
            sub_mat_row_start = (i // 3) * 3
            sub_mat_col_start = (j // 3) * 3
            sub_mat = arr[sub_mat_row_start:sub_mat_row_start + 3, sub_mat_col_start:sub_mat_col_start + 3]
            sub_mat = sub_mat.flatten().tolist()
            known_vals = arr[i, :].tolist() + arr[:, j].tolist() + sub_mat
            # print(known_vals)
            known_vals = set(known_vals)
            missing = [x for x in range(9) if x not in known_vals]
            print(f"{i, j} -- {missing=}")
            if len(missing) == 1:
                print(f"updating {i, j}")
                arr[i, j] == missing[0]
