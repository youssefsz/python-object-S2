#Exercice 3:


DicPC = { 'Hp' : 10, 'Dell' : 15, 'Lenovo' : 20 }
DicPhone = { 'Samsung' : 5, 'Apple' : 8, 'Huawei' : 12 }
DicTablet = { 'iPad' : 7, 'Samsung' : 6, 'Lenovo' : 9 }

#method 1
DicAll = {}
for key, value in DicPC.items():
    DicAll[key] = value
for key, value in DicPhone.items():
    DicAll[key] = value
for key, value in DicTablet.items():
    DicAll[key] = value

print(DicAll)

#method 2
DicAll2 = DicPC.copy()
DicAll2.update(DicPhone)
DicAll2.update(DicTablet)
print(DicAll2)