# Q15. Write a python programs that extract three numbers from file input.txt and find largest of
# three numbers and return output into file largest.tx

nums = []
f1 = open("input.txt","r")
i=0
while(i<3):
    num = f1.readline()
    nums.append(int(num))
    i +=1

max = nums[0]
for item in nums:
    if(item != nums[0]):
        if(item > max):
            max = item

f2 = open("largest.txt","w")
f2.write(str(max))


