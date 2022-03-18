def print_formatted(n):
    s=str(bin(n))
    l=len(s)-2
    for i in range(1,n+1):
        de=str(i)
        oc=str(oct(i))
        he=str(hex(i))
        bi=str(bin(i))
        print(de.rjust(l),oc[2:].rjust(l),(he[2:].upper()).rjust(l),bi[2:].rjust(l))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
