# 13. Write a python program that read input string from file stringinput.txt .Find the reverse of
# that string and write result into another file reversestr.txt

f1 = open("stringinput.txt",'r')
str1 = f1.read()
str2 = str1[-1::-1]
f2 = open("reversestr.txt",'w')
f2.write((str2))