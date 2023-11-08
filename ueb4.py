'''
Algorithmen und Programmierung 3, WS 2023/24 — 7. ¨Ubungsblatt
Abgabe bis Donnerstag, 16. November 2023, 12:00 Uhr, online

Daniel Yu und Leonard Goldmann
28. Verschieben von Funktionen, 0 Punkte, Programmieraufgabe
(a) Schreiben Sie eine Python-Funktion, die eine st¨uckweise konstante Funktion F
um einen Parameter b ∈ R verschiebt:
H = verschiebe(F,b)
Es soll H(x) = F (x + b) sein ¨uberall dort, wo F (x + b) definiert ist.
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

30. Gleichheitstest, 0 Punkte
Schreiben Sie eine Funktion, die zwei st¨uckweise konstante Funktionen auf Gleichheit
testet. Die Definition der Gleichheit ist dabei die ¨ubliche Definition f¨ur Funktionen:
Zwei Funktionen sind gleich, wenn sie den gleichen Definitionsbereich haben und
wenn sie an jeder Stelle des Definitionsbereiches denselben Wert liefern.

31. St¨uckweise konstante Funktionen in Java, 0 Punkte
(a) Schreiben Sie eine abstrakte Klasse oder ein Interface f¨ur den abstrakten Daten-
typ st¨uckweise konstante Funktion mit den Operationen aus der Vorlesung
und aus den obigen Aufgaben.
(b) Implementieren Sie den Datentyp.

32. St¨uckweise konstante Funktionen in Haskell, 0 Punkte
(a) Durch welche Merkmale der Sprache Haskell wird das Konzept der abstrakten
Datentypen unterst¨utzt? (Typklassen? Module?)

Algebraische Datentypen?

(b) Implementieren Sie st¨uckweise konstante Funktionen in Haskell.

33. Umwandeln einer Liste in einen Baum, 0 Punkte (aus einer ehemaligen Klausurauf-
gabe)
Schreiben Sie ein Programm in Java oder Haskell, das eine sortierte Liste von
ganzen Zahlen in einen bin¨aren Suchbaum der kleinstm¨oglichen H¨ohe h umwandelt.
7

34. Spezifikation und Implementierung eines abstrakten Datentyps, 15 Punkte (eine ehe-
malige Klausuraufgabe)
Die folgende Klasse BitSet1 implementiert einen Menge von (nicht zu großen) nicht-
negativen ganzen Zahlen als Bitvektor, gruppiert in 64-Bit-W¨orter.
public class BitSet {
int maxWert, Gr¨oße;
long A[];
BitSet(int maxW) {
maxWert = maxW;
Gr¨oße = 1+maxW/64;
A = new long[Gr¨oße];
}
public boolean contains(int i) {
if ((i>maxWert) || (i<0))
return false;
int k = i/64;
int shift = i-k*64;
return ((A[k]>>shift) & 1)==1;
}
. . .
Python-Version:
class BitSet:
def __init__(self, maxW):
self.maxWert = maxW
self.Gr¨oße = 1+maxW//64
self.A = [0]*self.Gr¨oße
def contains(self, i):
if i>self.maxWert or i<0:
return False
k = i//64
shift = i%64
return (self.A[k]>>shift) & 1
. . .
(a) Wie wird die Menge {1, 3, 5, 7} bei einer Menge mit maxWert = 100 dargestellt?
(b) Definieren Sie einen passenden abstrakten Datentyp, der zus¨atzlich zur Initiali-
sierung und zu contains auch die Operationen add (Hinzuf¨ugen eines Elemen-
tes), union (Vereinigungsmenge) und isempty (Test auf leere Menge) enth¨alt.
(c) Spezifizieren sie alle Operationen und den Konstruktor durch die n¨otigen Vor-
bedingungen und Nachbedingungen.
(d) Erg¨anzen Sie die Implementierung der entsprechenden Methoden in Java oder
Python.
(e) Geben Sie die Abstraktionsfunktion und gegebenfalls die Darstellungsinvarian-
ten und Nebenbedingungen dieser Implementierung an. Geben Sie an, was bei
Verletzung der Nebenbedingungen passiert. (Die Korrektheit brauchen Sie nicht
zu beweisen.)
(f) (0 Punkte) In gewissen F¨allen wird bei dieser Implementierung Speicherplatz
verschwendet? Wie kann man das vermeiden?
35. Teilwort, Pr¨adikatenlogik, 5 Punkte
a = a1a2 . . . am, b = b1b2 . . . bn und c = c1c2 . . . uu seien W¨orter der L¨ange m, n, u
¨uber einem Alphabet Σ, das heißt, Folgen von Symbolen ai, bi, ci ∈ Σ.
Definieren Sie in der Sprache der Pr¨adikatenlogik folgende Aussagen pr¨azise:
(a) ab = c, das heißt, c entsteht durch Hintereinanderschreiben von a und b.
(b) a kommt in b als Teilwort vor. (Sie k¨onnen die in 35a definierte Verkn¨upfung
zweier W¨orter verwenden, oder es direkt definieren.)
1https://mycampus.imp.fu-berlin.de/x/WGOPZe und https://mycampus.imp.fu-berlin.de/x/ZhD8nM
8'''