def load_file(fname):
    with open(fname) as inf:
        data = [[int(i) for i in line.split()] for line in inf]
    return data

# stoogesort algorithm sourced and modified from ispycode.com

def stoogesort(L, i=0, j=None):
    if j is None:
        j = len(L) - 1
    if L[j] < L[i]:
        L[i], L[j] = L[j], L[i]
    if j - i > 1:
        t = (j - i + 1) // 3
        stoogesort(L, i, j - t)
        stoogesort(L, i + t, j)
        stoogesort(L, i, j - t)
    return L


def save_file(fname,data):
    with open(fname,"w") as outf:
        lines = [" ".join(str(i) for i in row) for row in data]
        outf.write("\n".join(lines))

def main():
    data = load_file("data.txt")
    data = [stoogesort(row[1:]) for row in data]
    save_file("stooge.out", data)

main()