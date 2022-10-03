from env import CrossWord
from agent import arc_consistency, recursive_backtracking


def main():
    variables = ("1A", "2D", "3D", "4A", "5D", "6D", "7A", "8A")

    # Domain of all variables
    words = ("AFT", "ALE", "EEL", "HEEL", "HIKE", "HOSES", "KEEL", "KNOT",
             "LASER", "LEE", "LINE", "SAILS", "SHEET", "STEER", "TIE")

    # (1) intersect constraint
    intersect_constraints = {
        "1A": ((2, "2D", 0), (4, "3D", 0)),
        "2D": ((0, "1A", 2), (2, "4A", 1), (3, "7A", 0), (4, "8A", 2)),
        "3D": ((0, "1A", 4), (2, "4A", 3), (3, "7A", 2), (4, "8A", 4)),
        "4A": ((1, "2D", 2), (2, "5D", 0), (3, "3D", 2)),
        "5D": ((0, "4A", 2), (1, "7A", 1), (2, "8A", 3)),
        "6D": ((1, "8A", 0),),
        "7A": ((0, "2D", 3), (1, "5D", 1), (2, "3D", 3)),
        "8A": ((0, "6D", 1), (2, "2D", 4), (3, "5D", 2), (4, "3D", 4))}

    # (2) Length constraint
    len_constraints = {"1A": 5, "2D": 5, "3D": 5, "4A": 4,
                       "5D": 4, "6D": 3, "7A": 3, "8A": 5}

    # (3) used-once constraint
    # Will be captures in the env class

    env = CrossWord(variables, words, intersect_constraints, len_constraints)
    # print(env.domains)

    # init_assignments = {var: '' for var in variables}
    # assignments, n_expanded = recursive_backtracking(
    #     init_assignments, env, n_expanded=0)
    # print(f'assignments = {assignments}')
    # print(f'n_expanded/n_backtracking = {n_expanded}')

    print("revised: ", arc_consistency(env))


if __name__ == '__main__':
    main()
