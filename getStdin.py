# get unknown lines of stdin
n = 0
while True:
    try:
        string = input()
        n = n +1
        print("input"+str(n)+": "+string)
    except EOFError:
        break