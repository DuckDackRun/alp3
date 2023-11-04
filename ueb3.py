'''Daniel Yu, Loenard Goldmann

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

menge vereinige(menge,menge) mit vereinige: MxM->M
menge schnitt(menge,menge) mit schnitt: MxM->M

#sehr verwirrt


23.

a) es wird ein Blatt nachgereicht
b)
höchstens 2^h-1, denn 
mindestens 2^(h-1)+1 (wenn alle Knoten mit Tiefe <= h-2 zwei Knoten haben, ist bis h-1 alles vollständig)
c) 

24.
das ist eine Form eine Menge darzustellen, anhand der Reihenfolge der Operationen, die ausgeführt worden sind.
Man kann für jede Zahl z, eine Sortierung finden, dessen erste Stelle vorgibt, ob das Element in M enthalten ist (anhand Lö,Ei)

Gesucht ist die prädikatenlogische Abstraktionsfkt, die den ADT in eine menge übersetzt.


'''