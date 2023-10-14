def remove_candidates_by_implicit_certainty(candidates, arr):
    digits_with_only_2_candidates_in_submat = {}
    for digit in range(1, 10):
        for (smr, smc), cells in candidates[digit].items():
            if len(cells) == 2:
                cands = digits_with_only_2_candidates_in_submat.get((smr, smc))
                if not cands:
                    digits_with_only_2_candidates_in_submat[(smr, smc)] = []
                digits_with_only_2_candidates_in_submat[(smr, smc)].append(digit)

    submats_with_2d_2c = {k: v for k, v in digits_with_only_2_candidates_in_submat.items() if len(v) == 2}

    for (smr, smc), digits in submats_with_2d_2c.items():
        first_digit_cands = candidates[digits[0]][smr, smc]
        second_digit_cands = candidates[digits[1]][smr, smc]
        if set(first_digit_cands) == set(second_digit_cands):
            for cell in first_digit_cands:
                for digit in range(1, 10):
                    if digit not in digits \
                            and (smr, smc) in candidates[digit] \
                            and cell in candidates[digit][(smr, smc)]:
                        print(f"removing -->  {cell} from {digit=}, {(smr, smc)=}")
                        candidates[digit][(smr, smc)].remove(cell)
                        if len(candidates[digit][(smr, smc)]) == 1:
                            arr[cell[0], cell[1]] = digit
                            print(f"updated{cell=}, {digit}")
    print(f"{digits_with_only_2_candidates_in_submat=}")
