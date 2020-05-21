class Graph:
    def __init__(self, v):
        self.V = v  # numarul de varfuri
        self.muchii = []  # muchiile sunt memorate in matrice
        self.parinte = [i for i in range(v)]  # fiecare element pointeaza spre el insusi
        self.rang = [1 for i in range(v)]  # si are rangul 1
        self.cheapest = [-1 for i in range(v)]

    # functie ce adauga o muchie la graf, necesara pentru formarea acestuia
    def adaugamuchie(self, sursa, destinatie, cost):

        self.muchii.append([sursa, destinatie, cost])

    # functie ce gaseste multimea un unui element x
    # si returneaza radacina
    def gasestemultime(self, x):
        if self.parinte[x] == x:  # daca parintele este elementul insusi
            return x  # il returneaza
        self.parinte[x] = self.gasestemultime(self.parinte[x])  # apel recursiv pentru gasirea radacinii
        return self.parinte[x]  # returnarea acesteia, dupa gasire

    # conecteaza doua submultimi
    def uneste(self, x, y):

        xr = self.gasestemultime(x)
        yr = self.gasestemultime(y)
        if xr == yr:  # daca sunt deja in acelasi arbore
            return False  # returneaza fals si iese din functie, unirea nu mai e necesara

        if self.rang[xr] < self.rang[yr]:
            t = xr  # interschimb xr cu yr
            xr = yr
            yr = t

        self.parinte[yr] = xr  # conecteaza pe xr cu yr
        self.rang[xr] += self.rang[yr]
        return True  # returneaza true si iese din functie

    def arboreacoperireminima(self):

        f = open("dateoutkruskal.txt", "a")
        self.muchii = sorted(self.muchii, key=lambda p: p[2])
        ans = []
        for i in range(len(self.muchii)):
            sursa, destinatie, cost = self.muchii[i]
            if (self.uneste(sursa, destinatie)):
                ans.append([sursa, destinatie, cost])

        print("Muchiile din arborele de acoperie minima: \n")
        costtotal = 0
        for sursa, destinatie, cost in ans:
            costtotal += cost
            print("%d <--> %d, weight %d" % (sursa, destinatie, cost))

        f.write(str(costtotal) + "\n")  # scrie costul total in fisier
        f.close()
