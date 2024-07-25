y = int(input('lenght of the list'))
x = []
for i in range(y):
    data = int(input('input your data'))
    x = x.append(data)


n = sorted(x)
print("sorted list:",n)
if y % 2 ==0:
    one = y // 2
    two = one + 1
    summation = n[one-1] + n[two-1]
    median_of_center = float(summation/2)
    print("Median of the center:",median_of_center)
else:
    half = int(y // 2)
    median_of_center = n[half]
    print("Median of the center:",median_of_center)
    
