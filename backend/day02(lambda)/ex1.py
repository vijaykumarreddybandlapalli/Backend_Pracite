# d1=[('a',2),('f',4),('z',0),('q',10),('g',9)]
# map()


set={11,22,33,44,55,66,77,88}
def productwith2(num):
    return num*2
print(tuple(map(productwith2,set)))
# (66, 132, 22, 88, 154, 44, 110, 176)
#



print(list(map(lambda x:x*2 ,set)))
# [66, 132, 22, 88, 154, 44, 110, 176]



# names=['Vijay','Manasa','Ajay','hemanth','Santhosh','Chandra','Manjula']
#
# print( list(filter(lambda name: name.lower().startswith('m'), names)))
names = ['Vijay', 'Manasa', 'Ajay', 'hemanth', 'Santhosh', 'Chandra', 'Manjula']
filtered_names = [(i, name) for i, name in enumerate(names) if name.startswith('M')]
print(filtered_names)
