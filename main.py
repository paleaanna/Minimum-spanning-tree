import kruskal
import afiseazameniu
import time
afiseazameniu.afiseazameniu()
alegere = raw_input()
file_paths = {
    'a': 'date1.txt',
    'b': 'date2.txt',
    'c': 'date3.txt',
    'd': 'date4.txt',
    'e': 'date5.txt',
    'f': 'date6.txt',
    'g': 'date7.txt',
    'h': 'date8.txt',
    'i': 'date9.txt',
    'j': 'date10.txt',
    }
file_path = file_paths.get(alegere)
if not file_path:
    print("Input invalid")
    exit(1)

with open(file_path, 'r') as fin:
    varfuri = int(fin.readline())
    g = kruskal.Graph(varfuri)
    muchii = int(fin.readline())
    i = 0
    while i < muchii:
        g.adaugamuchie(int(fin.readline()), int(fin.readline()), int(fin.readline()))
        i = i + 1
start = time.time()
g.arboreacoperireminima()
print("Timpul cat a rulat programul: %f" % (time.time()-start))