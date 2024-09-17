if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    swaps_sum = 0
    for _ in a:
        swaps = 0
        i = 0
        while i < len(a)-1:
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swaps = swaps + 1
                swaps_sum = swaps_sum + 1
            i = i + 1
            # print(f"{a} r{i}, swaps{swaps}, swaps_sum{swaps_sum}")
        if swaps == 0:
            break

    print(f"Array is sorted in {swaps_sum} swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[-1])