#len gives you the lenght of the entire string
print(len("Hello"), len("Hello!"))

#you can assign a string to any variable
a = "123"
b = "abcd"

# + will concatenate the string
c = a + b
print(c)

c = a + b + c
print(c)

# * can only miltiply with a positive integer and repeats the string
a = "Banana"
print(a*3)
print(4*a)
print((4//2)*a) #you have to do // as this is a integer division
print(int(10/3)*a)

#string are iterable... we can use for on them
for letter in a:
    print(letter,end=" ! ")

for letter in a:
    print(3*letter, end="")

#while to iterate a string backwards
a = "@racecar!"
print("\n\n")
i = len(a) - 1
while i>= 0:
    print(a[i])
    i -=1 #1 = i -1