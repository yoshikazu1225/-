N = int(input())

for i in range(9, -1, -1):
    wari = 2 ** i
    print((N // wari)%2, end="")