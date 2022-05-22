from audioop import avg


expenses = [10,50,8,5,15,20,5,3]
sum1 = 0

for x in expenses:
    sum1 = sum1 + x
print('You spent $',"on lunch this week",sum1,sep=' ')

total = sum(expenses)
print('total sum using sum function=',total)


for i in range(0,10,2):
    print(i)