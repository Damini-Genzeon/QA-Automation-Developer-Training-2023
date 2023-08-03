# Q12. Write a python program that reads given list and convert list elements into Capitalize format
# and return the result into target file named listupper.txt(use higher order functions if possible)
# input : [ramu,laxman,sita,john] output : [Ramu , Laxman, Sita ,John]

str = input("Enter String : ")
input = list(str.split(","))
output = []
for item in input:
    output.append(item.capitalize())
f = open("listupper.txt","w")
f.write(output[0])
for item in output:
    if(item != output[0]):
        f.write(", "+item)
