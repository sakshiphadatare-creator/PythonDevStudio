num = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(num[0][1])
print(num[2][1])
print(num[3][0])

for row in num:
    print(row)
    for col in row:
        print(col)

matrix =  [
    [1,2,3],
    [4,5,2],
    [7,8,5]
]
for row in matrix:
    for element in row:
        print(element," " ,end='')
    print()

total_sum = 0
for row in matrix:
    for element in row:
        total_sum += element
print("Total no: ",total_sum)

