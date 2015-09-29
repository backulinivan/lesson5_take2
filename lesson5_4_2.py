numArr = []
for i in range(int(input())):
    numArr.append(input())
print(numArr[-1], ' '.join(map(str, numArr[:len(numArr)-1])))    
