class Combinaison:
    def __init__(self,l):
        self.combinaison = []
        self.combine(l)
        
    @staticmethod
    def swap_(l,i,j):
        l2 = l    
        tmp = l2[i]
        l2[i] = l2[j]
        l2[j] = tmp
        return l2
    
    def combine(self, l, begin = []):
        for i in range(len(l)) :   
            x = begin + l[i:i+1]
            y = l[:i] + l[i+1:]
            if len(y)==2   :     
                self.combinaison.append(x + y )
                self.combinaison.append(x+ self.swap_(y, 0, 1))
            else:
                self.combine(y, x)


cb = Combinaison([0,1,2,3])
for i in cb.combinaison:
    print(i)


