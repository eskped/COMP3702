from itertools import product
 
def cartesian_product(A, B):
    return list(product(A, B))

set1 = set( {0,1,2,3,4})
set2 = set( {'a', 'b', 'c', 'd', 'e'} )

# print(cartesian_product(set1, set2))

from itertools import chain, combinations


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


print(len(list(powerset(("abdce")))))