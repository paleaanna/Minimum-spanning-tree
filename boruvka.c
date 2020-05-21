#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include "boruvka.h"
#include "declarati.h"
//functie ce gaseste multimea un unui element x
//si returneaza radacina
int GasesteMultime(int x)
{
    if(parinte[x] == x)//daca parintele este elementul insusi
    {
        return x;//il returneaza
    }
    parinte[x] = GasesteMultime(parinte[x]); //apel recursiv pentru gasirea radacinii
    return parinte[x];//returnarea acesteia, dupa gasire
}
//conecteaza doua submultimi
int Uneste (int x, int y)
 {
    int xr = GasesteMultime(x);
    int yr = GasesteMultime(y);
    if(xr == yr)//daca sunt deja in aceeasi arbore
    {
        return 0;//iese din functie, unirea nu mai e necesara, returnand valoarea 1
    }
    if(rang[xr] < rang[yr])
    {
        int t = xr;//interschimb xr cu yr
        xr = yr;
        yr = t;
    }
    parinte[yr] = xr;//conecteaza pe xr cu yr
    return 1;//daca unirea s-a putut realiza, returneaza valoarea 1
}
//functie ce gaseste arborele de acoperire minima
void ArboreAcoperireMinima(struct Graf* g)
{
    FILE *G;
    G = fopen("dateoutboruvka.txt", "a");//deschidere fisier pentru scriere/adaugare
    //variabilele primesc valorile corespunzatoare grafului dat
    int noduri = g -> V, muchii = g -> M;
    //creeaza un arbore independent pentru fiecare nod
    for(int i = 0; i < noduri; i++)
    {
        parinte[i] = i; //fiecare element pointeaza spre el insusi
        rang[i] = 1;  //si are rangul 1
        cheapest[i] = -1;
    }

    //numarul de arbori va fi egal cu cel al nodurilor
    int arbori = noduri, costtotal = 0;//intializeaza variabila costtotal la 0
    //la final, numarul de arbori va fi 1, arborele de acoperire minima

    //continua sa combine componente, pana cand toate sunt
    //combinate intr-un singur arbore
    while (arbori > 1)
    {
        //de fiecare data initializeaza vectorul cheapest
        for(int i = 0; i < noduri; i++)
        {
            cheapest[i] = -1;
        }
        for (int i = 0; i < muchii; i++)
        {
            int sursa = GasesteMultime(g -> muchie[i].sursa);
            int destinatie = GasesteMultime(g -> muchie[i].destinatie);

            //daca doua varfuri ale muchiei curente apartin aceleiasi multimi,
            if (sursa == destinatie)
            {
                continue; //muchia curenta este ignorata
            }

            //verificam daca  muchia curenta este mai apropiata de
            //muchia cu costul cel mai mic cost dintre sursa si destinatie
            if(cheapest[sursa] == -1 || g -> muchie[i].cost < g -> muchie[cheapest[sursa]].cost)
            {
             cheapest[sursa] = i;
            }
            if(cheapest[destinatie] == -1 || g -> muchie[i].cost < g -> muchie[cheapest[destinatie]].cost)
            {
                cheapest[destinatie] = i;
            }
        }
        //muchia cu costul cel mai mic selectata mai sus
        //se adauga la arborele de acoperire minima
        for(int i = 0; i < noduri; i++)
        {
            if (cheapest[i] == -1)
            {
                continue;
            }
            int sursa = GasesteMultime(g -> muchie[cheapest[i]].sursa);
            int destinatie = GasesteMultime(g -> muchie[cheapest[i]].destinatie);
            if(sursa == destinatie)
            {
                continue;
            }
            costtotal = costtotal+ g -> muchie[cheapest[i]].cost;
            printf("%d <---> %d, cost %d\n", g -> muchie[cheapest[i]].sursa, g -> muchie[cheapest[i]].destinatie, g -> muchie[cheapest[i]].cost);
            //uneste sursa cu destinatia si decsreste numarul de arbori
            Uneste(sursa, destinatie);
            arbori = arbori - 1;
        }
    }
    fprintf(G, "%d\n", costtotal);//scrie costul total in fisier
    return;
}

