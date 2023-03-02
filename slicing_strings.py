a ="abcdefghijklmnop"
print(a[3:6])
print(a[13:17], a[-3:], a[13:]) #all of them mean the same: nop
# : is used to say until the end

#step slice
print(a[:10:2]) #you go 2 by 2

string = "racecar"
if string == string[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
