class order:
    def reorder(self,a):
        if len(a)==0:
            return[]
            k=0
            for i in range(len(a)):
                if a[i]!=0:
                    a[k]=a[i]
                    k+=1
            for j in range(k,len(a)):
                a[j]=0
            return a
ob=order()
a=[2,0,1,4,0,5,6,4,0,1,7]
print(ob.reorder(a))
