from itertools import permutations


def main():
    f = [int(i) for i in open("./supplements/0059_cipher.txt").read().split(",")]
    l = permutations("abcdefghijklmnopqrstuvwxyz", 3)
    l = [list(map(ord, i)) for i in l]
    for key in l:
        s = ""
        for i in range(len(f)):
            s += chr(f[i] ^ key[i % 3])
        if " the " in s:
            print(sum([ord(i) for i in s]))
            break


main()
