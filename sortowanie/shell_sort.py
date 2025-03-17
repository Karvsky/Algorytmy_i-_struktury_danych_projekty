def shell_sort(n):

    def sedgewick_gaps(x):
        gaps = [1]
        k = 0
        while True:
            gap = 4**(k + 1) + 3 * 2**k + 1
            if gap >= x:
                break
            gaps.append(gap)
            k += 1
        gaps = gaps[::-1]
        return gaps

    gaps = sedgewick_gaps(len(n))

    for gap in gaps:
            for i in range(gap, len(n)):
                temp = n[i]
                j = i
                while j >= gap and n[j - gap] > temp:
                    n[j] = n[j - gap]
                    j -= gap
                n[j] = temp
    return n


