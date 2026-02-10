str1 = "hello"
str2 = 'hello'
str3 = str("hello")
str4 = ""
print(type(str1), type(str2), type(str3), type(str4))
str5 = "he said that \"i am from tunisia\""
print(str5)
str6 = ''' he said that i'm from tunisia '''
print(str6)
s1 = "hello "
s2 = "mohamed"
s3 = s1 + s2
print(s3)
s4 = s1 * 3
print(s4)
#index
print(s1[1])
print(s2[0:3])
#s1[1] = 'a'
print(id(s1))
s1 += "world"
