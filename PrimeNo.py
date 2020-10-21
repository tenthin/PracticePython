check_prime = [26,39,51,53,57,79,85]
for num in check_prime:
    for i in range(2,num):
        if (num % i) == 0:
            print("{} is not a prime,{} is factor of {}".format(num,i,num ))
            break
        if i == num - 1:
             print("{} is a prime no".format(num))

#In this program, variable num is checked if it's prime or not.
#Numbers less than or equal to 1 are not prime numbers.
#Hence, we only proceed if the num is greater than 1.
#We check if num is exactly divisible by any number from 2 to num - 1.
#If we find a factor in that range, the number is not prime. Else the number is prime.
#We can decrease the range of numbers where we look for factors.
#In the above program, our search range is from 2 to num - 1.
# A natural number that is greater than 1 but is not a prime number is known as a composite number.
#Therefore, we cannot include 1 in the list of prime numbers. All lists of prime numbers begin with 2.
#Thus, the smallest prime number is 2 and not 1.