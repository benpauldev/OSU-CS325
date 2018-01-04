def load_file(fname):
    with open(fname) as inf:
        data = [[int(i) for i in line.split()] for line in inf]
    return data

# mergeSort algorithm sourced and modified from interactivepython.org

def mergeSort(row):
    
    if len(row)>1:
        mid = len(row)//2
        lefthalf = row[:mid]
        righthalf = row[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                row[k]=lefthalf[i]
                i=i+1
            else:
                row[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            row[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            row[k]=righthalf[j]
            j=j+1
            k=k+1
    return row


def save_file(fname,data):
    with open(fname,"w") as outf:
        lines = [" ".join(str(i) for i in row) for row in data]
        outf.write("\n".join(lines))

def main():
    data = load_file("data.txt")
    data = [mergeSort(row[1:]) for row in data]
    save_file("merge.out", data)

main()