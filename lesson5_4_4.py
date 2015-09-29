numArr = []
for i in range(int(input())):
    numArr.append(int(input()))
maximum = 0

for i in range(len(numArr)):
    if numArr.count(numArr[i]) > maximum:
        maximum = numArr.count(numArr[i])
        num = numArr[i]
print(num)               
