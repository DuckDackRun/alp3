import random
def swap(li,a,b):
  li[a],li[b]=li[b],li[a]

def sum(li):
  num=0
  for i in li:
    num+=i
  return num

def check(li,multcount=0):
  bool=True

  for i in range(len(li)-1):
    if li[i]>li[i+1]:
      bool=False
    
    if li[i]==li[i+1]:
      multcount+=1


    return (multcount,bool)

def insertsort(li,counter=0):#input li, output num
  for i,n in enumerate(li):
    for _ in range(i):
      counter+=1
      if li[i] >= li[i-1]:
        break
      swap(li,i,i-1)
      i-=1
      
  return counter
    
def quicksort(li,b=3):#input li;output num
  if len(li)<b:
    return insertsort(li)
  else:
    pivot=random.randint(0,len(li)-1)
    lower=[] #inplace quicksort müsste echt schwer sein
    higher=[]
    middle=[]

    for i in li:
      if i <li[pivot]:
        lower.append(i)
      elif i>li[pivot]:
        higher.append(i)
      else:
        middle.append(i)


    count1=quicksort(lower,b)
    count1+=quicksort(higher,b)
    #print(lower,middle,higher)
    liste=lower+middle+higher #das problem derzeit ist, dass er die lsg nur lokal und nicht global speichert/übernimmt - besteht nicht mehr
    for i in range(len(li)):
      li[i]=liste[i]

  return count1+len(li)-1


def gen(n):
  li= [random.random() for _ in range(n)]
  return li



#for i in range(100):
#  print(random.random()) 

def testinsert():
    anzahl=2000 #20000000 ist zu viel für meinen armen rechner
    stat={j:sum([quicksort(gen(anzahl),j) for _ in range(anzahl)])/anzahl for j in range(1,15)}
    print(stat)


     
    
    i=gen(anzahl)
    for schranke in [3,100,20000]:
        b=quicksort(i,schranke)
        print(check(i),b)
    ##es lebt



def testmultiplicat():
    und=6
    num=7

    d={i:0 for i in [10**i for i in range(und,num)]}
    for i in [10**i for i in range(und,num)]:
        for _ in range(10):
            
            test=gen(i)
            #print(test)
            quicksort(test)
            #print(test)
            d[i]+=check(test)[0]

    for i in d.values():
      i=i//10
    print(d)#die wahrscheinlichkeit ist sehr gering, dass zwei zahl identisch sind (überabzählbar) - mehrmals 100* 100000 tests gemacht und unter 100000 nie doppelte vorgekommen

testmultiplicat()
#testinsert()

