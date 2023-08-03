# Q11. Write a Python program that reads a number from input() , calculate sum of n- natural
# number and write result into a file sumresult.txt

num = int(input("Enter number : "))
def Sum(x):
    if(x==1):
        return 1
    return x + Sum(x-1)

result = Sum(num)

f = open("sumresult.txt","w")
f.write(str(result))

