# Q10. Write a Python function to count the number of digits in a given number and return result into a file countdigit.txt

num = 465645754
def count(x):
  num1 = str(num)
  length = len(num1)
  return length

result = count(num)
f = open("countdigit.txt","w")
f.write(str(result))
