def bubblesort(li):
    for i in range(len(li)):
        for j in range(0,len(li)-i-1):
            if li[j] > li[j+1]:
                temp = li[j]
                li[j] = li[j+1]
                li[j+1] = temp

list1 = [5,4,20,11,56,27,89]
print("Before sorting : \n")
print(list1)
bubblesort(list1)
print("After sorting : \n")
print(list1)