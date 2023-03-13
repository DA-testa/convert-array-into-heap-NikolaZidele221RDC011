# python3



def build_heap(n, data):
    swaps = []
    # size = (n - 1)
    i = int(n/2)
    while i > -1:
        swaps, data = otrais(i, data, swaps, n)
        i = i - 1
    return swaps


def otrais(i, data, swaps, n):
    mazaka = i
    pa_kreisi = 2* i + 1
    if pa_kreisi <= int(n - 1) and data[pa_kreisi] < data[mazaka]:
        mazaka = pa_kreisi
    pa_labi = 2 * i + 2
    if pa_labi <= int(n - 1) and data[pa_labi] < data[mazaka]:
        mazaka = pa_labi
    if i != mazaka:
        data[i], data[mazaka] = data[mazaka], data[i]
        swaps.append((i, mazaka))
        swaps, data = otrais(mazaka, data, swaps, n)
    return swaps, data





def main():
    letter = input("Enter letter I or F: ")
    if letter == "I" or letter == "i":
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
        swaps = build_heap(n, data)
        print(len(swaps))
        for k in swaps:
            print(k[0], k[1])
    elif letter == "F" or letter == "f":
        file = input()
        with open("./tests/" + file, mode='r') as fails:
            viss = fails.read()
            dala = viss.splitlines()
            n = int(dala[0])
            numbers = dala[1]
            data = list(map(int, numbers.split()))
            assert len(data) == n
            swaps = build_heap(n, data)
            print(len(swaps))
            for k in swaps:
                print(k[0], k[1])


if __name__ == "__main__":
    main()
