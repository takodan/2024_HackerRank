if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    height = len(arr)
    width = len(arr[0])
    max_sum = ""
    for i, e in enumerate(arr):
        hourglasses_sum = 0
        if i+2 == len(arr):
            # print("break")
            break
        for ii, ie in enumerate(e):
            if ii+2 == len(e):
                # print("break")
                break
            hourglasses_sum = ie+e[ii+1]+e[ii+2]+\
                arr[i+1][ii+1]+\
                arr[i+2][ii]+arr[i+2][ii+1]+arr[i+2][ii+2]
            # print(hourglasses_sum, max_sum)
            if max_sum == "":
                max_sum = hourglasses_sum
            if max_sum < hourglasses_sum:
                max_sum = hourglasses_sum
    print(max_sum)