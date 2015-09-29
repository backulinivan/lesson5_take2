numArr = []
for i in range(int(input())):
    numArr.append(int(input()))
for i in range(0, len(numArr)-1, 2):
    numArr[i], numArr[i+1] = numArr[i+1], numArr[i]
print(' '.join(map(str, numArr)))               
