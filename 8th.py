def sequeance():
    sequeance = []
    a,b = 0,1
    for i in range(10):
        sequeance.append(a)
        a,b = b,a+b
    return sequeance

print(sequeance())