#Defining a function to check if the number is prime or not.
def prime_checker(number):
  is_prime = True
#If the number is divisible by any other numbers in range [2 to n-1), it's not a prime number
  for x in range(2,n):
    if n % x == 0:
      is_prime = False
  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")
    
#Ask user for a number to check.
n = int(input("Check this number: "))
prime_checker(number=n)
