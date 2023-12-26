from euler_utils import generatePentagonalList
def main():
    pents = generatePentagonalList(10000)
    pset = set(pents)
    for i in range(len(pents)):
        for j in range(i, len(pents)):
            if pents[i] + pents[j] in pset and pents[j] - pents[i] in pset:
                print(pents[j] - pents[i])
                break
    

main()