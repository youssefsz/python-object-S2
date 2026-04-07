# TP5 : Les tuples en Python
# Ce programme est uniquement a but educatif.

t1 = (1, 2, 3, 4, 5)
print(t1, type(t1))

t2 = tuple([10, 20, 30, 50, 60, 30])
print(t2, type(t2))

list1 = ["apple", "banana", "cherry"]
list1[1] = 12
print(list1)

'''
t1[1] = 12
print(t1)
'''

print(max(t2), min(t2), len(t2), sum(t2))

t3 = ((1, 2, 3), (4, 5, 6), "hello", "bonjour")
print(type(t3))
print(t3)
print(t3[0])
print(t3[0][2])

for i in t2:
    print(i, end="\n")

t4 = "bonjour", "hello"
print(type(t4))

print(t2.count(30))
print(t2.index(30))

a = ("a", "b", "c")
x, y, z = a

print(x)
print(y)
print(z)
