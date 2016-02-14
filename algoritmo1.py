n = 1000
numbers = range(2, n)
results = []

while len(numbers) > 0:
    tmp = numbers[0]
    results.append(tmp)
    i = 0
    numbers = filter(lambda x: x % tmp != 0, numbers)
    print tmp, numbers
            
    
print 'Result:', len(results)
