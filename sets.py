mi_set = set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)

mi_set2 = {1,2,3,4,5,1,1,2,3,3,4}
print(type(mi_set2))
print(mi_set2)

# si acepta tuplas
mi_set3 = {1,2,3,4,5,(1,2,3),1,1,2,3,3,4}
print(type(mi_set3))
print(mi_set3)

# print(mi_set[0])
# mi_set[0] = 5

print(len((mi_set)))
print(2 in mi_set)

s1 = {1,2,3}

# s1.add(4)
# print(s1)
#
# s1.pop() # Elimina un elemento aleatorio si no se especifica
# print(s1)
#
# s1.remove(3)
# print(s1)
#
# s1.discard(2) # No da error solo lo descarta si no existe el elemento
# print(s1)
#
# s1.clear()
# print(s1)

s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)
