
def combinations(L_combinations: list, L: list,  M: list, k: int) -> None:
    '''Set of combinations of k elements taken from list M.

    Arguments:
    ----------
    L_combinations : List which will contain
    the set of combinations of k elements taken in M.

    L : Combination list between 0 and k element of M,
    when we have iterated k times, L is copied in the list L_combinations.

    M : List which initially contains the elements to combine
    and which is purified by the elements already combined
    at each iteration of this recursive function.
    '''
    # if k greater than the number of elements of M
    if k > len(M):
        return
    elif k == 0:
        # Add L to L_combinations
        L_combinations.append(L)
    else:
        # for all the elements x of the set M
        for x in M:
            # List Next_element = the elements of M placed after x in L
            index_next_element_after_x = M.index(x) + 1
            Next_element = M[index_next_element_after_x:]
            # List L_update = L plus x (we concatenate x to list L)
            L_update = L.copy()
            L_update.append(x)
            # Iteration until "k-1 == 0"
            combinations (L_combinations, L_update, Next_element, k-1)
