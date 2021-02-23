PARASCHIV ALEXANDRA
GRUPA 333CA
LABORATOR 4 ASC

Precizari sistem:
Intel  i3-5005U @ 2.00GHz
RAM = 4GB @ 1600MHz

Task 1
a)
Nu se pot da mmap()-uri mari => probleme valgrind.
Astfel, putem aloca maximum 10000000 de elemente.

b)
Dimensiunea stiva - 8MB pe Linux; 
Astfel se pot aloca mai putin de 8MB / sizeof(struct particle) elemente, adica 8MB/3. 
Pentru ca atunci cand declaram vectorul = 1 acces la memorie => stiva va fi in cacheul de date atunci cand parcurgem vectorul => mult mai putine miss-uri.

c)
Sistemul de operare aloca maximul, in functie de memoria vrituala;
se vor scadea spatiul pentru kernel, sectiunile de
cod, bss, etc.

Task 2
task2_lin
Matricea este o linie => miss-uri putine => timpul de executie este mai mic.

task2_mat
Matricea este parcursa pe linii => miss-uri mai evidente.


Task 3
Compilatorul -> reordoneaza variabilele i, l, a, b pentru aliniere. 
Primele sunt b-urile (aliniere la 32B), apoi a, apoi l si apoi i. Dimensiunile pentru i, l si a = puteri de 2 = > este alocat spatiu pentru ele de catre compilator, nu incearca sa le si alinieze.

Task 4
L1
Plot pentru dimensiunea cache-ului L1.
Graficul ce ilustreaza performanta incepe sa scada pe la 30K +, adica dimensiunea cu aproximare a cache-ului L1 al procesorului.

L2
Plot pentru dimensiunea cache-ului L2.
Graficul ce ilustreaza performanta incepe sa se aplatizeze/indrepte intre 100K si 200k, adica dimensiunea cu aproximare a cache-ului L2 al procesorului.

Task 5
Plot pentru dimensiunea liniei cache-ului.
Graficul ce ilustreaza performanta incepe sa se aplatizeze/indrepte intre 50 si 100 bytes, adica dimensiunea cu aproximare a liniei cache-ului procesorului.


