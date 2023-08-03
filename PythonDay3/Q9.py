# Q9. Write a python program that read cost from file input() and create userdefined exception
# InvalidProductBillException , raise exception if cost<0 print message – Bill cannot be negative

f = open('cost.txt','r')
str = f.read()
list1 = str.split("\n")
print(list1)
class InvalidProductBillException(Exception):
    pass

for item in list1:
    try:
        if(int(item)>0):
            print("You need to pay amount ",item)
        else :
            raise InvalidProductBillException
    except InvalidProductBillException as e:
        print("Bill cannot be negative")