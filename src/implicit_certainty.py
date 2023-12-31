from helper import dict_print, candidates_reverse, update_arr


def remove_candidates_by_implicit_certainty(candidates, arr):
    digits_with_candidates_in_submat = {}
    for digit in range(1, 10):
        for (smr, smc), cells in candidates[digit].items():
            cands = digits_with_candidates_in_submat.get((smr, smc))
            if not cands:
                digits_with_candidates_in_submat[(smr, smc)] = []
            digits_with_candidates_in_submat[(smr, smc)].append(digit)

    # dict_print(digits_with_candidates_in_submat)
    candidates_reversed = candidates_reverse(candidates)

    d_gangs = {}
    for (smr, smc), digits in candidates_reversed.items():
        d_gangs[(smr, smc)] = {}
        for d in digits:
            d_gang = [d]
            for d_2 in digits:
                if d != d_2 and set(candidates[d][(smr, smc)]) == set(candidates[d_2][(smr, smc)]):
                    d_gang.append(d_2)
            if len(d_gang) == len(candidates[d][(smr, smc)]):
                d_gangs[(smr, smc)][tuple(candidates[d][(smr, smc)])] = d_gang

    d_gangs = {k: v for k, v in d_gangs.items() if v}
    # dict_print(d_gangs)
    # dict_print(candidates_reversed)

    for (smr, smc), d_g in d_gangs.items():
        for cell_tuples, digits in d_g.items():
            a = set(digits)
            b = set(candidates_reversed[(smr, smc)])
            c = b - a
            # if smr == 0 and smc == 2:
            #     print(f"{c=}, {cell_tuples=}")
            for x in c:
                for ct in cell_tuples:
                    if ct in candidates[x][(smr, smc)]:
                        candidates[x][(smr, smc)].remove(ct)
