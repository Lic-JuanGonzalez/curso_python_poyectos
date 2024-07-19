mi_tuples = (1,2,3,4)
print(type(mi_tuples))

t = (5,5.6,'ff')
print(type(t))

print(mi_tuples[0])
# mi_tuples[0] = 5
print(mi_tuples)

mi_tuples2 = (1,2,(10,20),4)
print(mi_tuples2[2][0])

mi_tuples2 = list(mi_tuples2)
print(type(mi_tuples2))

mi_tuples2 = tuple(mi_tuples2)
print(type(mi_tuples2))

x,y,z = t
print(x,y,z)

mi_tuples3 = (1,2,3,1)
print(len(mi_tuples3))

print(mi_tuples3.count(1))
print(mi_tuples3.index(2))
