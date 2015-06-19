def seq_add(start, k, end):
    x = start
    countr = start
    while x + k <= end:
        x += k
        countr += x
    return countr



def fact(n):
    count = 1
    if n <= 0:
        return 0
    else:
        for x in range(0, n, 1):
            count += count * x
        return count

