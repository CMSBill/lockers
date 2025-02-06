import re

#OPEN = 1
#CLOSED = 0

theLockers = ""
for i in range(100):
    theLockers += "1"
n=2
regex = r"11"
result = re.sub(regex, "10", theLockers, 0)
print(result)
j=1
n+=1
temp = result
temp2 = ""
while n <= 99:
    for i in range(100):
        # print(i)
        if i == 0 or i%n==0:
            temp3 = (temp[i])
            if temp3 == "1":
                temp2+="0"
            else:
                temp2+="1"
            # print(f"{temp2}, {n}, {i}")
        else:
            temp2+= (temp[i])
            # print(f"{temp2}, {n}, {i}")
    print(f"{temp2}, {n}")
    temp=temp2
    n+=1 
    temp2=""
result = temp
ones=0
temp=""
for i in range(100):
    if i != 99 or i != 0:
        temp+=result[i]
    else:
        if result[i] == "1":
            temp+="0"
        else:
            temp+="1"
result=temp

for i in result:
    if i == "1":
        ones+=1
print(f"There are {ones} closed lockers.")
ones=0
for i in result:
    if i == "0":
        ones+=1
print(f"There are {ones} open lockers.")
