numArr = []
for i in range(int(input())):
    numArr.append(int(input()))
print(' '.join(map(str, numArr[::-1])))       
