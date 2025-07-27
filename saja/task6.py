rows=int(input("enter number of rows"))
for i in range(rows):
    for s in range (rows-i):
        print(" ",end="")
    for g in range (i+1):
        print("* ",end="")
    print()