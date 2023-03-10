# n stands for counter
# vr stands for value
# s stands for sum
# c stands for condition

import math

def listMaker():
    n=input("How much elements your list will have:\t")
    n=int(n)
    n=round(n)
    if n<=0:
        print("Your list size is not supported")
        return

    lista=[]
    for i in range(0,n):
        k=input("Enter value:\t")
        lista.append(k)
    return lista
def counter(lista):
    n = 0
    for i in lista:
        n += 1
    return n

def cdCounter(cd):
    if cd < 1:
        cd *= 100
    if cd == 80:
        cd = 1.282
    elif cd == 85:
        cd = 1.440
    elif cd == 90:
        cd = 1.645
    elif cd == 95:
        cd = 1.960
    elif cd == 99:
        cd = 2.576
    elif cd == 99.5:
        cd = 2.807
    elif cd == 99.9:
        cd = 3.291
    else:
        print("Not supported value, we will work as if it was 95%")
        return 1.960
    return cd

def mean():
    lista = listMaker()
    s = 0
    n = counter(lista)
    for i in lista:
        s += i
    vr = s / n
    return vr

def median():
    lista = listMaker()
    print("elements of the list were\n", lista)
    print("elements of the list after sorting are")
    lista = sortGeneralAsc(lista)
    n = counter(lista)
    vr = 0
    if n % 2 == 0:
        n = (n + 1) / 2
        n = int(n)
        vr = lista[n]
    else:
        n = n / 2
        n = int(n)
        vr = lista[n]
    return vr

def mode():
    lista = listMaker()
    vr = 0
    for i in lista:
        vr2 = 0
        for j in lista:
            if i == j:
                vr2 += 1
                if vr2 > vr:
                    vr = vr2
                    trvr = i
    print(trvr, "appears ", vr, "times")
    return vr

def populationVariance():
    lista = listMaker()
    s = 0
    s1 = 0
    k = mean(lista)
    n = counter(lista)
    for i in lista:
        s1 = i - k
        s1 = math.pow(s1, 2)
        s += s1
    s = s / n
    return s

def populationStandardDeviation():
    lista = listMaker()
    vr = populationVariance(lista)
    vr = math.sqrt(vr)
    return vr

def sampleVariance():
    lista = listMaker()
    s = 0
    s1 = 0
    k = mean(lista)
    n = counter(lista)
    for i in lista:
        s1 = i - k
        s1 = math.pow(s1, 2)
        s += s1
    s = s / (n - 1)
    return s

def sampleStandardDeviation():
    lista = listMaker()
    vr = sampleVariance(lista)
    vr = math.sqrt(vr)
    return vr

def confidenceInterval(cd):
    lista = listMaker()
    cd = cdCounter(cd)
    x = mean(lista)
    n = counter(lista)
    st = sampleStandardDeviation(lista)
    x1 = x - cd * (st / math.sqrt(n))
    x2 = x + cd * (st / math.sqrt(n))
    vr = [x1, x2]
    return vr

def sortOneTimeAsc():
    lista = listMaker()
    n = counter(lista) - 1
    n1 = 0
    n2 = n1 + 1
    for i in lista:
        for j in lista:
            if n2 <= n:
                if lista[n1] > lista[n2]:
                    pom = lista[n1]
                    lista[n1] = lista[n2]
                    lista[n2] = pom
                n2 += 1
            n1 += 1
    print(lista)
    return lista

def sortMultiTimeAsc():
    lista = listMaker()
    n = counter(lista) - 1
    n1 = 0
    while n >= n1:
        sortOneTimeAsc(lista)
        n1 += 1
    return lista

def sortGeneralAsc():
    lista = listMaker()
    c = counter(lista) - 1
    c1 = 0
    while c >= c1:

        n = counter(lista) - 1
        n1 = 0
        n2 = n1 + 1
        for i in lista:
            for j in lista:
                if n2 <= n:
                    if lista[n1] > lista[n2]:
                        pom = lista[n1]
                        lista[n1] = lista[n2]
                        lista[n2] = pom
                    n2 += 1
                n1 += 1

        c1 += 1
    print(lista)
    return lista

def sortOneTimeDesc():
    lista = listMaker()
    n = counter(lista) - 1
    n1 = 0
    n2 = n1 + 1
    for i in lista:
        for j in lista:
            if n2 <= n:
                if lista[n1] < lista[n2]:
                    pom = lista[n1]
                    lista[n1] = lista[n2]
                    lista[n2] = pom
                n2 += 1
            n1 += 1
    print(lista)
    return lista

def sortMultiTimeDesc():
    lista = listMaker()
    n = counter(lista) - 1
    n1 = 0
    while n >= n1:
        sortOneTimeDesc(lista)
        n1 += 1
    return lista

def sortGeneralDesc():
    lista = listMaker()
    c = counter(lista) - 1
    c1 = 0
    while c >= c1:

        n = counter(lista) - 1
        n1 = 0
        n2 = n1 + 1
        for i in lista:
            for j in lista:
                if n2 <= n:
                    if lista[n1] < lista[n2]:
                        pom = lista[n1]
                        lista[n1] = lista[n2]
                        lista[n2] = pom
                    n2 += 1
                n1 += 1

        c1 += 1
    print(lista)
    return lista

def StandardError():
    lista = listMaker()
    n = counter(lista)
    st = sampleStandardDeviation(lista)
    vr = st / (math.sqrt(n))
    return vr

def marginOfError(cd):
    lista = listMaker()
    n = counter(lista)
    st = populationStandardDeviation(lista)
    cd = cdCounter(cd)
    vr = cd * (st / (math.sqrt(n)))
    return vr

def quartile25():
    lista = listMaker()
    lista=sortGeneralAsc(lista)
    n=counter(lista)
    p=(n+1)/4
    Q1=0
    if p%1==0:
        p=int(p)-1
        Q1=lista[p]
    else:
        p1 = int(p)
        p2 = p1 - 1
        Q1 = (lista[p2] + lista[p1]) / 2
    return Q1
def quartile50():
    lista = listMaker()
    lista = sortGeneralAsc(lista)
    n = counter(lista)
    p = (n + 1) / 2
    Q2 = 0
    if p % 1 == 0:
        p = int(p) - 1
        Q2 = lista[p]
    else:
        p1 = int(p)
        p2 = p1 - 1
        Q2 = (lista[p2] + lista[p1]) / 2
    return Q2
def quartile75():
    lista = listMaker()
    lista = sortGeneralAsc(lista)
    n = counter(lista)
    p = (3*(n + 1)) / 4
    Q3 = 0
    if p % 1 == 0:
        p = int(p) - 1
        Q3 = lista[p]
        print(Q3)
    else:
        p1 = int(p)
        p2 = p1 - 1
        Q3 = (lista[p2] + lista[p1]) / 2
        print(Q3)
    return Q3

def IQR():
    lista = listMaker()
    Q1=quartile25(lista)
    Q3=quartile75(lista)
    vr=Q3-Q1
    return vr