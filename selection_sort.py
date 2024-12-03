def selection_sort(li):
    l1 = len(li)
    for i in range(0,l1,1):
        min_elem = i
        for j in range(i + 1,l1):
            if li[j] < li[min_elem]:
                min_elem = j
        temp = li[i]
        li[i] = li[min_elem]
        li[min_elem] = temp
    return


li = [4, 3, 2, 1]
print(li)
selection_sort(li)
print(li)
x=6
y=7

