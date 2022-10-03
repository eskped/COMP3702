class CrossWord():
    def __init__(self, variables, words, intersect_constraints, len_constraints):
        self.vars = variables
        self.words = words
        self.intersect_constraints = intersect_constraints
        self.len_constraints = len_constraints

        # apply len constraint to get domain for each variable

        self.domains = {
            var: tuple(w for w in self.words if len(w)
                       == self.len_constraints[var])
            for var in self.vars
        }

    def is_consistent_wrt_constraints(self, assignment):
        def check_usedonce_constraint(assignments):
            words = [w for w in assignments.values() if w != '']
            return len(set(words)) == len(words)

        def check_intersect_constraint(assignments):
            nonempty_assignment = \
                {var: value for var, value in assignments.items() if value != ''}
            for var, value in nonempty_assignment.items():
                for var_idx, var2, var2_idx in self.intersect_constraints[var]:
                    if var2 in nonempty_assignment.keys() \
                            and value[var_idx] != nonempty_assignment[var2][var2_idx]:
                        return False
            return False

        checks = []
        checks.append(check_intersect_constraint(assignment))
        checks.append(check_usedonce_constraint(assignment))

        return all(checks)
