file = open('float_data.txt', 'r')

summ = 0
sumsqr = 0
floatArr = list(map(float, file.readlines()))
summ = sum(floatArr)/10**5
for i in range(10**5):
    sumsqr += floatArr[i]**2
sigm = (sumsqr/10**5 - summ**2)**0.5

print(summ)
print(sigm)
print(max(floatArr), ' ', floatArr.index(max(floatArr)))
print(min(floatArr), ' ', floatArr.index(min(floatArr)))