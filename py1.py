a=12
a=-120
print(a)

str="python's tech"
print(str)

mul='''Life
Is
too
Short'''
print(mul)

str1="hello"
str2=" world"

print(str1+str2)

print(str1*3)

print(len(str1))

print(str1[1])

print(str1[0:3])

print("I eat %d apple" % 3)

number=10

day="three"

print("%d %s" % (number, day))

a="hobby"

print(a.count('a'))

a="bes Python is the best choice"

print(a.find('b'))
print(a.find('K'))
print(a.find('best'))

main_string = "Hello, world!"
try:
    index = main_string.index("z")
    print("Substring found at index:", index)
except ValueError:
    print("Substring not found")


print(",".join("abcd"))

a="hi"
print(a.upper())

a="  hi  "
print(a.lstrip(), len(a.lstrip()))
print(a.rstrip(), len(a.rstrip()))
print(a.strip(), len(a.strip()))

a="Life is too shore Life"
print(a.replace("Life", "ABC"))

print(a.split())

a=[1,2,3,4,5]
print(a[0:2])
del a[1]
print(a)

a.append(6)
print(a)

a=[1,4,3,2]
a.sort()
print(a)

a.reverse()
print(a)

print(a.index(3))

a.insert(0, 9)
print(a)

a.remove(9)
print(a)

print(a.pop())
print(a)

print(a.count(1))

a.extend([6,7])
print(a)

a={1:"name"}
print(a)
print(a[1])
print(a.keys())
print(a.values())
print('name' in a)

s1=set([1,2,3])
l1=list(s1)
print(l1)

s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])

print(s1&s2)
print(s1|s2)
print(s1-s2)

a=["Life", "Life", "Life", "Life"]
print(" ".join(a))


l1=[1,2,3]
l2=[1,2,3]
print(l1+l2)

str="I ate {0} pizza and write {1} quotes".format(1, "many")
print(str)