def values(a):
    print('The_Original_List_is:',a)
    return sorted(a,key=len)
b=['apple','Blueberries','banana','pine apple','mango','Dragon Fruit']
print('sort_by_length:',values(b))