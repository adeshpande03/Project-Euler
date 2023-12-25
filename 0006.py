def main():
    l = list(range(1, 101))
    print( -sum([i*i for i in l]) + sum(l)**2)
main()