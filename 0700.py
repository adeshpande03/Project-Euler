N = 1504170715041707
M = 4503599627370517
min = N
sum = N
def t_print(strings, lengths = []):
    lenStr = len(strings)
    lenLen = len(lengths)
    if lenLen < lenStr:
        lengths.extend(len(str(s)) for s in strings[lenLen:])
    print("".join(str(strings[i]).ljust(lengths[i]) for i in range(lenStr)))
t_print(["Eulercoin", "Sum"], [20])
print("-"*36)
t_print([min, sum], [20])
Nn = N
while Nn > 100000000:
    Nn = (Nn + N) % M
    if Nn < min:
        min = Nn
        sum += Nn
        t_print([min, sum], [20])
t_print(["","","<< end brute-force attack"], [20,18])        
t_print(["","","<< start tail analysis"], [20,18])
def modinv(a, n):
    t = 0
    newt = 1
    r = n
    newr = a

    while newr != 0:
        quotient = r // newr
        t, newt = newt, t - quotient * newt
        r, newr = newr, r - quotient * newr

    if r > 1:
        return "a is not invertible"
    if t < 0:
        t = t + n
        
    return t
invN = modinv(N, M)
n = (min * invN) % M 
dict = {}
for Nn in range(1, min):
    n1 = (Nn * invN) % M
    dict[n1] = Nn
for n, Nn in sorted(dict.items()):
    if Nn < min:
        min = Nn
        sum += Nn
        t_print([min, sum], [20])
        if Nn == 1:
            t_print([0, sum], [20])
            break
print()
print("Solution: ", sum)