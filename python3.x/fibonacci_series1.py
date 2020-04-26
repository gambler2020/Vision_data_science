fib_list=[1,1]
for i in range(10):
    fib_list.append(fib_list[-1]+fib_list[-2])
print(fib_list)
