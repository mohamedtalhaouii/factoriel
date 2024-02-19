N = int(input("Entrer un nombre : "))
F = 1
if N == 0:
    print("Le Factoriel est: 1")
elif N > 0:
    for i in range(1,N+1):
        F = F * i
    print("Le factoriel de", N,"est:", F)