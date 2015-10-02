file = open('int_data.txt', 'r')

intArr = list(map(int, file.readlines()))

maxCase = 0
minCase = 100001

for i in range(101):
    caseOf = intArr.count(i)
    if maxCase < caseOf:
        maxCase = caseOf
        maxTimesInt = i
    if minCase > caseOf:
        minCase = caseOf
        minTimesInt = i
print(maxTimesInt, ' ', maxCase, ' times')
print(minTimesInt, ' ', minCase, ' times')

intCase = []
diffCase = 0
for j in range(len(intArr)):
    if intCase.count(intArr[j]) == 0:
        diffCase += 1
print(diffCase, ' various integers')