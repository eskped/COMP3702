def arc_consistency(env):
    queue = [(v,) + c for v, clist in env.intersect_constraints.items()
             for c in clist]  # Line 3
    domains = env.domains.copy()
    while len(queue) != 0:
        v1, v1_idx, v2, v2_idx = queue.pop(0)  # Line 5
        revised, domains = revise(domains, v1, v1_idx, v2, v2_idx)  # Line 6
        if revised:  # Line 6
            if len(domains[v1]) == 0:  # Line 7
                return None  # Line 7
            # Line 8
            # Line 8
            for v1_idx_b, v2_2, v2_2_idx in env.intersect_constraints[v1]:
                if v2_2 == v2:
                    continue  # Line 8
                queue.append((v2_2, v2_2_idx, v1, v1_idx_b))  # Line 9

    return domains  # Line 10


def revise(domains, v1, v1_idx, v2, v2_idx):
    revised = False
    w_to_delete = []
    for w1 in domains[v1]:
        delete = True
        for w2 in domains[v2]:
            if w1[v1_idx] == w2[v2_idx]:
                delete = False
                break
        if delete:
            w_to_delete.append(w1)
            revised = True

    if revised:
        domains[v1] = [word for word in domains[v1] if word not in w_to_delete]

    return (revised, domains)


def recursive_backtracking(assignments, env, n_expanded):
    # Line 4 and 5 in pseudocode
    unassigned_var = None
    for var, value in assignments.items():
        if value == '':
            unassigned_var = var
            break
    if unassigned_var is None:
        return (assignments, n_expanded)

    for word in env.domains[unassigned_var]:  # line 6
        assignments[unassigned_var] = word  # Line 8

        if env.is_consistent_wrt_constraints(assignments):  # Line 7
            assignments_out, n_expanded = recursive_backtracking(
                assignments.copy(), env, n_expanded+1)  # Line 9

            if assignments_out is not None:
                return (assignments_out, n_expanded)  # Line 10

    # line 12
    return (None, n_expanded)
