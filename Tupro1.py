"""
TugasPemrograman1
1. Arda Ardiansyah
2. Arliyanna Nilla
"""
import random
import math

# perhitungan fungsi
def fungsi(x,y):
    return (math.cos(x) + math.sin(y)) / x**2 + y**2

# decode kromosom 
def decode(kromosom):
    hasildecode = []
    hasildecode.append(-1 + ((2-(-1))/ (math.pow(2,-1)+math.pow(2,-2)+math.pow(2,-3)+math.pow(2,-4)+math.pow(2,-5))*( (kromosom[0]*math.pow(2,-1))+(kromosom[1]*math.pow(2,-2))+(kromosom[2]*math.pow(2,-3))+(kromosom[3]*math.pow(2,-4))+(kromosom[4]*math.pow(2,-5)))))
    hasildecode.append(-1 + ((1-(-1))/(math.pow(2,-1)+math.pow(2,-2)+math.pow(2,-3)+math.pow(2,-4)+math.pow(2,-5))*( (kromosom[5]*math.pow(2,-1))+(kromosom[6]*math.pow(2,-2))+(kromosom[7]*math.pow(2,-3))+(kromosom[8]*math.pow(2,-4))+(kromosom[9]*math.pow(2,-5)))))
    return hasildecode

# crossover
def Crossover(parent1, parent2):
    ank1 = []
    ank2 = []
    n = random.randint(1,10)
    for i in range(n):
        ank1.append(parent1[i])
        ank2.append(parent2[i])
    while(n<10):
        ank1.append(parent2[n])
        ank2.append(parent1[n])
        n+=1
    return ank1, ank2

# mutasi anak dengan probabilitas mutasi anak 10%
def mutasi(ank):
    ank3 = ank[:]
    for i in range(10):
        n = random.uniform(0, 1)
        if (n < 0.1):
            if (ank3[i] == 0):
                ank3[i] = 1
            else:
                ank3[i] = 0
    return ank3

def Regenerasi(ortuLama,ortuBaru,Popfitness,Popf):
    index = CariIndeksMinfitnes(Popf)
    idx = CariIndeksMaxfitnes(Popfitness)
    ortuLama[index] = ortuBaru[idx]
    index2 = CariIndeksMinfitnes(Popf)
    idx2 = CariIndeksMaxfitnes(Popfitness)
    ortuLama[index2] = ortuBaru[idx2]
    return ortuLama

# Membuat populasi
def buatpopulasiK(pjg):
    populasi = []
    for i in range(pjg):
        kromosom = []
        for j in range(10):
            kromosom.append(random.randint(0, 1))
        populasi.append(kromosom)
    return populasi

# Membuat populasi fitness 
def PopulasiFitnes(populasi):
    PopulasiFitnes = []
    for i in range(len(populasi)):
        j = decode(populasi[i])
        PopulasiFitnes.insert(i,fungsi(j[0],j[1]))
    return PopulasiFitnes

def seleksitour(populasi,fitnes):
    pop = populasi[:]
    fit = fitnes[:] 
    ortu = []
    for i in range(len(fit)): 
        min_idx = i 
        for j in range(i+1, len(fit)): 
            if fit[min_idx] > fit[j]: 
                min_idx = j        
        fit[i], fit[min_idx] = fit[min_idx], fit[i]
        pop[i], pop[min_idx] = pop[min_idx], pop[i]
    for i in range(populasi // 2):
        ortu.append(pop[i])
    return ortu

# Mencari Nilai maksimum
def CariIndeksMaxfitnes(fitnes):
    indeks = 0
    for i in range(len(fitnes)):
        if (fitnes[i] > fitnes[indeks]):
            indeks = i
    return indeks

#Mencari nilai minimum
def CariIndeksMinfitnes(Popfitnes):
    indeks = 0
    for i in range(len(Popfitnes) ):
        if (Popfitnes[i] < Popfitnes[indeks]):
            indeks = i
    return indeks
