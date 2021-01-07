from typing import List


def find_max_matches(compatible: List[List[bool]]):
    """
    :param compatible:
    :return: all length 2 or 3 cycles in the Matrix.
    Note: that for every index i ,which represent couple i ( Donor + Recipient) obviously
    compatible[i][i] = False, otherwise the donor in this couple could donate to
    the recipient in this couple and they would not need any cycle. (you could say they
    have "Length 1 cycle" which is not interesting).
    >>> mat = [[False, True], # couple 0 can donate to couple 1
    ...       [True, False]] # couple 1 can donate to couple 0
    >>> res = find_max_matches(mat)
    >>> for c in res:
    ...     print(c)
    Length 2 cycle: 0->1 and 1->0
    Length 2 cycle: 1->0 and 0->1
    >>> mat = [[False, True, False],
    ...       [True, False, True],
    ...       [True, False, False]]
    >>> res = find_max_matches(mat)
    >>> for c in res:
    ...     print(c)
    Length 2 cycle: 0->1 and 1->0
    Length 2 cycle: 1->0 and 0->1
    Length 3 cycle: 1->2 and 2->0 and 0->1
    Length 3 cycle: 2->0 and 0->1 and 1->2
    """
    cycles = []
    for i in range(len(compatible)):
        for j in range(len(compatible[0])):
            if compatible[i][j] and compatible[j][i]:
                cycles.append("Length 2 cycle: " + str(i) + "->" + str(j) + " and " + str(j) + "->" + str(i))
            elif compatible[i][j]:
                for k in range(len(compatible[0])):
                    if compatible[j][k] and compatible[k][i]:
                        cycles.append("Length 3 cycle: " + str(i) + "->" + str(j) + " and " + str(j) + "->" + str(k)
                                      + " and " + str(k) + "->" + str(i))
    return cycles


if __name__ == "__main__":
    import doctest

    doctest.testmod()
