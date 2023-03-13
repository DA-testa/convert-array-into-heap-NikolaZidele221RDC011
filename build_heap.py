# # python3
#
#
# def build_heap(n, data):
#     swaps = []
#
#     i = int(n/2)
#     while i > -1:
#         swaps, data = otrais(i, data, swaps, n)
#         i = i - 1
#     return swaps
#
#
# def otrais(i, data, swaps, n):
#     mazaka = i
#     pa_kreisi = 2*i + 1
#     if pa_kreisi <= int(n - 1) and data[pa_kreisi] < data[mazaka]:
#         mazaka = pa_kreisi
#     pa_labi = 2*i + 2
#     if pa_labi <= int(n - 1) and data[pa_labi] < data[mazaka]:
#         mazaka = pa_labi
#     if i != mazaka:
#         data[i], data[mazaka] = data[mazaka], data[i]
#         swaps.append((i, mazaka))
#         swaps, data = otrais(i, data, swaps, n)
#     return swaps, data
#
#
# def main():
#     letter = input("Enter I or F: ")
#     if letter == "I" or letter == "i":
#         n = int(input())
#         data = list(map(int, input().split()))
#         assert len(data) == n
#         swaps = build_heap(n, data)
#         print(len(swaps))
#         for k in swaps:
#             print(k[0], k[1])
#     elif letter == "F" or letter == "f":
#         file = input()
#         with open("./test/" + file, mode='r') as fails:
#             n = fails.readline()
#             data = fails.readline()
#             data = list(map(int, input().split()))
#             assert len(data) == n
#             swaps = build_heap(n, data)
#             print(len(swaps))
#             for k in swaps:
#                 print(k[0], k[1])
#     else:
#         print("Next time enter I or F first!")
#
#
# if __name__ == "__main__":
#     main()


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
    letter = input()
    if letter == "I":
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
        swaps = build_heap(n, data)
        print(len(swaps))
        for k in swaps:
            print(k[0], k[1])
    elif letter == "F":
        file = input()
        with open("./tests/" + file, mode='r') as fails:
            n = fails.readline()
            numbers = fails.readline()
            numbers = numbers.split()
            n = int(input())
            data = list(map(int, input().split()))
            assert len(data) == n
            swaps = build_heap(n, data)
            print(len(swaps))
            for k in swaps:
                print(k[0], k[1])
    # else:
    #     print("Next time enter I or F value!")


if __name__ == "__main__":
    main()
