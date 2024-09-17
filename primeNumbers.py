for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print("Not prime")
        continue
    for i in range(2, round(n**0.5)+1):
        if n % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")