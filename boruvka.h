#ifndef CODE_BORUVKA_H
#define CODE_BORUVKA_H
#include"declarati.h"

 struct Muchie
{
    int sursa, destinatie, cost;
};

struct Graf
{
    int V, M;
    struct Muchie muchie[MAX_MUCHII];
};


int Uneste (int x, int y);
int GasesteMultime(int x);
void ArboreAcoperireMinima(struct Graf* g);
#endif // CODE_BORUVKA_H

