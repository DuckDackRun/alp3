'''
Algorithmen und Programmierung 3, WS 2023/24 — 7. ¨Ubungsblatt
Abgabe bis Donnerstag, 16. November 2023, 12:00 Uhr, online

Daniel Yu und Leonard Goldmann
28. Verschieben von Funktionen, 0 Punkte, Programmieraufgabe
(a) Schreiben Sie eine Python-Funktion, die eine st¨uckweise konstante Funktion F
um einen Parameter b ∈ R verschiebt:
H = verschiebe(F,b)
Es soll H(x) = F (x + b) sein ¨uberall dort, wo F (x + b) definiert ist.


'''
def v(st,b):
    l=st[0]+b
    r=st[-1]+b
    ans=[]
    i=0
    while l<=st[i]<r:#while bedingung, dass sti zwischen l und r wäre robuster 
        if st[i]>r:
            ans.append(r)
            break
        ans.append(st[i]+b)
        ans.append(st[i+1])
        i+=2
    ans.append(r)
    return ans
        

'''
(b) Wie entsteht der Graph von H aus dem Graphen von F , wenn b = 1 ist?

29. Fallunterscheidung, 10 Punkte, Programmieraufgabe
Schreiben Sie eine Python-Funktion
H = fallunterscheidung(b,F,G)
die bei Eingabe von zwei st¨uckweise konstanten Funktion F und G und einem Para-
meter b ∈ R die Funktion H erzeugt, die folgendermaßen definiert ist:
H(x) =
{
F (x), wenn x < b
G(x), wenn x ≥ b
Erg¨anzen Sie diese Spezifikation, falls Sie es f¨ur erforderlich halten, zum Beispiel
durch Angabe von passenden Vorbedingungen.

'''
#Vorbedingugn F mindestens bis b definiert, G mindestens ab G definiert
def fallunterscheidung(F,G,b):
    #addiere G and current ans
    def addG(cur,G,b):
        G=list(G)
        if G[-1]<=b:
            return           
        else:
            i=0
            while b>G[i]:
                i+=2
            cur= cur + G[i-1:]
    
    ans=[]
    if b<F[0]:
        addG(ans,G,b)         
    else:
        i=0
        while b>=F[i]:           
            ans.append(F[i])
            ans.append(F[i+1])
            i+=2
        ans.append(b)
        addG(ans,G,b)
    return tuple(ans)
# ... wird sowieso nicht benotet :/
'''
30. Gleichheitstest, 0 Punkte
Schreiben Sie eine Funktion, die zwei st¨uckweise konstante Funktionen auf Gleichheit
testet. Die Definition der Gleichheit ist dabei die ¨ubliche Definition f¨ur Funktionen:
Zwei Funktionen sind gleich, wenn sie den gleichen Definitionsbereich haben und
wenn sie an jeder Stelle des Definitionsbereiches denselben Wert liefern.
'''
def equal(F,G):
    def norm():
        pass#ziemlich ineffizient, eine sinnvolle annahme wäre, dass die fkt automatisch normiert werden
    return norm(F)==norm(G)

def equal2(F,G):
    i=0
    j=0
    cur=[0,0]
    end=max(len(F),len(G))
    while i<end and j <end:
        if F[i]<F[j]:
            pass# da müsste man überlegen wie man das elegant macht
        i+=2
        j+=2
'''
31. St¨uckweise konstante Funktionen in Java, 0 Punkte
(a) Schreiben Sie eine abstrakte Klasse oder ein Interface f¨ur den abstrakten Daten-
typ st¨uckweise konstante Funktion mit den Operationen aus der Vorlesung
und aus den obigen Aufgaben.

hm 

(b) Implementieren Sie den Datentyp.

32. St¨uckweise konstante Funktionen in Haskell, 0 Punkte
(a) Durch welche Merkmale der Sprache Haskell wird das Konzept der abstrakten
Datentypen unterst¨utzt? (Typklassen? Module?)

Algebraische Datentypen? Ich weiß es nicht, sag es mir.

(b) Implementieren Sie st¨uckweise konstante Funktionen in Haskell.

TYPE Num = Num Int Int Num | Num Int

33. Umwandeln einer Liste in einen Baum, 0 Punkte (aus einer ehemaligen Klausurauf-
gabe)
Schreiben Sie ein Programm in Java oder Haskell, das eine sortierte Liste von
ganzen Zahlen in einen bin¨aren Suchbaum der kleinstm¨oglichen H¨ohe h umwandelt.
7
uff rotation? oder mittels Median suchen und dividen >.> letzteres klappt eigentlich super gut

34. Spezifikation und Implementierung eines abstrakten Datentyps, 15 Punkte (eine ehe-
malige Klausuraufgabe)
Die folgende Klasse BitSet1 implementiert einen Menge von (nicht zu großen) nicht-
negativen ganzen Zahlen als Bitvektor, gruppiert in 64-Bit-W¨orter.
'''
class BitSet:

  def __init__(self, maxW):
     self.maxWert = maxW
     self.Größe = 1+maxW//64
     self.A = [0]*self.Größe
  
  def contains(self, i):
     if i>self.maxWert or i<0:
        return False
     k = i//64
     shift = i%64
     return (self.A[k]>>shift) & 1 == 1

