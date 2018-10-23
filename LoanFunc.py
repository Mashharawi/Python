# P = L[i(1 + i/12)m]/[(1 + i/12)m - 1]
def mortgage(L,r,m):
    P = (L * (r / 12 *(1+ r / 12)**m)) / ((1 + r / 12)**m - 1)
    return P
