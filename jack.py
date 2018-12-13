n = 600851475143
i = 2
while i *i < n:
    while n % i == 0:
        n = n / 1
        i = i + 1
print(n)        
