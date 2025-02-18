import math
import random
import Tupro1 as GeneticAlgorithm

#jumlah generasi dan populasi
uk_gen = 100
uk_populasi = 10

#list populasi
populasi = GeneticAlgorithm.buatpopulasiK(uk_populasi)

#tempat populasi
Pfit = []
best = []

#mencari kromosom terbaik dari suatu gen
for i in range(uk_gen):
    #variable populasi baru
    new_p = []
    nfit = []

#membuat populasi
Pfit = GeneticAlgorithm.PopulasiFitnes(populasi)

#variabel kosong untuk menghitung saat melakukan meeting pool
j = 0

#mencari kromosom terbaik dari generasi saat ini
indeks = GeneticAlgorithm.CariIndeksMinfitnes(Pfit)

#mendecode kromosom terbaik
x = GeneticAlgorithm.decode(populasi[indeks])

#membuat nilai fitness dari kromosom terbaik
nilai = GeneticAlgorithm.fungsi(x[0], x[1])
print("=================================")
print("Terbaik Gen : ", populasi[indeks])
print("Nilai X : ", x[0])
print("Nilai Y : ", x[1])
print("Fitness : ", nilai)
print("==================================")

#membuat parent dan mating pool
#mengambil setengah dari jumlah populasi
parent = GeneticAlgorithm.seleksitour(populasi, Pfit)
best.append(nilai)

#mating pool
while (j < (uk_populasi // 2)):
    #probabilitas crossover
    if(random.uniform(0,1)<0.85):
        #crossover
        child0, child1 = GeneticAlgorithm.Crossover(parent[j], parent[j+1])
        #mutasi
        child0 = GeneticAlgorithm.mutasi(child0)
        child1 = GeneticAlgorithm.mutasi(child1)
        new_p.append(child0)
        new_p.append(child1)
    j = j + 2
nfit = GeneticAlgorithm.PopulasiFitnes(Pfit)
populasi = GeneticAlgorithm.Regenerasi(populasi, new_p, nfit, Pfit)

indeks = GeneticAlgorithm.CariIndeksMinfitnes(Pfit)
x = GeneticAlgorithm.decode(populasi[indeks])
nilai = GeneticAlgorithm.fungsi(x[0], x[1])
print("=====================================")
print("Kromosom terbaik : ", populasi[indeks])
print("Nilai X : ", x[0])
print("Nilai Y : ", x[1])
print("=====================================")
    
