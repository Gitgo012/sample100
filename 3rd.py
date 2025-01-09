list1=[1,2,3,4]
list2=[5,6,7]
list3=[]
max_length=max(len(list1),len(list2))
for i in range(max_length):
    if i<len(list1):
        list3.append(list1[i])
    if i<len(list2):
        list3.append(list2[i])
print(list3)