# Create function called greetings()
# First parameter: first name
# Second parameter: last name
# Last parameter: age

# greetings('Samir', 'Chahine', 21)
# def documents(downloads downloads= documents
#                     print("error")

def primes_sieve2(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    primes = []

    for (number, isprime) in enumerate(a):
        if isprime:
            primes.append(number)

            for n in range(number*number, limit, number):     # Mark factors non-prime
                a[n] = False

    print(sum(primes))


primes_sieve2(2000000)

# def primes_sieve2(limit):
#  a = [True] * limit                          # Initialize the primality list
#  a[0] = a[1] = False
#
#     # 1. make empty list for primes
# (primes):[]
# for (number, isprime) in enumerate('a'):
#         if isprime:
#             # 2. add number to the list
#             prime.append(number)
#
#             for n in range(number*number, limit, number):     # Mark factors non-prime
#                 a[n] = False
#         # 3. print the sum of the list
#         print(primes[number])
