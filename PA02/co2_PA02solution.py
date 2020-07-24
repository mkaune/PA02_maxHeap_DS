"""
In dieser Programmieraufgabe geht es um eine erste Implementierung von
Max-Heaps und Operationen auf diesen.
"""

class MaxHeap:
    #A=[3,4,10,14,7,9,16,2,8,1]
    # Der Konstruktor soll eine ubergebene Liste keys von paarweise
    #verschiedenen, positiven ganzen Zahlen in einen Max-Heap umwandeln
    def __init__(self, keys):
        #keys soll die max-Heap E erfullen
        A=keys
        n=len(A)
        #Build-Max-heap aus der Vorlesung

        #Iteriere uber alle Nicht-Blatter des Binarbaumes
        #von unten nach oben
        
        #Blater haben keine kinder"
        for i in range(n//2, 0, -1):
            largest=i
        #MaxHeapify aus der Vorlesung mit while anstatt Functionaufruf
        
            while largest==i:

                #i ist parent  
                l=2*i #left Kind
                r=2*i+1 #right Kind
            
                if l<=n and A[l-1]>A[i-1]:
                    largest=l
                
                if r<=n and A[r-1]>A[largest-1]:
                    largest=r

                # mind. ein kind ist grosser als parent  
                if largest!= i:
                    A[largest-1],A[i-1]=A[i-1],A[largest-1]#swap parent-kind
                    i=largest  
                    #bei VL: Max-Heapify(A, largest)
                    
                #dies beduetet parent grosser als kinder 
                else:
                    largest= -1
                    #break
        self.keys=A
        
    #Operationen fur Maxheaps
        
    def maximum(self):
        #maximale element des Max-Heaps self.keys zuruck, also die Wurzel!
        #Laufzeit: O(1)
        
       return self.keys[0]
    
    def extractMax(self):
        
        """liefert maximales Element
        und loscht dieses aus der Datenstruktur"""

        #Lsufzeit O(log n)
        A=self.keys
        n=len(A)-1

        #A[0] grosstes Element
        #swap letztes Element mit dem ersten --> Maxheap eigenschaft verletzt sich
        A[n],A[0]=A[0],A[n]
        #Maximales ELement befindet sich jetzt am ende
        n=n-1
        i=1 # verletzung der MH eingeschaft an der Wurzel
        largest=1
        #aber MHE lokal an allen anderen Knoten erfullt:
        
        #es reciht max_hipify in A[:n-1]:
        #stellt die Max-Heap-Eigenschaft von self.keys wieder her.
        while largest==i:
                    
                l=2*i
                r=2*i+1
            
                if l<=n and A[l-1]>A[i-1]:
                    largest=l
                
                if r<=n and A[r-1]>A[largest-1]:
                    largest=r
                if largest!= i:
                    A[largest-1],A[i-1]=A[i-1],A[largest-1]
                    i=largest
                else:
                    largest=-1

        #gibt letztes Element zuruck
        max_elem=A.pop()
        self.keys=A
        return max_elem
    
    def increaseKey(self,i,k):
        #Laufzeit o(log n)
        A=self.keys
        # erhohe A[i] auf k falls moglich!!
        n=len(A)-1
        #  
        if i<=n and A[i]<=k:
            A[i]=k #A[i] wird grosser
            indice_parent=(i-1)//2 #vorgaenger
            
            # MaxHeap eigenschaft konnte verletzt sein(slso falls k>parent von A[i])
            #schleife beschaftigt sich solange: i ist nicht die wurzel; vorganger ist kleiner
            while i>0 and A[indice_parent]<A[i]:
                # bei der vorganger von i ist die MHE verletzt
                #swap parent mit child
                A[indice_parent],A[i]=A[i],A[indice_parent] #lokale MHE ersetzt
                i=indice_parent #wir gehen nach oben
                indice_parent=(i-1)//2
                #nach oben reparieren
        else:
            print("k too small")

        self.keys=A
        #bei decreaseKey komplizierter: jeder Knoten bis zu zwei kinder. 
    def insert(self,k):
        
        #einfugen vom schlussel k am ende
        #O(log n)
        
        A=self.keys
        n=len(A)
        
        #fuge ein weiteres Element in das array ein
        A.append(-1) #negative zahl reicht, demn schlusseln sind naturliche zahlen.
        #erhoht diesen Eintrag auf positiven k
        self.increaseKey(n,k)

    def heapSort(self):
        A=self.keys
        #liste mit maxheap Eigenschaft
        n=len(A)
        for j in range(n, 1, -1):
            #swap erstes Element(grosstes) mit letztes
            A[0],A[j-1]=A[j-1],A[0 ]
            #j+= -1
            i=1
            largest=i
            #Max-heapify auf liste  bis j-1
            while largest==i:
                    
                l=2*i #leftchild    
                r=2*i+1 #rightchild
                
                #j reduziert sich bei jeder iteration
                if l<=j-1 and A[l-1]>A[i-1]:
                    largest=l
                
                if r<=j-1 and A[r-1]>A[largest-1]:
                    largest=r
                    
                if largest!= i:
                    #child ist grosser als parent
                    A[largest-1],A[i-1]=A[i-1],A[largest-1]
                    i=largest #continue while Schleife mit neuen child
                else:
                    largest=-1 #stop while Schleife
            #A[0] wieder grosstes element
        self.keys=A
        self.keys.reverse()
        #self.A.reverse() 
            
        
keys=[3,4,10,14,7,9,16,2,8,1]
c=MaxHeap(keys)
print(keys)
#keys=[3,4,10,14,7,9,16,2,8,1]
c.insert(13)
print(keys)

#keys=[3,4,10,14,7,9,16,2,8,1]
c.extractMax()
print(keys)

#keys=[3,4,10,14,7,9,16,2,8,1]
c.increaseKey(4,23)
print(keys)

#keys=[3,4,10,14,7,9,16,2,8,1]
c.heapSort()
print(keys)

#keys=[3,4,10,14,7,9,16,2,8,1]

        
    