#Rückgabe ist, ob Funktion erfolgt ist
  def add(self,i):
    if i>self.maxWert or i<0:
        
        
        altwert=self.maxWert
        self.maxWert =i
        self.Größe = 1+i//64
        self.A=self.A+[0]*(self.Größe-altwert)
        self.add(i)
        #klappt relativ gut?
        return 
    k=i//64
    shift =i%64
    self.A[k] |= (1<<shift)
    return 
#self-Liste ist selbst größer als fremdes bitset, Rückgabe ob Funktion erfolgt ist
  def union(self,bitset):
    
    if bitset.maxWert>self.maxWert:
        #self vergößern
        altwert=self.maxWert
        self.maxWert =bitset.maxWert
        self.Größe = bitset.Größe
        self.A=self.A+[0]*(self.Größe-altwert)
    
    for i in range(bitset.Größe):
        self.A[i]=self.A[i] | bitset.A[i]

    return
     
     
  def isempty(self):
    return self.A == [0]*self.Größe #klappt das?
# Tests

a1 = BitSet(500)
a2 = BitSet(300)

a2.add(300)
a2.add(7)
a2.add(5)
a2.add(3)
a2.add(1)
try:
    a2.add(301)
except AssertionError:
    print("Add Error")
print (a1.isempty(),a2.isempty())
try:
    a1.union(a2)
    print(1)
except AssertionError:
    print("Union Error")
a1.union(a2)
print(a2.A,a1.A)
print (a1.isempty(),a2.isempty(), a1.contains(301), a1.contains(300),a2.contains(300),a2.contains(7),a2.contains(301))

'''
(a) Wie wird die Menge {1, 3, 5, 7} bei einer Menge mit maxWert = 100 dargestellt?

hm 2+8+32+2**7=170. Da 1<3<5<7<100 liegt alles im ersten Block (170 zusammenaddiert) und 2*64>100>64, ergeben zwei Blöcke => [170,0]

(b) Definieren Sie einen passenden abstrakten Datentyp, der zus¨atzlich zur Initiali-
sierung und zu contains auch die Operationen add (Hinzuf¨ugen eines Elemen-
tes), union (Vereinigungsmenge) und isempty (Test auf leere Menge) enth¨alt.



(c) Spezifizieren sie alle Operationen und den Konstruktor durch die n¨otigen Vor-
bedingungen und Nachbedingungen.


(d) Erg¨anzen Sie die Implementierung der entsprechenden Methoden in Java oder
Python.

s.0.

(e) Geben Sie die Abstraktionsfunktion und gegebenfalls die Darstellungsinvarian-
ten und Nebenbedingungen dieser Implementierung an. Geben Sie an, was bei
Verletzung der Nebenbedingungen passiert. (Die Korrektheit brauchen Sie nicht
zu beweisen.)



(f) (0 Punkte) In gewissen F¨allen wird bei dieser Implementierung Speicherplatz
verschwendet? Wie kann man das vermeiden?

Ähnlich wie bei Arrays können weit hinten angelegte Blöcke unbenutzt sein. Diese könnte man dynamisch löschen. 



35. Teilwort, Pr¨adikatenlogik, 5 Punkte
a = a1a2 . . . am, b = b1b2 . . . bn und c = c1c2 . . . uu seien W¨orter der L¨ange m, n, u
¨uber einem Alphabet Σ, das heißt, Folgen von Symbolen ai, bi, ci ∈ Σ.
Definieren Sie in der Sprache der Pr¨adikatenlogik folgende Aussagen pr¨azise:
(a) ab = c, das heißt, c entsteht durch Hintereinanderschreiben von a und b.
(b) a kommt in b als Teilwort vor. (Sie k¨onnen die in 35a definierte Verkn¨upfung
zweier W¨orter verwenden, oder es direkt definieren.)
1https://mycampus.imp.fu-berlin.de/x/WGOPZe und https://mycampus.imp.fu-berlin.de/x/ZhD8nM
8'''

