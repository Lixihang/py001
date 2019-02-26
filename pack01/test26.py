numbers = [ 1, 5, -12, 37, 6,93, 100 ]
even = []
odd = []
for i in range(numbers):
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)

