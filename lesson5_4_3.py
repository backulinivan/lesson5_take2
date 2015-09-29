numArr = []
for i in range(int(input())):
    numArr.append(int(input()))
for i in range(len(numArr)):
    if numArr.count(numArr[i]) == 1:
        print(numArr[i])       
