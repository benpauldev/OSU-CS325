def load_file(fname):
    with open(fname) as inf:
        data = [[int(i) for i in line.split()] for line in inf]
    return data

# insertionSort algorithm sourced and modified from interactivepython.org

def insertionSort(row):

    for i in range(0, len(row)):

         currentvalue = row[i]
         position = i


         while position>0 and row[position-1]>currentvalue:
             row[position]=row[position-1]
             position = position-1

         row[position]=currentvalue

    return row



def save_file(fname,data):
    with open(fname,"w") as outf:
        lines = [" ".join(str(i) for i in row) for row in data]
        outf.write("\n".join(lines))

def main():
    data = load_file("data.txt")
    data = [insertionSort(row[1:]) for row in data]
    save_file("insert.out", data)

main()




       


