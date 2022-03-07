n=int(input("Enter a number to print it's square multipication table "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i*j,end="")
    print()
