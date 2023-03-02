print(dir(""))

help(" ".capitalize) #see what a command does
print("bogDAN!","bogDAN!".capitalize())

#lower
print("lower example ACDEF =", "ABCDEF".lower())

#cente
print("center example James =", "Jamer".center(30))

#count
a = "ana-ana-ana-naana"
print(a.count("ana"), a.count("a"))

#find . index of first occurence unlesss a start is specified
a = "banana, i like bananas"
print(a.find("banana")) #the index is 0 as at position 0 we start banana
#if a.find("banana",5) starts finding since the 5 position
#a[5:].find("banana") is the same as above

#islower - says if all the characters are lower case (isupper the opossite)
print("banana".islower(), "Banana".islower())

#slits, breaks down by delimiter
a = "I see a cat on the roof"
print(a.split()) #breaks down by space and returns to a list

#join (kinda like the opposite of split)
a = "I see a cat on a roof"
words = a.split()

print(" ".join(words))
print("++".join(words))
print(" freaking ".join(words))