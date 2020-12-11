import unittest


def alignment(a, b, isGlobal=True):
    if isGlobal:
        return alignment_function(a, b, f_needleman_wunsch)
    else:
        return alignment_function(a, b, f_smith_waterman)


def alignment_function(a, b, f):
    sa = len(a)+1
    sb = len(b)+1

    # initialize score
    score = [(-float('inf'), (0, 0)) for _x in range(0, sa*sb)]
    score[0] = (0, (0, 0))

    for pos in range(1, sb*sa):
        i = pos % sa
        j = int(pos / sa)

        ti = i - 1
        if ti < 0:
            ti = 0
        tj = j - 1
        if tj < 0:
            tj = 0

        s = -2
        if a[ti] == b[tj] and i > 0 and j > 0:
            s = 2
        elif a[ti] != b[tj] and i > 0 and j > 0:
            s = -1

        score[sa*j + i] = f(sa, sb, i, j, s, score)

    ra = []
    rb = []
    rs = -float('inf')

    ta = sa - 1
    tb = sb - 1

    while score[tb * sa + ta][1] != (0, 0):
        f = score[tb * sa + ta]

        fa = f[1][1]
        fb = f[1][0]
        fs = f[0]
        
        if fa == -1:
            ra.append(a[ta-1])
        else:
            ra.append(None)
        if fb == -1:
            rb.append(b[tb-1])
        else:
            rb.append(None)

        ta = ta + fa
        tb = tb + fb
        rs = max(rs, fs)

    return (rs, ra[::-1], rb[::-1])


def f_needleman_wunsch(sa, sb, i, j, s, score):
    assert len(score) == sa*sb
    assert i < sa and j < sb

    f1 = (-float('inf'), (-1, -1))
    if i > 0 and j > 0:
        f1 = (score[sa*(j-1) + (i-1)][0] + s, (-1, -1))

    f2 = (-float('inf'), (0, -1))
    if i > 0:
        f2 = (score[sa*(j) + (i-1)][0] - 2, (0, -1))

    f3 = (-float('inf'), (-1, 0))
    if j > 0:
        f3 = (score[sa*(j-1) + (i)][0] - 2, (-1, 0))
    
    f = f1
    if f1[0] < f2[0]:
        if f2[0] < f3[0]:
            f = f3
        else:
            f = f2
    elif f1[0] < f3[0]:
        f = f3
    else:
        f = f1

    return f


def f_smith_waterman(sa, sb, i, j, s, score):
    assert len(score) == sa*sb
    assert i < sa and j < sb

    f1 = (-float('inf'), (-1, -1))
    if i > 1 and j > 1:
        ts = score[sa*(j-1) + (i-1)][0] + s
        f1 = (max(0, ts), (-1, -1))
    f2 = (-float('inf'), (0, -1))
    if i > 1:
        ts = score[sa*(j) + (i-1)][0] - 2
        f2 = (max(0, ts), (0, -1))
    f3 = (-float('inf'), (-1, 0))
    if j > 1:
        ts = score[sa*(j-1) + (i)][0] - 2
        f3 = (max(0, ts), (-1, 0))
    
    f = f1
    if f1[0] < f2[0]:
        if f2[0] < f3[0]:
            f = f3
        else:
            f = f2
    elif f1[0] < f3[0]:
        f = f3
    else:
        f = f1

    return f


class TestAlignment(unittest.TestCase):

    def test_local_alignment():
        # test data
        a = 'ACCACGATGCATGCTATTAGCTAGCCGAT'
        b = 'AAGCAAGCCTGTCATTAGCTAGCCGGA'
        r = alignment(a, b, False)
        
        # expect
        ea = 'ACCACGAAGCATGCTTTTTCGCTAGCCGAT'
        eb = 'A--AGCAAGCATGTCATCAAGCTAGCCGGA'
        es = 6

        # actual
        ra = ''.join(map(lambda n: n if n  else '-', r[1]))
        rb = ''.join(map(lambda n: n if n  else '-', r[2]))
        rs = r[0]

        self.assertEqual(ea, ra)
        self.assertEqual(eb, rb)
        self.assertEqual(es, rs)

    def test_global_alignment():
        # test data
        a = 'ATTGC'
        b = 'ATGC'
        r = alignment(a, b)
        
        # expect
        ea = 'ATTGC'
        eb = 'A-TGC'
        es = 6

        # actual
        ra = ''.join(map(lambda n: n if n  else '-', r[1]))
        rb = ''.join(map(lambda n: n if n  else '-', r[2]))
        rs = r[0]

        self.assertEqual(ea, ra)
        self.assertEqual(eb, rb)
        self.assertEqual(es, rs)


if __name__ == '__main__':
    unittest.main()

