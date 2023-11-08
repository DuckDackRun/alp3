'''Daniel Yu, Loenard Goldmann ... bei Dori

21.
z.z
istenthalten(u, einfügen(y, löschen(x, m)))= istenthalten(u, löschen(x, einfügen(y, m)))

Fall: u=y!=x
=>istenthalten(u, einfügen(y, löschen(x, m)))= istenthalten(u, löschen(x, einfügen(y, m)))
=>True = istenthalten(u, löschen(x, einfügen(y, m)))                                        |(Regel 2 u=y)
=>True = istenthalten(u, einfügen(y, m))                                                    |(Regel 5 u!=x)
=>True = True                                                                               |(Regel 2 u=y)

Fall: u!=y!=x
=>istenthalten(u, einfügen(y, löschen(x, m)))= istenthalten(u, löschen(x, einfügen(y, m)))
=>istenthalten(u,löschen(x, m))= istenthalten(u, löschen(x, einfügen(y, m)))
=>istenthalten(u, m)= istenthalten(u, löschen(x, einfügen(y, m)))
=>istenthalten(u, m)= istenthalten(u, einfügen(y, m))
=>istenthalten(u, m)= istenthalten(u, m)

Fall: u=x!=y
kriegt man gut hin


22.

menge unite(menge,menge) mit vereinige: MxM->M
dann ist:
istenthalten(x, unite(A,B)) = istenthalten(x,A) or istenthalten(x,B) (1)
istenthalten(x, einfügen(y, unite(A,B))) = True, für x = y 
istenthalten(x, einfügen(y, m)) = istenthalten(x, m), f¨ur x̸ = y s.o.
istenthalten(x, löschen(x, m)) = False f¨ur x = y 
istenthalten(x, löschen(y, m)) = istenthalten(x, m), f¨ur x̸ = y s.o.

menge cut(menge,menge) mit schnitt: MxM->M
dann ist:
stenthalten(x, cut(A,B)) = istenthalten(x,A) and istenthalten(x,B) (1)
istenthalten(x, einfügen(y, m)) = True, für x = y 
istenthalten(x, einfügen(y, m)) = istenthalten(x, m), für x̸ = y s.o.
istenthalten(x, löschen(x, m)) = False für x = y 
istenthalten(x, löschen(y, m)) = istenthalten(x, m), f¨ur x̸ = y s.o.


23.

a) es wird ein Blatt nachgereicht

b)
höchstens 2^(h+1)-1, denn wenn wir alle Knoten besetzen bis h haben wir 1+2+4... also sum von i=0 bis h mit 2**i = 2^(h+1)-1
mindestens 2^(h) (wenn alle Knoten mit Tiefe <= h-2 zwei Knoten haben, ist bis h-1 alles vollständig wie s.o. =>2^h-1+1=2^h)
c)
Sei n die Anzahl der Knoten eines vollst. balanc. Baum, dann gilt 2^h<=n<=2^(h+1)-1 
also h<=logn  und n <=2^(h+1)-1 -> h >=log(n+1)-1
so ist h element von theta(logn)
Schranken lassen sich oben ableiten 

24.
das ist eine Form eine Menge darzustellen, anhand der Reihenfolge der Operationen, die ausgeführt worden sind.
Man kann für jede Zahl z, eine Sortierung finden, dessen erste Stelle vorgibt, ob das Element in M enthalten ist (anhand Lö,Ei)

Gesucht ist die prädikatenlogische Abstraktionsfkt, die den ADT in eine menge übersetzt.


'''