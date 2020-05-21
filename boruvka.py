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

# functie ce gaseste arborele de acoperire minima
    def arboreacoperireminima(self):

        trees = self.V   # numarul arborilor este egal cu numarul varfurilor grafului
        costtotal = 0   # initalizeaza variabila costtotal la 0

        muchii = len(self.muchii)
        # combina submultimile, pana cand toate sunt
        # combinate intr-un singur arbore
        while trees > 1:
            for i in range(muchii):

                # cauta submultimi a doua colturi ale muchiei curente
                sursa, destinatie, cost = self.muchii[i]
                ur = self.gasestemultime(sursa)
                vr = self.gasestemultime(destinatie)
                # daca doua varfuri ale muchiei curente apartin aceleiasi multimi
                if ur == vr:
                    continue    # multimea curenta este ignorata
                # verificam daca muchia curenta este mai apropiata de
                # muchia cu costul cel mai mic din sursa si destinatie
                if self.cheapest[ur] == -1 or cost < self.muchii[self.cheapest[ur]][2]:
                    self.cheapest[ur] = i
                if self.cheapest[vr] == -1 or cost < self.muchii[self.cheapest[vr]][2]:
                    self.cheapest[vr] = i
            # muchia cu costul cel mai mic selectata mai sus
            # se adauga la arborele de acoprire minima
            for i in range(self.V):
                if self.cheapest[i] == -1:
                    continue
                im = self.cheapest[i]
                sursa = self.gasestemultime(self.muchii[im][0])
                destinatie = self.gasestemultime(self.muchii[im][1])

                if sursa == destinatie:
                    continue
                costtotal += self.muchii[im][2]
                # uneste sursa cu destinatia
                self.uneste(sursa, destinatie)
                print("%d <--> %d, cost %d" % (self.muchii[im][0], self.muchii[im][1], self.muchii[im][2]))
                trees -= 1  # scade numarul de arbori
            # de fiecare data, initializeaza vectorul cheapest
            self.cheapest = [-1 for i in range(self.V)]
        print("Costul total este: %d\n" % costtotal)