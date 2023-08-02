# Q1. Unique Sort problem – Implement this in 5 different ways. Take a string as input that accepts a comma separated sequence of words as input and
# prints the unique words in sorted form (alphanumerically).  *Input*: orange, white, red, cyan, green, magenta, cyan, pink, white
# *Output*: cyan, green, magenta, orange, pink, red, white

myStr =  input("Enter String : ")
mySet = set(myStr.split(", "))
myList = list(mySet)
myList.sort()
str = myList[0]
for item in myList:
    if(item!=myList[0]):
        str = str+", " + item
#myStr2 = str(myList)

print("Unique and Sorted words: ",str)