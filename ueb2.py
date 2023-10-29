''' Ueb3 Daniel Yu, Leonard Goldmann
11.
a) 
Enden sicher mit 4->2, da 2 einzige ohne Nachfolger, 4 nur vor 2 mit 1,6,5,3 abhängigkeiten (in)direkt vor vier haben, nun malt man sich den Graphen auf mit den vier Knoten 

übrig bleiben die Möglichkeiten: 
1,3,6,5
1,3,5,6
3,1,6,5
3,1,5,6
3,5,1,6 

Also
1,3,6,5,4,2
1,3,5,6,4,2
3,1,6,5,4,2
3,1,5,6,4,2
3,5,1,6,4,2 

b) n-1 Abhängigspaare braucht man mindestens (kleinster Baum)

c) Man kann maximal n-1 + n-2 ... + 1 = n(n-1)/2 (kleiner Gauß)

12.
Wir brechen einfach immer ab, wenn
Queue/Liste L mit Knoten ohne Vorgänger leer ist.
Falls es Einträge von Knoten mit Abhängigkeiten existieren, 
bedeutet das, dass diese einen Kreis bilden, da jeder einen Vorgänger hat 
und keine weiteren entfernt werden können -> das Schöne ist, jeder hat nun einen Vorgänger

Wir haben eine Liste L mit Knoten und A mit Abhängigkeiten.

Wir nehmen einen beliebigen Knoten und kennzeichnen ihn als gesehen
1. Für alle Nachbarn besuchen wir iterativ einmal.
2. Gehe zu Nachbar, Abhängigkeit speichern
2.1 falls nicht gesehen, als gesehen markieren. Wdh von Schritt 1
2.2 gesehen -> Kreis. Knoten n ganz dick merken
3.Nun gehen wir nochmal durch alle Abhängigkeit bis wir wieder eine abh zu n finden.


14.
a) Algorithmus funktioniert nicht, denn quantitativ werden 
doppelte Abhängigkeiten nicht entfernt, s.d. ein Knoten nie vollständig 
seine 

Ein Paar (i,i) ist selbst ein Kreis und sorgt dafür, dass ein Knoten i 
niemals selbst entfernt wird.

b) 

c) 

15.
Nicht für alle Durchläufe haben wir lineare laufzeit.
Betrachtet man die letzten Summanden, dann findet man Ausdrücke
wie (n-2)n+(n-1)+n*n, alles in O(n*n)

Eigentlich sollte man n aus dem Term ausklammern und mittels 
Sum k erhält man per gauß n*n*(n+1)/2 => O(n*n*n)




13.
'''
import sys
if len(sys.argv)>1:
    file = open(sys.argv[1],'r')
else:
    file = sys.stdin

def readInt():
    for line in file:
        for v in line.split():
            yield int(v)

def circle_finder():
    pass

def TopoSort():
    print ("Topologischen Sortieren.")
    # Einlesen
    input = readInt() #<- spezifikation?
    #input=input()#?
    n = next(input)

    # Inititalisieren array:
    Knotenliste = [None] + [ Knoten(i) for i in range(1,n+1) ]
    
    # Einlesen Kanten
    try:
        while True:
            e = Knotenliste[next(input)]
            f = Knotenliste[next(input)]
            x = Kante(e,f)
            e.Nachfolgerliste.append(x)
            f.anzVorgänger+=1
    except StopIteration:
        pass
        
    # Vorbereiten:
    freieKnoten = []
    for i in range(1,n+1):
        e = Knotenliste[i]
        if e.anzVorgänger==0:
            freieKnoten.append(e)


    # Sortieren:
    print("");
    for i in range(1,n+1):#achso n mal einfach ausführen
        if freieKnoten == []:
            kreis=circle_finder()
            print("Die Eingabe enthält einen Kreis.")
            return
        # Wähle einen Knoten ohne Vorgänger
        x = freieKnoten.pop()
        print(x)
        # Entferne ausgehende Kanten:
        for z in x.Nachfolgerliste:
            z.v.anzVorgänger -= 1
            if z.v.anzVorgänger == 0:
                freieKnoten.append(z.v)

class Knoten:
    def __init__(self, i):
        self.Name = i
        self.anzVorgänger = 0
        self.Nachfolgerliste = []
    def __str__(self):
        return str(self.Name)

class Kante:
    def __init__(self, u, v):
        self.u = u
        self.v = v

TopoSort()        
