L=[3,5,4,1,2]
def menor(L):
    for i in range(len(L)-1):
        if L[i]<L[i+1]:
            temp = L[i]
            L[i] = L[i+1]
            L[i+1] = temp
    return L[len(L)-1]
print(menor(L))
def maior(L):
    for i in range(len(L)-1):
        if L[i]>L[i+1]:
            temp=L[i]
            L[i]=L[i+1]
            L[i+1]=temp
    return L[len(L)-1]
print(maior(L))
