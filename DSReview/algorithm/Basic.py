class Basic(object):
    @staticmethod
    def qsort(l):
        if len(l) == 0:
            return []
        return Basic.qsort([t for t in l[1:] if t < l[0]]) + [l[0]] + qsort([t for t in l[1:] if t >= l[0]])

    @staticmethod
    def select(l):
        for i in range(0, len(l)):
            min = i
            for j in range(i, len(l)):
                if l[min] > l[j]:
                    min = j
            l[i], l[min] = l[min], l[i]
        return l

    @staticmethod
    def bubble(l):
        for i in range(0, len(l)):
            for j in range(i, len(l)):
                if l[i] > l[j]:
                    l[i], l[j] = l[j], l[i]
        return l

    @staticmethod
    def __binsearch(l, n, left, right):
        if left > right:
            return -1
        if l[(left + right) / 2] > n:
            return Basic.__binsearch(l, n, 0, (left + right) / 2)
        elif l[(left + right) / 2] < n:
            return Basic.__binsearch(l, n, (left + right) / 2, right)
        else: 
            return (left + right) / 2
    @staticmethod
    def binsearch(l, n):
       Basic. __binsearch(l, n, 0, len(l))

    @staticmethod
    def __perm(l, i, n):
        if i == n:
            print l
        for j in range(i, n):
            l[i], l[j] = l[j], l[i]
            Basic.__perm(l, i + 1, n)
            l[i], l[j] = l[j], l[i]
    @staticmethod
    def perm(l):
       Basic.__perm(l,0 ,len(l))

    @staticmethod
    def __bool(l, i, n):
        if i == n:
            print l
            return
        Basic.__bool(l, i + 1, n)
        l[i] = False if l[i] is True else True
        Basic.__bool(l, i + 1, n)
    @staticmethod
    def bool(n):
        Basic.__bool([True for i in range(0, n)], 0, n)

    @staticmethod
    def strinsert(s, i, n):
        return s[0: n] + i + s[n: len(s)]


