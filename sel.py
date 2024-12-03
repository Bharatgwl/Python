def selection(li):
    le =len(li)
    for i in range(0,le,1):
        mini =i
        for j in range(i+1,le):
            if li[j]<li[mini]:
                mini=li[j]
        li[i],li[mini]=li[mini],li[i]
    return 
li=[4,3,2,1]
selection(li)
print(li)
                
        